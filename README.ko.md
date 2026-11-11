# gcube-edu-templates

[English](README.md) | **한국어**

gcube GPU 플랫폼용 교육용 컨테이너 이미지 템플릿 모음입니다. 대학 GPU 실습 수업 유형별로 필요한 패키지를 사전 구성한 이미지로, 워크로드를 배포하면 바로 JupyterLab에서 실습을 시작할 수 있습니다.

## 템플릿 목록

| 이미지 | 대상 수업 | GPU 권장 |
|---|---|---|
| `edu-dl-tensorflow` | TensorFlow/Keras 딥러닝 | VRAM 8GB 이상 |
| `edu-cv-pytorch` | CNN, 전이학습, 컴퓨터비전 | VRAM 8GB 이상 |
| `edu-ml-data` | 기초 ML, 데이터분석 | VRAM 8GB 이상 |
| `edu-nlp-hf` | NLP, Transformer, LLM 입문 | VRAM 8GB 이상 |
| `edu-rl-pytorch` | 강화학습 | VRAM 8GB 이상 |
| `edu-genai-sd` | Stable Diffusion, 이미지 생성 | VRAM 16GB 이상 |
| `edu-llm-train` | LLM 파인튜닝, RAG | VRAM 16GB 이상 |
| `edu-audio-pytorch` | 음성인식, 오디오 처리 | VRAM 8GB 이상 |
| `edu-medical-monai` | 의료영상 분석 | VRAM 8GB 이상 |
| `edu-geo-gdal` | 원격탐사, 위성영상 | VRAM 8GB 이상 |
| `edu-gnn-pyg` | 그래프 신경망(GNN) | VRAM 8GB 이상 |

각 이미지의 상세 구성은 해당 폴더의 README를 참고하세요.

## 사용

gcube 워크로드 배포 시 이미지 주소만 바꿔서 사용합니다. 포트는 모두 `8888`(JupyterLab 자동 실행), 작업 디렉터리는 `/workspace`로 동일합니다.

**GitHub Container Registry**

| # | 이미지 | 주소 | 주소 (CUDA 12.8) |
|---|---|---|---|
| 1 | edu-dl-tensorflow | `ghcr.io/data-alliance/edu-dl-tensorflow:tf2.17-cuda12.8` | (왼쪽과 동일) |
| 2 | edu-cv-pytorch | `ghcr.io/data-alliance/edu-cv-pytorch:torch2.11-cuda13.0` | `ghcr.io/data-alliance/edu-cv-pytorch:torch2.11-cuda12.8` |
| 3 | edu-ml-data | `ghcr.io/data-alliance/edu-ml-data:ubuntu24.04-cuda13.0` | `ghcr.io/data-alliance/edu-ml-data:ubuntu24.04-cuda12.8` |
| 4 | edu-nlp-hf | `ghcr.io/data-alliance/edu-nlp-hf:torch2.11-cuda13.0` | `ghcr.io/data-alliance/edu-nlp-hf:torch2.11-cuda12.8` |
| 5 | edu-rl-pytorch | `ghcr.io/data-alliance/edu-rl-pytorch:torch2.11-cuda13.0` | `ghcr.io/data-alliance/edu-rl-pytorch:torch2.11-cuda12.8` |
| 6 | edu-genai-sd | `ghcr.io/data-alliance/edu-genai-sd:torch2.11-cuda13.0` | `ghcr.io/data-alliance/edu-genai-sd:torch2.11-cuda12.8` |
| 7 | edu-llm-train | `ghcr.io/data-alliance/edu-llm-train:torch2.11-cuda13.0` | `ghcr.io/data-alliance/edu-llm-train:torch2.11-cuda12.8` |
| 8 | edu-audio-pytorch | `ghcr.io/data-alliance/edu-audio-pytorch:torch2.11-cuda13.0` | `ghcr.io/data-alliance/edu-audio-pytorch:torch2.11-cuda12.8` |
| 9 | edu-medical-monai | `ghcr.io/data-alliance/edu-medical-monai:torch2.11-cuda13.0` | `ghcr.io/data-alliance/edu-medical-monai:torch2.11-cuda12.8` |
| 10 | edu-geo-gdal | `ghcr.io/data-alliance/edu-geo-gdal:torch2.11-cuda13.0` | `ghcr.io/data-alliance/edu-geo-gdal:torch2.11-cuda12.8` |
| 11 | edu-gnn-pyg | `ghcr.io/data-alliance/edu-gnn-pyg:torch2.11-cuda13.0` | `ghcr.io/data-alliance/edu-gnn-pyg:torch2.11-cuda12.8` |

노드의 NVIDIA 드라이버 버전에 맞는 주소를 사용합니다. `주소` 열은 CUDA 13.0(드라이버 580 이상, `edu-dl-tensorflow`만 CUDA 12.8)이며 `latest`와 동일하고, `주소 (CUDA 12.8)` 열은 드라이버 570 이상에서 사용합니다. `edu-ml-data`는 베이스가 Ubuntu 버전별로 제공되어 태그에 Ubuntu 버전도 표시합니다. 태그별 패키지 버전은 각 템플릿 폴더의 README를 참고하세요.

**Docker Hub**

같은 이미지가 Docker Hub [`gcubeai`](https://hub.docker.com/u/gcubeai)에도 같은 이름·태그로 있습니다.

| # | 이미지 | 주소 | 주소 (CUDA 12.8) |
|---|---|---|---|
| 1 | edu-dl-tensorflow | `gcubeai/edu-dl-tensorflow:tf2.17-cuda12.8` | (왼쪽과 동일) |
| 2 | edu-cv-pytorch | `gcubeai/edu-cv-pytorch:torch2.11-cuda13.0` | `gcubeai/edu-cv-pytorch:torch2.11-cuda12.8` |
| 3 | edu-ml-data | `gcubeai/edu-ml-data:ubuntu24.04-cuda13.0` | `gcubeai/edu-ml-data:ubuntu24.04-cuda12.8` |
| 4 | edu-nlp-hf | `gcubeai/edu-nlp-hf:torch2.11-cuda13.0` | `gcubeai/edu-nlp-hf:torch2.11-cuda12.8` |
| 5 | edu-rl-pytorch | `gcubeai/edu-rl-pytorch:torch2.11-cuda13.0` | `gcubeai/edu-rl-pytorch:torch2.11-cuda12.8` |
| 6 | edu-genai-sd | `gcubeai/edu-genai-sd:torch2.11-cuda13.0` | `gcubeai/edu-genai-sd:torch2.11-cuda12.8` |
| 7 | edu-llm-train | `gcubeai/edu-llm-train:torch2.11-cuda13.0` | `gcubeai/edu-llm-train:torch2.11-cuda12.8` |
| 8 | edu-audio-pytorch | `gcubeai/edu-audio-pytorch:torch2.11-cuda13.0` | `gcubeai/edu-audio-pytorch:torch2.11-cuda12.8` |
| 9 | edu-medical-monai | `gcubeai/edu-medical-monai:torch2.11-cuda13.0` | `gcubeai/edu-medical-monai:torch2.11-cuda12.8` |
| 10 | edu-geo-gdal | `gcubeai/edu-geo-gdal:torch2.11-cuda13.0` | `gcubeai/edu-geo-gdal:torch2.11-cuda12.8` |
| 11 | edu-gnn-pyg | `gcubeai/edu-gnn-pyg:torch2.11-cuda13.0` | `gcubeai/edu-gnn-pyg:torch2.11-cuda12.8` |

## 환경변수

모든 환경변수는 선택 사항입니다. 비공개 저장소를 사용하거나 커밋 작성자를 지정하려는 경우에만 입력합니다.

| 변수 | 기본값 | 설명 |
|---|---|---|
| `JUPYTER_TOKEN` | (없음) | JupyterLab 접속 토큰. 미지정 시 토큰 없이 접속 |
| `GIT_CLONE_REPO` | (없음) | 워크로드 시작 시 `/workspace`에 자동 clone할 저장소 URL. 네트워크 연결이 늦게 열리는 노드를 위해 실패 시 최대 1분간 재시도 |
| `GIT_USER_NAME` | (없음) | git 커밋 작성자 이름 |
| `GIT_USER_EMAIL` | (없음) | git 커밋 작성자 이메일 |
| `GIT_TOKEN` | (없음) | git 인증 토큰(PAT). private 저장소 clone/push 시 필요 |
| `GIT_HOST` | `github.com` | git 호스트. GitLab(`gitlab.com`) 또는 사내 git 서버 주소도 가능 |