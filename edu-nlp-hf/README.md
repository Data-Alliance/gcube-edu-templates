# edu-nlp-hf

Hugging Face 기반 자연어처리 교육용 이미지. `gcube-pytorch` 베이스에 JupyterLab과 Hugging Face 생태계 패키지를 포함합니다. Transformer, BERT, 텍스트 분류·생성 등 NLP·LLM 입문 수업에 사용합니다.

## 구성

| 항목 | 내용 |
|---|---|
| 기반 | `gcube-pytorch-<torch>-cuda<cuda>` (torch 포함) |
| 패키지 | JupyterLab, ipykernel, transformers, datasets, tokenizers, sentencepiece, accelerate, evaluate, tensorboard, scikit-learn, tqdm |
| 작업 디렉터리 | `/workspace` |
| 포트 | 8888 |

```
ghcr.io/<owner>/edu-nlp-hf:latest
```

Hugging Face 표준 구성(transformers, datasets, tokenizers, accelerate)에 평가(evaluate, scikit-learn)와 학습 시각화(tensorboard)를 더해, 모델 불러오기부터 미세조정·평가까지 NLP 실습 흐름 전체를 지원합니다. sentencepiece가 포함되어 한국어·다국어 모델 토크나이저를 사용할 수 있습니다.

모델 파일은 이미지에 포함하지 않으며, 실행 시 Hugging Face Hub에서 내려받아 `/workspace/.cache/huggingface`(베이스의 `HF_HOME`)에 저장됩니다. 작업 볼륨을 `/workspace`에 마운트하면 모델 캐시가 유지됩니다.

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