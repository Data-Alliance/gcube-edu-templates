# edu-genai-sd

생성형 AI(이미지 생성) 교육용 이미지. `gcube-pytorch` 베이스에 JupyterLab과 Hugging Face Diffusers 생태계 패키지를 포함합니다. Stable Diffusion 등 이미지 생성 모델 실습 수업에 사용합니다.

## 구성

| 항목 | 내용 |
|---|---|
| 기반 | `gcube-pytorch-<torch>-cuda<cuda>` (torch 포함) |
| 패키지 | JupyterLab, ipykernel, diffusers, transformers, accelerate, safetensors, datasets, invisible-watermark, OpenCV(headless), Pillow, tqdm |
| 작업 디렉터리 | `/workspace` |
| 포트 | 8888 |

```
ghcr.io/<owner>/edu-genai-sd:latest
```

Hugging Face Diffusers 표준 구성(diffusers, transformers, accelerate, safetensors)에 데이터셋 로드(datasets)와 SDXL 호환에 필요한 invisible-watermark를 더해, 이미지 생성부터 LoRA·DreamBooth 등 파인튜닝까지 수업 흐름 전체를 지원합니다. 이미지 후처리·표시를 위한 OpenCV와 Pillow도 포함되어 있습니다.

모델 파일은 이미지에 포함하지 않으며, 실행 시 Hugging Face Hub에서 내려받아 `/workspace/.cache/huggingface`(베이스의 `HF_HOME`)에 저장됩니다. Stable Diffusion 모델은 VRAM 사용량이 크므로 Tier2 환경 사용을 권장합니다.

## 실행

컨테이너 시작 시 JupyterLab이 자동 실행되며, `/workspace`를 작업 디렉터리로 사용합니다.

## 환경변수

| 변수 | 기본값 | 설명 |
|---|---|---|
| `JUPYTER_TOKEN` | (없음) | 접속 토큰. 미지정 시 토큰 없이 접속 가능 |

git 구성 및 작업 저장소 자동 clone 관련 환경변수(`GIT_USER_NAME`, `GIT_TOKEN`, `GIT_CLONE_REPO` 등)는 베이스 이미지에서 상속됩니다.

## 빌드

GitHub Actions의 수동 실행(workflow_dispatch)으로 빌드하며, 템플릿·베이스 이미지·태그를 선택할 수 있습니다. ghcr.io와 Docker Hub에 동시 푸시됩니다.

베이스 이미지(`gcube-pytorch`)가 먼저 빌드되어 있어야 합니다.