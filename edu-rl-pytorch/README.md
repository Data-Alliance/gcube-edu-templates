# edu-rl-pytorch

PyTorch 기반 강화학습 교육용 이미지. `gcube-pytorch` 베이스에 JupyterLab과 강화학습 표준 패키지를 포함합니다. DQN, PPO, A2C 등 강화학습 알고리즘 실습 수업에 사용합니다.

## 구성

| 항목 | 내용 |
|---|---|
| 기반 | `gcube-pytorch-<torch>-cuda<cuda>` (torch 포함) |
| 패키지 | JupyterLab, ipykernel, Gymnasium, Stable-Baselines3, TensorBoard, Matplotlib, NumPy, tqdm |
| 작업 디렉터리 | `/workspace` |
| 포트 | 8888 |

```
ghcr.io/<owner>/edu-rl-pytorch:latest
```

강화학습 실습의 표준 조합인 Gymnasium(환경)과 Stable-Baselines3(PyTorch 기반 RL 알고리즘)에 학습 모니터링용 TensorBoard와 결과 시각화용 Matplotlib을 더해, 에이전트 학습부터 평가까지 강화학습 수업 흐름 전체를 지원합니다. Gymnasium의 classic-control(CartPole, Pendulum 등) 환경이 기본 포함되어 별도 설치 없이 바로 실습할 수 있습니다.

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