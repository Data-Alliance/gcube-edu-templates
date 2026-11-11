# edu-dl-tensorflow

**English** | [한국어](README.ko.md)

TensorFlow/Keras-based image for deep learning courses. It adds JupyterLab and machine learning lab packages on top of the `gcube-tensorflow` base image. Use it for TensorFlow-based deep learning courses such as CNNs and transfer learning.

## Contents

| Item | Value |
|---|---|
| Base | `gcube-tensorflow-2.17-cuda12.8` (includes TensorFlow 2.17) |
| Working directory | `/workspace` |
| Port | 8888 |

## Usage

Use these settings when deploying a gcube workload.

| Item | Value |
|---|---|
| Image | `ghcr.io/data-alliance/edu-dl-tensorflow:tf2.17-cuda12.8` (same as `latest`) |
| Image (Docker Hub) | `gcubeai/edu-dl-tensorflow:tf2.17-cuda12.8` (same as `latest`) |
| Port | 8888 |
| GPU | 8 GB+ VRAM |

After deployment, open the service URL to access JupyterLab.

This image is based on CUDA 12.8 and needs NVIDIA driver 570 or later.

## Installed packages

Package versions are pinned in this folder's `requirements.txt`. The snapshot date and versions for each tag are listed below.

### `tf2.17-cuda12.8`

**As of:** 2026-11-10

The versions below are a snapshot of this image. Run `pip show <package>` in the container terminal to check the installed version.

<!-- VERSIONS:tf2.17-cuda12.8:START -->
| Package | Version |
|---|---|
| TensorFlow | 2.17.0+nv25.2 |
| ipywidgets | 8.1.8 |
| scikit-learn | 1.5.2 |
| SciPy | 1.12.0 |
| Pillow | 12.2.0 |
| Matplotlib | 3.11.0 |
| NumPy | 1.26.4 |
| tqdm | 4.67.1 |
<!-- VERSIONS:tf2.17-cuda12.8:END -->

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