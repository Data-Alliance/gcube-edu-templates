# edu-gnn-pyg

PyTorch 기반 그래프 신경망(GNN) 교육용 이미지. `gcube-pytorch` 베이스에 JupyterLab과 PyTorch Geometric(PyG)을 포함합니다. 노드 분류, 링크 예측, 그래프 분류 등 그래프 신경망 수업에 사용합니다.

## 구성

| 항목 | 내용 |
|---|---|
| 기반 | `gcube-pytorch-2.11-cuda13.0` (PyTorch, torchvision, torchaudio 포함) |
| 패키지 | JupyterLab, ipykernel, PyTorch Geometric, NetworkX, scikit-learn, Matplotlib, tqdm |
| 작업 디렉터리 | `/workspace` |
| 포트 | 8888 |

## 사용

gcube 워크로드 배포 시 아래 설정으로 사용합니다.

| 항목 | 값 |
|---|---|
| 이미지 | `chaeyoon08/edu-gnn-pyg:latest` |
| 포트 | 8888 |
| GPU | VRAM 8GB 이상 |

배포 후 서비스 URL로 접속하면 JupyterLab이 열립니다.

PyTorch Geometric 본체는 GCN, GAT, GraphSAGE 등 일반적인 그래프 신경망 실습을 지원합니다. 대규모 그래프 이웃 샘플링 등 일부 고급 기능에 필요한 컴파일 확장(pyg_lib, torch_scatter 등)은 포함하지 않으며, 필요한 경우 PyTorch·CUDA 버전에 맞는 wheel을 추가로 설치합니다.

이미지는 GitHub Container Registry에서도 받을 수 있습니다.

```
ghcr.io/data-alliance/edu-gnn-pyg:latest
chaeyoon08/edu-gnn-pyg:latest
```

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