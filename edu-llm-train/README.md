# edu-llm-train

LLM 파인튜닝·RAG 교육용 이미지. `gcube-pytorch` 베이스에 JupyterLab과 LLM 파인튜닝 표준 패키지를 포함합니다. LoRA·QLoRA 파인튜닝, RAG 실습 수업에 사용합니다.

## 구성

| 항목 | 내용 |
|---|---|
| 기반 | `gcube-pytorch-2.11-cuda13.0` (PyTorch 포함) |
| 작업 디렉터리 | `/workspace` |
| 포트 | 8888 |

## 사용

gcube 워크로드 배포 시 아래 설정으로 사용합니다.

| 항목 | 값 |
|---|---|
| 이미지 | `chaeyoon08/edu-llm-train:latest` |
| 포트 | 8888 |
| GPU | VRAM 16GB 이상 |

배포 후 서비스 URL로 접속하면 JupyterLab이 열립니다.

이미지는 GitHub Container Registry에서도 받을 수 있습니다.

```
ghcr.io/data-alliance/edu-llm-train:latest
chaeyoon08/edu-llm-train:latest
```

## 포함 환경

**기준일:** 2026-06-19

아래 버전은 해당 이미지 기준 스냅샷입니다. 컨테이너 터미널에서 `pip show <패키지>`로 현재 설치된 버전을 확인할 수 있습니다.

<!-- VERSIONS:START -->
| 패키지 | 버전 |
|---|---|
| transformers | 5.12.1 |
| tokenizers | (자동 입력) |
| datasets | 5.0.0 |
| peft | 0.19.1 |
| trl | 1.6.0 |
| bitsandbytes | 0.49.2 |
| accelerate | 1.14.0 |
| faiss-cpu | 1.14.3 |
| sentencepiece | 0.2.1 |
| einops | 0.8.2 |
| evaluate | 0.4.6 |
| scikit-learn | 1.9.0 |
| tensorboard | 2.20.0 |
| tqdm | 4.68.3 |
| ipywidgets | 8.1.8 |
<!-- VERSIONS:END -->

## 환경변수

모든 환경변수는 선택 사항입니다. 비공개 저장소를 사용하거나 커밋 작성자를 지정하려는 경우에만 입력합니다.

| 변수 | 기본값 | 설명 |
|---|---|---|
| `JUPYTER_TOKEN` | (없음) | JupyterLab 접속 토큰. 미지정 시 토큰 없이 접속 |
| `GIT_CLONE_REPO` | (없음) | 워크로드 시작 시 `/workspace`에 자동 clone할 저장소 URL |
| `GIT_USER_NAME` | (없음) | git 커밋 작성자 이름 |
| `GIT_USER_EMAIL` | (없음) | git 커밋 작성자 이메일 |
| `GIT_TOKEN` | (없음) | git 인증 토큰(PAT). private 저장소 clone/push 시 필요 |
| `GIT_HOST` | `github.com` | git 호스트. GitLab(`gitlab.com`) 또는 사내 git 서버 주소도 가능 |