# edu-geo-gdal

PyTorch 기반 지리공간·원격탐사 교육용 이미지. `gcube-pytorch` 베이스에 JupyterLab과 GDAL 기반 지리공간 처리 스택을 포함합니다. 위성영상 분류·분할, 래스터·벡터 데이터 처리, 원격탐사 등 지리공간 수업에 사용합니다.

## 구성

| 항목 | 내용 |
|---|---|
| 기반 | `gcube-pytorch-2.11-cuda13.0` (PyTorch, torchvision, torchaudio 포함) |
| 패키지 | JupyterLab, ipykernel, rasterio, GeoPandas, Shapely, pyproj, scikit-image, Matplotlib, tqdm |
| 작업 디렉터리 | `/workspace` |
| 포트 | 8888 |

## 사용

gcube 워크로드 배포 시 아래 설정으로 사용합니다.

| 항목 | 값 |
|---|---|
| 이미지 | `chaeyoon08/edu-geo-gdal:latest` |
| 포트 | 8888 |
| GPU | VRAM 8GB 이상 |

배포 후 서비스 URL로 접속하면 JupyterLab이 열립니다.

위성영상 분류·분할은 타일 또는 patch 단위로 처리하면 VRAM 8GB 환경에서 학습할 수 있습니다. 대형 영상은 타일로 분할해 사용하는 것을 권장합니다.

rasterio·GeoPandas는 GDAL이 포함된 바이너리 패키지로 설치되어, GeoTIFF·Shapefile 등 일반적인 지리공간 포맷을 별도 시스템 설치 없이 다룰 수 있습니다.

이미지는 GitHub Container Registry에서도 받을 수 있습니다.

```
ghcr.io/data-alliance/edu-geo-gdal:latest
chaeyoon08/edu-geo-gdal:latest
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