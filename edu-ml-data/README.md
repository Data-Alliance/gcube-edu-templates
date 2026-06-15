# edu-ml-data

기초 머신러닝·데이터분석 교육용 이미지. `gcube-ubuntu` 베이스에 JupyterLab과 데이터분석 표준 패키지를 포함합니다. 데이터 전처리, 시각화, 회귀·분류 등 기초 AI·데이터분석 수업에 사용합니다.

## 구성

| 항목 | 내용 |
|---|---|
| 기반 | `gcube-ubuntu<ubuntu>-cuda<cuda>` |
| 패키지 | JupyterLab, ipykernel, NumPy, pandas, SciPy, Matplotlib, seaborn, scikit-learn, statsmodels, plotly, openpyxl, tqdm |
| 작업 디렉터리 | `/workspace` |
| 포트 | 8888 |

```
ghcr.io/<owner>/edu-ml-data:latest
```

딥러닝 프레임워크를 포함하지 않는 가벼운 이미지로, 데이터 다루기(pandas, openpyxl), 시각화(Matplotlib, seaborn, plotly), 머신러닝(scikit-learn), 통계 분석(statsmodels)까지 기초 데이터분석 수업 흐름 전체를 지원합니다.

## 실행

컨테이너 시작 시 JupyterLab이 자동 실행되며, `/workspace`를 작업 디렉터리로 사용합니다.

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


## 빌드

GitHub Actions의 수동 실행(workflow_dispatch)으로 빌드하며, 템플릿·베이스 이미지·태그를 선택할 수 있습니다. ghcr.io와 Docker Hub에 동시 푸시됩니다.

베이스 이미지(`gcube-ubuntu`)가 먼저 빌드되어 있어야 합니다.