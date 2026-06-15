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

베이스 이미지(`gcube-pytorch`)가 먼저 빌드되어 있어야 합니다.