#!/usr/bin/env python3
"""Refresh the package-version table for one image tag in a template README.

Usage: update_readme_versions.py <README> <image> <tag> <ref_date YYYY-MM-DD>

Works for both README.md (English) and README.ko.md (Korean); the table header and
the date label ("As of" / "기준일") of each file are kept.

Each tag has its own section under "## 포함 환경", in the existing README format:

    ### `torch2.11-cuda13.0`

    **기준일:** 2026-06-19

    아래 버전은 해당 이미지 기준 스냅샷입니다. ...

    <!-- VERSIONS:torch2.11-cuda13.0:START -->
    | 패키지 | 버전 |
    |---|---|
    | torch | 2.11.0+cu130 |
    <!-- VERSIONS:torch2.11-cuda13.0:END -->

The table between the markers and the 기준일 line of that section are updated.
If the section for <tag> does not exist yet, it is appended after the last
section by copying the first section's format and package list.
"""
import re
import subprocess
import sys

readme_path, image, tag, ref_date = sys.argv[1:5]

txt = open(readme_path, encoding="utf-8").read()

section_re = re.compile(
    r"### `(?P<tag>[^`]+)`\n(?P<head>.*?)<!-- VERSIONS:(?P=tag):START -->\n"
    r"(?P<table>.*?)<!-- VERSIONS:(?P=tag):END -->",
    re.S,
)
sections = list(section_re.finditer(txt))
if not sections:
    print(f"[ERROR] VERSIONS 섹션 없음: {readme_path}", file=sys.stderr)
    sys.exit(1)


def package_names(table):
    names = []
    for line in table.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) != 2 or cells[0] in ("패키지", "Package") or set(cells[0]) <= {"-", ":"}:
            continue
        names.append(cells[0])
    return names


target = next((s for s in sections if s.group("tag") == tag), None)
source = target or sections[0]
pkgs = package_names(source.group("table"))
if not pkgs:
    print(f"[ERROR] 표에서 패키지명을 못 찾음: {readme_path}", file=sys.stderr)
    sys.exit(1)

out = subprocess.run(
    ["docker", "run", "--rm", "--entrypoint", "pip", image, "show", *pkgs],
    capture_output=True, text=True,
)
versions, cur = {}, None
for line in out.stdout.splitlines():
    if line.startswith("Name:"):
        cur = line.split(":", 1)[1].strip()
    elif line.startswith("Version:") and cur:
        versions[cur.lower()] = line.split(":", 1)[1].strip()
        cur = None

# Keep the table header language of this README (e.g. "패키지 | 버전" or "Package | Version").
header = next((l.strip() for l in source.group("table").splitlines() if l.strip().startswith("|")), "| 패키지 | 버전 |")
rows, missing = [header, "|---|---|"], []
for p in pkgs:
    v = versions.get(p.lower())
    if v is None:
        missing.append(p)
        v = "(미확인)"
    rows.append(f"| {p} | {v} |")

head = re.sub(r"\*\*(기준일|As of):\*\*\s*\d{4}-\d{2}-\d{2}", lambda m: f"**{m.group(1)}:** {ref_date}", source.group("head"))
section = (
    f"### `{tag}`\n{head}<!-- VERSIONS:{tag}:START -->\n"
    + "\n".join(rows)
    + f"\n<!-- VERSIONS:{tag}:END -->"
)

if target:
    txt = txt[:target.start()] + section + txt[target.end():]
else:
    end = sections[-1].end()
    txt = txt[:end] + "\n\n" + section + txt[end:]

open(readme_path, "w", encoding="utf-8").write(txt)
print(f"[OK] {readme_path} [{tag}] 갱신 완료 (패키지 {len(pkgs)}개)")
if missing:
    print(f"[WARN] pip show에서 못 찾은 패키지: {missing}", file=sys.stderr)
