# edu-ml-data

**English** | [한국어](README.ko.md)

Image for intro machine learning and data analysis courses. It adds JupyterLab and data analysis/ML lab packages on top of the `gcube-ubuntu` base image. Use it for courses on data preprocessing, visualization, and basic ML algorithms.

## Contents

| Item | Value |
|---|---|
| Base | `gcube-ubuntu24.04-cuda13.0` (CUDA environment) |
| Base (CUDA 12.8) | `gcube-ubuntu24.04-cuda12.8` (same contents as above) |
| Working directory | `/workspace` |
| Port | 8888 |

## Usage

Use these settings when deploying a gcube workload.

| Item | Value |
|---|---|
| Image | `ghcr.io/data-alliance/edu-ml-data:ubuntu24.04-cuda13.0` (same as `latest`) |
| Image (CUDA 12.8) | `ghcr.io/data-alliance/edu-ml-data:ubuntu24.04-cuda12.8` |
| Image (Docker Hub) | `gcubeai/edu-ml-data:ubuntu24.04-cuda13.0` (same as `latest`) |
| Image (Docker Hub, CUDA 12.8) | `gcubeai/edu-ml-data:ubuntu24.04-cuda12.8` |
| Port | 8888 |
| GPU | 8 GB+ VRAM |

After deployment, open the service URL to access JupyterLab.

Pick the image that matches the node's NVIDIA driver. CUDA 13.0 images need driver 580 or later; CUDA 12.8 images need driver 570 or later.

This is the only image whose tags include the Ubuntu version. The PyTorch and TensorFlow base images each have a fixed Ubuntu version, but this image's base (`gcube-ubuntu`) is provided per Ubuntu version. Currently only Ubuntu 24.04 is provided.

## Installed packages

Package versions are pinned in this folder's `requirements.txt`. The snapshot date and versions for each tag are listed below.

### `ubuntu24.04-cuda13.0`

**As of:** 2026-11-10

The versions below are a snapshot of this image. Run `pip show <package>` in the container terminal to check the installed version.

<!-- VERSIONS:ubuntu24.04-cuda13.0:START -->
| Package | Version |
|---|---|
| NumPy | 2.5.0 |
| pandas | 3.0.3 |
| scikit-learn | 1.9.0 |
| SciPy | 1.18.0 |
| statsmodels | 0.14.6 |
| Matplotlib | 3.11.0 |
| seaborn | 0.13.2 |
| Plotly | 6.8.0 |
| openpyxl | 3.1.5 |
| tqdm | 4.68.3 |
| ipywidgets | 8.1.8 |
<!-- VERSIONS:ubuntu24.04-cuda13.0:END -->

### `ubuntu24.04-cuda12.8`

**As of:** 2026-11-10

The versions below are a snapshot of this image. Run `pip show <package>` in the container terminal to check the installed version.

<!-- VERSIONS:ubuntu24.04-cuda12.8:START -->
| Package | Version |
|---|---|
| NumPy | 2.5.0 |
| pandas | 3.0.3 |
| scikit-learn | 1.9.0 |
| SciPy | 1.18.0 |
| statsmodels | 0.14.6 |
| Matplotlib | 3.11.0 |
| seaborn | 0.13.2 |
| Plotly | 6.8.0 |
| openpyxl | 3.1.5 |
| tqdm | 4.68.3 |
| ipywidgets | 8.1.8 |
<!-- VERSIONS:ubuntu24.04-cuda12.8:END -->

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