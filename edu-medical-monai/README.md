# edu-medical-monai

**English** | [한국어](README.ko.md)

PyTorch-based image for medical imaging courses. It adds JupyterLab and the MONAI medical imaging deep learning stack on top of the `gcube-pytorch` base image. Use it for medical imaging courses on classification, organ segmentation, DICOM/NIfTI processing, and more.

## Contents

| Item | Value |
|---|---|
| Base | `gcube-pytorch-2.11-cuda13.0` (includes PyTorch, torchvision, torchaudio) |
| Base (CUDA 12.8) | `gcube-pytorch-2.11-cuda12.8` (same contents as above) |
| Working directory | `/workspace` |
| Port | 8888 |

## Usage

Use these settings when deploying a gcube workload.

| Item | Value |
|---|---|
| Image | `ghcr.io/data-alliance/edu-medical-monai:torch2.11-cuda13.0` (same as `latest`) |
| Image (CUDA 12.8) | `ghcr.io/data-alliance/edu-medical-monai:torch2.11-cuda12.8` |
| Image (Docker Hub) | `gcubeai/edu-medical-monai:torch2.11-cuda13.0` (same as `latest`) |
| Image (Docker Hub, CUDA 12.8) | `gcubeai/edu-medical-monai:torch2.11-cuda12.8` |
| Port | 8888 |
| GPU | 8 GB+ VRAM |

After deployment, open the service URL to access JupyterLab.

Pick the image that matches the node's NVIDIA driver. CUDA 13.0 images need driver 580 or later; CUDA 12.8 images need driver 570 or later.

2D medical image classification/segmentation can be trained with 8 GB of VRAM. 3D CT/MRI volume segmentation needs more GPU memory; reduce the patch size and use mixed precision (AMP) to control memory use.

## Installed packages

Package versions are pinned in this folder's `requirements.txt`. The snapshot date and versions for each tag are listed below.

### `torch2.11-cuda13.0`

**As of:** 2026-11-10

The versions below are a snapshot of this image. Run `pip show <package>` in the container terminal to check the installed version.

<!-- VERSIONS:torch2.11-cuda13.0:START -->
| Package | Version |
|---|---|
| MONAI | 1.6.0 |
| NiBabel | 5.4.2 |
| pydicom | 3.0.2 |
| SimpleITK | 2.5.5 |
| scikit-image | 0.26.0 |
| Matplotlib | 3.11.0 |
| tqdm | 4.68.3 |
| ipywidgets | 8.1.8 |
<!-- VERSIONS:torch2.11-cuda13.0:END -->

### `torch2.11-cuda12.8`

**As of:** 2026-11-10

The versions below are a snapshot of this image. Run `pip show <package>` in the container terminal to check the installed version.

<!-- VERSIONS:torch2.11-cuda12.8:START -->
| Package | Version |
|---|---|
| MONAI | 1.6.0 |
| NiBabel | 5.4.2 |
| pydicom | 3.0.2 |
| SimpleITK | 2.5.5 |
| scikit-image | 0.26.0 |
| Matplotlib | 3.11.0 |
| tqdm | 4.68.3 |
| ipywidgets | 8.1.8 |
<!-- VERSIONS:torch2.11-cuda12.8:END -->

## Environment variables

All environment variables are optional. Set them only to use a private repository or to set the commit author.

| Variable | Default | Description |
|---|---|---|
| `JUPYTER_TOKEN` | (none) | JupyterLab access token. If unset, JupyterLab opens without a token |
| `GIT_CLONE_REPO` | (none) | Repository URL to clone into `/workspace` when the workload starts. Retries for up to 1 minute on failure, for nodes whose network comes up late |
| `GIT_USER_NAME` | (none) | Git commit author name |
| `GIT_USER_EMAIL` | (none) | Git commit author email |
| `GIT_TOKEN` | (none) | Git access token (PAT). Needed to clone/push private repositories |
| `GIT_HOST` | `github.com` | Git host. GitLab (`gitlab.com`) or an internal git server also works |