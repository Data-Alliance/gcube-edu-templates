#!/usr/bin/env python3
"""Build Docker Hub descriptions for the gcubeai organization.

Writes tools/dockerhub/descriptions.json with, for every repository:
  - description:      short one-line description (English, max 100 chars)
  - full_description: Overview page (English first, then Korean)

EDU template text comes from edu-*/README.md (English) and edu-*/README.ko.md
(Korean) in this repository, so edit the READMEs and re-run this script.
Base image text is generated from the image name.

Usage (from the repository root):
    python3 tools/dockerhub/render.py
    python3 tools/dockerhub/update.py --dry-run
"""
import glob
import json
import os
import re
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
NS = "gcubeai"
GH_T = "https://github.com/Data-Alliance/gcube-edu-templates"
GH_B = "https://github.com/Data-Alliance/gcube-base-images"
GH_E = "https://github.com/Data-Alliance/gcube-edu-examples"
KO_NOTE = "> 한국어 설명은 아래에 있습니다."


def intro(path):
    """First paragraph after the title and the language switch line."""
    paras = [p.strip() for p in open(path, encoding="utf-8").read().split("\n\n") if p.strip()]
    return next(p for p in paras[1:] if not p.startswith(("**English**", "[English]")))


def image_tags(path):
    """Tags from the GHCR image rows of the usage table, e.g. ('torch2.11-cuda13.0', True)."""
    tags = []
    for line in open(path, encoding="utf-8"):
        m = re.match(r"\| (Image|이미지)( \(CUDA 12\.8\))? \| `ghcr\.io/[^:`]+:([^`]+)`", line)
        if m:
            tags.append((m.group(3), m.group(2) is None))
    return tags


def cuda_driver(tag):
    cuda = re.search(r"cuda([\d.]+)", tag).group(1)
    return cuda, {"13.0": "580", "12.8": "570"}[cuda]


def edu(name):
    en_intro = intro(f"{ROOT}/{name}/README.md")
    ko_intro = intro(f"{ROOT}/{name}/README.ko.md")
    tags = image_tags(f"{ROOT}/{name}/README.md")
    first = en_intro.split(". ")[0].rstrip(".")
    short = f"[EDU Template] {first} · JupyterLab"
    if len(short) > 100:
        short = f"[EDU Template] {name} · JupyterLab"
    rows_en = "\n".join(f"| `{t}`{' (= `latest`)' if latest else ''} | {cuda_driver(t)[0]} | {cuda_driver(t)[1]} or later |" for t, latest in tags)
    rows_ko = "\n".join(f"| `{t}`{' (= `latest`)' if latest else ''} | {cuda_driver(t)[0]} | {cuda_driver(t)[1]} 이상 |" for t, latest in tags)
    default = tags[0][0]
    run = f"""```bash
docker run --gpus all -p 8888:8888 \\
  -e GIT_CLONE_REPO={GH_E}.git \\
  {NS}/{name}:{default}
```"""
    full = f"""# {name}

{KO_NOTE}

## English

{en_intro}

An educational container image for the gcube GPU platform. JupyterLab starts on port `8888` when the container runs.

### Tags

| Tag | CUDA | NVIDIA driver |
|---|---|---|
{rows_en}

Pick the tag that matches the node's NVIDIA driver (check with `nvidia-smi`).

### Usage

{run}

With `GIT_CLONE_REPO`, the lab examples are cloned into `/workspace` at startup.

### Documentation

- Template contents and package versions: {GH_T}/tree/main/{name}
- Lab example notebooks: {GH_E}/tree/main/{name}
- Choosing a tag and pinned versions: {GH_E}/blob/main/VERSIONS.md

The same image is also on GitHub Container Registry: `ghcr.io/data-alliance/{name}`

---

## 한국어

{ko_intro}

gcube GPU 플랫폼의 교육용 컨테이너 이미지입니다. 컨테이너를 실행하면 JupyterLab이 포트 `8888`에서 바로 열립니다.

### 태그

| 태그 | CUDA | NVIDIA 드라이버 |
|---|---|---|
{rows_ko}

노드의 NVIDIA 드라이버 버전에 맞는 태그를 선택하세요(`nvidia-smi`로 확인).

### 사용

{run}

`GIT_CLONE_REPO`를 지정하면 시작 시 `/workspace`에 실습 예제를 자동으로 받습니다.

### 문서

- 템플릿 구성·패키지 버전: {GH_T}/blob/main/{name}/README.ko.md
- 실습 예제 노트북: {GH_E}/blob/main/{name}/README.ko.md
- 태그 선택과 버전 고정 안내: {GH_E}/blob/main/VERSIONS.ko.md

같은 이미지가 GitHub Container Registry에도 있습니다: `ghcr.io/data-alliance/{name}`
"""
    return {"description": short, "full_description": full}


def base(name):
    m = re.match(r"gcube-pytorch-(\d+\.\d+)-cuda([\d.]+)$", name)
    if m:
        t, c = m.groups()
        ub = "22.04" if t in ("2.8", "2.9") else "24.04"
        short = f"[Base] PyTorch {t} + CUDA {c} · Ubuntu {ub}"
        en = f"Base image with PyTorch {t}, CUDA {c}, cuDNN, and Python. Based on the official PyTorch image (`pytorch/pytorch`), Ubuntu {ub}."
        ko = f"PyTorch {t}, CUDA {c}, cuDNN, Python이 포함된 베이스 이미지입니다. PyTorch 공식 이미지(`pytorch/pytorch`) 기반이며 Ubuntu {ub}입니다."
        tags = "`runtime`, `devel`"
    m = re.match(r"gcube-ubuntu([\d.]+)-cuda([\d.]+)$", name)
    if m:
        u, c = m.groups()
        short = f"[Base] Ubuntu {u} + CUDA {c}"
        en = f"Base image with only Ubuntu {u} and CUDA {c} (with cuDNN), for installing your own framework. Based on the official NVIDIA CUDA image (`nvidia/cuda`)."
        ko = f"Ubuntu {u}와 CUDA {c}(cuDNN 포함)만 들어 있어, 원하는 프레임워크를 직접 설치하는 베이스 이미지입니다. NVIDIA 공식 CUDA 이미지(`nvidia/cuda`) 기반입니다."
        if u == "26.04":
            en += " The default Python is 3.14, and an NVIDIA driver that supports CUDA 13.5 is required."
            ko += " 기본 Python은 3.14이며, CUDA 13.5를 지원하는 NVIDIA 드라이버가 필요합니다."
        tags = "`runtime`, `devel`"
    m = re.match(r"gcube-tensorflow-([\d.]+)-cuda([\d.]+)$", name)
    if m:
        t, c = m.groups()
        short = f"[Base] TensorFlow {t} + CUDA {c} · Ubuntu 24.04"
        en = f"Base image with TensorFlow {t}, CUDA {c}, cuDNN, and Python. TensorFlow is taken from the NVIDIA NGC TensorFlow 25.02 container, so the RTX 50 series (Blackwell) is supported."
        ko = f"TensorFlow {t}, CUDA {c}, cuDNN, Python이 포함된 베이스 이미지입니다. NVIDIA NGC TensorFlow 25.02의 TensorFlow를 옮겨 담아 RTX 50 시리즈(Blackwell)까지 지원합니다."
        tags = "`runtime`"
    dockerfile = f"""```dockerfile
FROM {NS}/{name}:runtime
RUN pip install --no-cache-dir <package>
```"""
    full = f"""# {name}

{KO_NOTE}

## English

{en}

Includes the common gcube settings: Korean font (NanumGothic), UTF-8 locale, git, `/workspace` working directory, and automatic clone via `GIT_CLONE_REPO`.

### Tags

{tags}

### Usage

{dockerfile}

### Documentation

- Full lineup and environment variables: {GH_B}

The same image is also on GitHub Container Registry: `ghcr.io/data-alliance/{name}`

---

## 한국어

{ko}

gcube GPU 플랫폼용 공통 설정(나눔고딕 한글 폰트, UTF-8 로케일, git, `/workspace` 작업 디렉터리, `GIT_CLONE_REPO` 자동 clone)이 들어 있습니다.

### 태그

{tags}

### 사용

{dockerfile.replace("<package>", "<필요한 패키지>")}

### 문서

- 전체 라인업·환경변수: {GH_B}/blob/main/README.ko.md

같은 이미지가 GitHub Container Registry에도 있습니다: `ghcr.io/data-alliance/{name}`
"""
    return {"description": short, "full_description": full}


def main():
    url = f"https://hub.docker.com/v2/repositories/{NS}/?page_size=100"
    repos = []
    while url:
        page = json.load(urllib.request.urlopen(url, timeout=30))
        repos += [r["name"] for r in page["results"]]
        url = page.get("next")
    out = {}
    for name in sorted(repos):
        if os.path.isdir(f"{ROOT}/{name}") and name.startswith("edu-"):
            out[name] = edu(name)
        elif name.startswith("gcube-"):
            out[name] = base(name)
        else:
            print(f"skip {name}: unknown repository")
    for name, d in out.items():
        assert len(d["description"]) <= 100, (name, len(d["description"]))
    json.dump(out, open(f"{HERE}/descriptions.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"wrote {len(out)} descriptions to {HERE}/descriptions.json")


if __name__ == "__main__":
    main()
