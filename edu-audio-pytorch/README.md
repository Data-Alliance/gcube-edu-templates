# edu-audio-pytorch

PyTorch 기반 음성·오디오 교육용 이미지. `gcube-pytorch` 베이스에 JupyterLab과 음성·오디오 처리 패키지를 포함합니다. 음성인식, 오디오 분류, 사운드 특징 추출 등 음성·오디오 수업에 사용합니다.

## 구성

| 항목 | 내용 |
|---|---|
| 기반 | `gcube-pytorch-2.11-cuda13.0` (PyTorch, torchvision, torchaudio 포함) |
| 기반 (CUDA 12.8) | `gcube-pytorch-2.11-cuda12.8` (위와 동일 구성) |
| 시스템 | FFmpeg (오디오 디코딩·Whisper 백엔드) |
| 작업 디렉터리 | `/workspace` |
| 포트 | 8888 |

## 사용

gcube 워크로드 배포 시 아래 설정으로 사용합니다.

| 항목 | 값 |
|---|---|
| 이미지 | `ghcr.io/data-alliance/edu-audio-pytorch:torch2.11-cuda13.0` (`latest`와 동일) |
| 이미지 (CUDA 12.8) | `ghcr.io/data-alliance/edu-audio-pytorch:torch2.11-cuda12.8` |
| 이미지 (Docker Hub) | `gcubeai/edu-audio-pytorch:<위와 같은 태그>` |
| 포트 | 8888 |
| GPU | VRAM 8GB 이상 |

배포 후 서비스 URL로 접속하면 JupyterLab이 열립니다.

노드의 NVIDIA 드라이버 버전에 맞는 이미지를 사용합니다. CUDA 13.0 이미지는 드라이버 580 이상, CUDA 12.8 이미지는 드라이버 570 이상이 필요합니다.

Whisper는 모델 크기별로 GPU 메모리 요구가 다릅니다. VRAM 8GB 환경에서는 medium 이하 모델을 권장합니다.

## 포함 환경

패키지 버전은 이 폴더의 `requirements.txt`로 고정되어 있습니다. 태그별 기준일과 버전은 아래와 같습니다.

### `torch2.11-cuda13.0`

**기준일:** 2026-11-10

아래 버전은 해당 이미지 기준 스냅샷입니다. 컨테이너 터미널에서 `pip show <패키지>`로 현재 설치된 버전을 확인할 수 있습니다.

<!-- VERSIONS:torch2.11-cuda13.0:START -->
| 패키지 | 버전 |
|---|---|
| torchaudio | 2.11.0+cu130 |
| librosa | 0.11.0 |
| soundfile | 0.14.0 |
| openai-whisper | 20250625 |
| Matplotlib | 3.11.0 |
| tqdm | 4.68.3 |
| ipywidgets | 8.1.8 |
<!-- VERSIONS:torch2.11-cuda13.0:END -->

### `torch2.11-cuda12.8`

**기준일:** 2026-11-10

아래 버전은 해당 이미지 기준 스냅샷입니다. 컨테이너 터미널에서 `pip show <패키지>`로 현재 설치된 버전을 확인할 수 있습니다.

<!-- VERSIONS:torch2.11-cuda12.8:START -->
| 패키지 | 버전 |
|---|---|
| torchaudio | 2.11.0+cu128 |
| librosa | 0.11.0 |
| soundfile | 0.14.0 |
| openai-whisper | 20250625 |
| Matplotlib | 3.11.0 |
| tqdm | 4.68.3 |
| ipywidgets | 8.1.8 |
<!-- VERSIONS:torch2.11-cuda12.8:END -->

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