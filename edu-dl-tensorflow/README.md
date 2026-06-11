# edu-dl-tensorflow

TensorFlow 기반 딥러닝 교육용 이미지. `gcube-tensorflow` 베이스에 JupyterLab과 표준 데이터 분석 패키지를 포함합니다.

## 구성

| 항목 | 내용 |
|---|---|
| 기반 | `gcube-tensorflow-<tf>-cuda<cuda>` |
| 패키지 | JupyterLab, NumPy, SciPy, scikit-learn, Matplotlib, Pillow, tqdm |
| 작업 디렉터리 | `/workspace` |
| 포트 | 8888 |

```
ghcr.io/<owner>/edu-dl-tensorflow:latest
```

## 실행

컨테이너 시작 시 JupyterLab이 자동 실행되며, `/workspace`를 작업 디렉터리로 사용합니다.

## 환경변수

| 변수 | 기본값 | 설명 |
|---|---|---|
| `JUPYTER_TOKEN` | (없음) | 접속 토큰. 미지정 시 토큰 없이 접속 가능 |

git 구성 및 작업 저장소 자동 clone 관련 환경변수(`GIT_USER_NAME`, `GIT_TOKEN`, `GIT_CLONE_REPO` 등)는 베이스 이미지에서 상속됩니다.

## 빌드

GitHub Actions의 수동 실행(workflow_dispatch)으로 빌드하며, 템플릿·베이스 이미지·태그를 선택할 수 있습니다. ghcr.io와 Docker Hub에 동시 푸시됩니다.

베이스 이미지(`gcube-tensorflow`)가 먼저 빌드되어 있어야 합니다.