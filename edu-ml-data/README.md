# edu-ml-data

기초 머신러닝·데이터분석 교육용 이미지. `gcube-ubuntu` 베이스에 JupyterLab과 데이터분석·ML 실습 패키지를 포함합니다. 데이터 전처리, 시각화, 기초 ML 알고리즘 수업에 사용합니다.

## 구성

| 항목 | 내용 |
|---|---|
| 기반 | `gcube-ubuntu24.04-cuda13.0` (CUDA 환경) |
| 작업 디렉터리 | `/workspace` |
| 포트 | 8888 |

## 사용

gcube 워크로드 배포 시 아래 설정으로 사용합니다.

| 항목 | 값 |
|---|---|
| 이미지 (권장) | `public.ecr.aws/g3x5o1w3/gcube/edu/ml-data:latest` |
| 이미지 (대안) | `ghcr.io/data-alliance/edu-ml-data:latest` |
| 포트 | 8888 |
| GPU | VRAM 8GB 이상 |

배포 후 서비스 URL로 접속하면 JupyterLab이 열립니다.

AWS ECR이 GitHub Container Registry보다 다운로드 속도가 빠르기 때문에 사용을 권장합니다.

## 포함 환경

**기준일:** 2026-06-19

아래 버전은 해당 이미지 기준 스냅샷입니다. 컨테이너 터미널에서 `pip show <패키지>`로 현재 설치된 버전을 확인할 수 있습니다.

<!-- VERSIONS:START -->
| 패키지 | 버전 |
|---|---|
| NumPy | 2.5.0 |
| pandas | 3.0.3 |
| scikit-learn | 1.9.0 |
| SciPy | 1.18.0 |
| statsmodels | 0.14.6 |
| Matplotlib | 3.11.0 |
| seaborn | 0.13.2 |
| Plotly | 6.8.0 |
| openpyxl | 3.1.5 |
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