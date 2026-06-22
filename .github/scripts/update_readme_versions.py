#!/usr/bin/env python3
import re, sys, subprocess, json
from datetime import date

# 사용법: update_readme_versions.py <README경로> <docker이미지> <기준일YYYY-MM-DD>
readme_path = sys.argv[1]
image = sys.argv[2]
ref_date = sys.argv[3] if len(sys.argv) > 3 else date.today().isoformat()

txt = open(readme_path, encoding="utf-8").read()

m = re.search(r"(<!-- VERSIONS:START -->)(.*?)(<!-- VERSIONS:END -->)", txt, re.S)
if not m:
    print(f"[ERROR] VERSIONS 마커 없음: {readme_path}", file=sys.stderr)
    sys.exit(1)

block = m.group(2)

# 표에서 패키지명 추출 (헤더/구분선 제외)
pkgs = []
for line in block.splitlines():
    line = line.strip()
    if not line.startswith("|"):
        continue
    cells = [c.strip() for c in line.strip("|").split("|")]
    if len(cells) != 2:
        continue
    if cells[0] in ("패키지", "---") or set(cells[0]) <= {"-", ":"}:
        continue
    pkgs.append(cells[0])

if not pkgs:
    print(f"[ERROR] 표에서 패키지명을 못 찾음: {readme_path}", file=sys.stderr)
    sys.exit(1)

# 이미지에서 pip show 실행 (소문자 정규화로 매칭)
def pip_versions(image, names):
    # pip show는 여러 패키지 한 번에 가능
    out = subprocess.run(
        ["docker", "run", "--rm", image, "pip", "show", *names],
        capture_output=True, text=True
    )
    versions = {}
    cur = None
    for line in out.stdout.splitlines():
        if line.startswith("Name:"):
            cur = line.split(":", 1)[1].strip()
        elif line.startswith("Version:") and cur:
            versions[cur.lower()] = line.split(":", 1)[1].strip()
            cur = None
    return versions

ver = pip_versions(image, pkgs)

# 새 표 생성 (역할 없는 2열, 기존 패키지명 표기 유지)
lines = ["| 패키지 | 버전 |", "|---|---|"]
missing = []
for p in pkgs:
    v = ver.get(p.lower())
    if v is None:
        missing.append(p)
        v = "(미확인)"
    lines.append(f"| {p} | {v} |")
new_table = "\n".join(lines)

# 마커 사이 교체
new_block = f"\n{new_table}\n"
new_txt = txt[:m.start(2)] + new_block + txt[m.end(2):]

# 기준일 갱신
new_txt = re.sub(r"\*\*기준일:\*\*\s*\d{4}-\d{2}-\d{2}", f"**기준일:** {ref_date}", new_txt)

open(readme_path, "w", encoding="utf-8").write(new_txt)

print(f"[OK] {readme_path} 갱신 완료 (패키지 {len(pkgs)}개)")
if missing:
    print(f"[WARN] pip show에서 못 찾은 패키지: {missing}", file=sys.stderr)