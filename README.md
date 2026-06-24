# gcube-edu-templates

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

AWS ECR이 GitHub Container Registry보다 다운로드 속도가 빠르기 때문에 사용을 권장합니다.

| # | 이미지 | AWS ECR (권장) | GitHub Container Registry |
|---|---|---|---|
| 1 | edu-dl-tensorflow | `public.ecr.aws/g3x5o1w3/gcube/edu/dl-tensorflow:latest` | `ghcr.io/data-alliance/edu-dl-tensorflow:latest` |
| 2 | edu-cv-pytorch | `public.ecr.aws/g3x5o1w3/gcube/edu/cv-pytorch:latest` | `ghcr.io/data-alliance/edu-cv-pytorch:latest` |
| 3 | edu-ml-data | `public.ecr.aws/g3x5o1w3/gcube/edu/ml-data:latest` | `ghcr.io/data-alliance/edu-ml-data:latest` |
| 4 | edu-nlp-hf | `public.ecr.aws/g3x5o1w3/gcube/edu/nlp-hf:latest` | `ghcr.io/data-alliance/edu-nlp-hf:latest` |
| 5 | edu-rl-pytorch | `public.ecr.aws/g3x5o1w3/gcube/edu/rl-pytorch:latest` | `ghcr.io/data-alliance/edu-rl-pytorch:latest` |
| 6 | edu-genai-sd | `public.ecr.aws/g3x5o1w3/gcube/edu/genai-sd:latest` | `ghcr.io/data-alliance/edu-genai-sd:latest` |
| 7 | edu-llm-train | `public.ecr.aws/g3x5o1w3/gcube/edu/llm-train:latest` | `ghcr.io/data-alliance/edu-llm-train:latest` |
| 8 | edu-audio-pytorch | `public.ecr.aws/g3x5o1w3/gcube/edu/audio-pytorch:latest` | `ghcr.io/data-alliance/edu-audio-pytorch:latest` |
| 9 | edu-medical-monai | `public.ecr.aws/g3x5o1w3/gcube/edu/medical-monai:latest` | `ghcr.io/data-alliance/edu-medical-monai:latest` |
| 10 | edu-geo-gdal | `public.ecr.aws/g3x5o1w3/gcube/edu/geo-gdal:latest` | `ghcr.io/data-alliance/edu-geo-gdal:latest` |
| 11 | edu-gnn-pyg | `public.ecr.aws/g3x5o1w3/gcube/edu/gnn-pyg:latest` | `ghcr.io/data-alliance/edu-gnn-pyg:latest` |

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