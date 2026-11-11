# edu-genai-sd

**English** | [한국어](README.ko.md)

Stable Diffusion-based image for generative AI courses. It adds JupyterLab and image generation lab packages on top of the `gcube-pytorch` base image. Use it for courses on image generation and LoRA/DreamBooth fine-tuning.

## Contents

| Item | Value |
|---|---|
| Base | `gcube-pytorch-2.11-cuda13.0` (includes PyTorch) |
| Base (CUDA 12.8) | `gcube-pytorch-2.11-cuda12.8` (same contents as above) |
| Working directory | `/workspace` |
| Port | 8888 |

## Usage

Use these settings when deploying a gcube workload.

| Item | Value |
|---|---|
| Image | `ghcr.io/data-alliance/edu-genai-sd:torch2.11-cuda13.0` (same as `latest`) |
| Image (CUDA 12.8) | `ghcr.io/data-alliance/edu-genai-sd:torch2.11-cuda12.8` |
| Image (Docker Hub) | `gcubeai/edu-genai-sd:torch2.11-cuda13.0` (same as `latest`) |
| Image (Docker Hub, CUDA 12.8) | `gcubeai/edu-genai-sd:torch2.11-cuda12.8` |
| Port | 8888 |
| GPU | 16 GB+ VRAM |

After deployment, open the service URL to access JupyterLab.

Pick the image that matches the node's NVIDIA driver. CUDA 13.0 images need driver 580 or later; CUDA 12.8 images need driver 570 or later.

## Installed packages

Package versions are pinned in this folder's `requirements.txt`. The snapshot date and versions for each tag are listed below.

### `torch2.11-cuda13.0`

**As of:** 2026-11-10

The versions below are a snapshot of this image. Run `pip show <package>` in the container terminal to check the installed version.

<!-- VERSIONS:torch2.11-cuda13.0:START -->
| Package | Version |
|---|---|
| diffusers | 0.38.0 |
| transformers | 5.12.1 |
| accelerate | 1.14.0 |
| safetensors | 0.8.0 |
| datasets | 5.0.0 |
| opencv-python-headless | 4.13.0.92 |
| Pillow | 12.1.1 |
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
| diffusers | 0.38.0 |
| transformers | 5.12.1 |
| accelerate | 1.14.0 |
| safetensors | 0.8.0 |
| datasets | 5.0.0 |
| opencv-python-headless | 4.13.0.92 |
| Pillow | 12.1.1 |
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