# edu-llm-train

LLM 파인튜닝·RAG 교육용 이미지. `gcube-pytorch` 베이스에 JupyterLab과 LLM 파인튜닝 표준 패키지를 포함합니다. LoRA·QLoRA 파인튜닝, SFTTrainer를 이용한 지도학습, RAG(검색 증강 생성) 등 대학원 세미나·고급 LLM 실습에 사용합니다.

## 구성

| 항목 | 내용 |
|---|---|
| 기반 | `gcube-pytorch-<torch>-cuda<cuda>` (torch 포함) |
| 패키지 | JupyterLab, ipykernel, transformers, datasets, tokenizers, sentencepiece, accelerate, peft, trl, bitsandbytes, einops, evaluate, tensorboard, scikit-learn, faiss-cpu, tqdm |
| 작업 디렉터리 | `/workspace` |
| 포트 | 8888 |

```
ghcr.io/<owner>/edu-llm-train:latest
```

LLM 파인튜닝의 표준 조합인 PEFT(LoRA·QLoRA), bitsandbytes(4-bit 양자화), TRL(SFTTrainer)에 데이터 로드(datasets), 평가(evaluate, scikit-learn), 학습 모니터링(tensorboard)을 더해, 큰 모델을 제한된 GPU에서 효율적으로 파인튜닝할 수 있도록 지원합니다. RAG 실습을 위한 벡터 검색(faiss-cpu)과 한국어·다국어 모델 토크나이저(sentencepiece), 일부 모델 attention 연산에 필요한 einops도 포함되어 있습니다.

모델 파일은 이미지에 포함하지 않으며, 실행 시 Hugging Face Hub에서 내려받아 `/workspace/.cache/huggingface`(베이스의 `HF_HOME`)에 저장됩니다. LLM은 VRAM 사용량이 크므로 Tier2 환경 사용을 권장합니다.

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