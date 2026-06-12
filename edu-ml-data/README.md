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

| 변수 | 기본값 | 설명 |
|---|---|---|
| `JUPYTER_TOKEN` | (없음) | 접속 토큰. 미지정 시 토큰 없이 접속 가능 |

git 구성 및 작업 저장소 자동 clone 관련 환경변수(`GIT_USER_NAME`, `GIT_TOKEN`, `GIT_CLONE_REPO` 등)는 베이스 이미지에서 상속됩니다.

## 빌드

GitHub Actions의 수동 실행(workflow_dispatch)으로 빌드하며, 템플릿·베이스 이미지·태그를 선택할 수 있습니다. ghcr.io와 Docker Hub에 동시 푸시됩니다.

베이스 이미지(`gcube-ubuntu`)가 먼저 빌드되어 있어야 합니다.