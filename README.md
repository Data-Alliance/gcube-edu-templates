# gcube-edu-templates

gcube GPU 플랫폼용 교육용 컨테이너 이미지 템플릿 모음입니다. 대학 GPU 실습 수업 유형별로 필요한 패키지를 사전 구성한 이미지로, 워크로드를 배포하면 바로 JupyterLab에서 실습을 시작할 수 있습니다.

## 템플릿 목록

| 이미지 | 대상 수업 | 주요 패키지 |
|---|---|---|
| `edu-dl-tensorflow` | TensorFlow/Keras 딥러닝 | TensorFlow 2.17, JupyterLab, scikit-learn, Matplotlib |
| `edu-cv-pytorch` | CNN, 전이학습, 컴퓨터비전 | PyTorch, OpenCV, albumentations, scikit-learn, Matplotlib |
| `edu-ml-data` | 기초 ML, 데이터분석 | pandas, scikit-learn, statsmodels, plotly, seaborn |
| `edu-nlp-hf` | NLP, Transformer, LLM 입문 | transformers, datasets, accelerate, sentencepiece, evaluate |
| `edu-rl-pytorch` | 강화학습 | gymnasium, stable-baselines3, tensorboard |
| `edu-genai-sd` | Stable Diffusion, 이미지 생성 | diffusers, transformers, accelerate, safetensors |
| `edu-llm-train` | LLM 파인튜닝, RAG | peft, trl, bitsandbytes, faiss-cpu |

각 이미지의 상세 구성은 해당 폴더의 README를 참고하세요.

## 공통 사항

- 베이스: `gcube-base-images`의 pytorch 또는 ubuntu 계열 이미지
- 작업 디렉터리: `/workspace`
- 포트: `8888` (JupyterLab 자동 실행)
- git 자동 설정 및 저장소 자동 clone(`GIT_CLONE_REPO`) 기능은 베이스에서 상속

| 환경변수 | 설명 |
|---|---|
| `JUPYTER_TOKEN` | JupyterLab 접속 토큰. 미지정 시 토큰 없이 접속 |
| `GIT_CLONE_REPO` | 워크로드 시작 시 `/workspace`에 자동 clone할 저장소 URL |

## 이미지 주소

```
# GitHub Container Registry
ghcr.io/<owner>/<이미지명>:latest

# Docker Hub
<owner>/<이미지명>:latest
```

두 레지스트리에 동일한 이미지가 제공됩니다.