# gcube-edu-templates

**English** | [한국어](README.ko.md)

Educational container image templates for the gcube GPU platform. Each image comes with the packages needed for a type of university GPU lab course, so you can start working in JupyterLab as soon as the workload is deployed.

## Templates

| Image | Course topic | Recommended GPU |
|---|---|---|
| `edu-dl-tensorflow` | Deep learning with TensorFlow/Keras | 8 GB+ VRAM |
| `edu-cv-pytorch` | CNNs, transfer learning, computer vision | 8 GB+ VRAM |
| `edu-ml-data` | Intro to ML, data analysis | 8 GB+ VRAM |
| `edu-nlp-hf` | NLP, Transformers, intro to LLMs | 8 GB+ VRAM |
| `edu-rl-pytorch` | Reinforcement learning | 8 GB+ VRAM |
| `edu-genai-sd` | Stable Diffusion, image generation | 16 GB+ VRAM |
| `edu-llm-train` | LLM fine-tuning, RAG | 16 GB+ VRAM |
| `edu-audio-pytorch` | Speech recognition, audio processing | 8 GB+ VRAM |
| `edu-medical-monai` | Medical image analysis | 8 GB+ VRAM |
| `edu-geo-gdal` | Remote sensing, satellite imagery | 8 GB+ VRAM |
| `edu-gnn-pyg` | Graph neural networks (GNN) | 8 GB+ VRAM |

See the README in each template folder for details.

## Usage

When deploying a gcube workload, just set the image address. All images expose port `8888` (JupyterLab starts automatically) and use `/workspace` as the working directory.

**GitHub Container Registry**

| # | Image | Address | Address (CUDA 12.8) |
|---|---|---|---|
| 1 | edu-dl-tensorflow | `ghcr.io/data-alliance/edu-dl-tensorflow:tf2.17-cuda12.8` | (same as left) |
| 2 | edu-cv-pytorch | `ghcr.io/data-alliance/edu-cv-pytorch:torch2.11-cuda13.0` | `ghcr.io/data-alliance/edu-cv-pytorch:torch2.11-cuda12.8` |
| 3 | edu-ml-data | `ghcr.io/data-alliance/edu-ml-data:ubuntu24.04-cuda13.0` | `ghcr.io/data-alliance/edu-ml-data:ubuntu24.04-cuda12.8` |
| 4 | edu-nlp-hf | `ghcr.io/data-alliance/edu-nlp-hf:torch2.11-cuda13.0` | `ghcr.io/data-alliance/edu-nlp-hf:torch2.11-cuda12.8` |
| 5 | edu-rl-pytorch | `ghcr.io/data-alliance/edu-rl-pytorch:torch2.11-cuda13.0` | `ghcr.io/data-alliance/edu-rl-pytorch:torch2.11-cuda12.8` |
| 6 | edu-genai-sd | `ghcr.io/data-alliance/edu-genai-sd:torch2.11-cuda13.0` | `ghcr.io/data-alliance/edu-genai-sd:torch2.11-cuda12.8` |
| 7 | edu-llm-train | `ghcr.io/data-alliance/edu-llm-train:torch2.11-cuda13.0` | `ghcr.io/data-alliance/edu-llm-train:torch2.11-cuda12.8` |
| 8 | edu-audio-pytorch | `ghcr.io/data-alliance/edu-audio-pytorch:torch2.11-cuda13.0` | `ghcr.io/data-alliance/edu-audio-pytorch:torch2.11-cuda12.8` |
| 9 | edu-medical-monai | `ghcr.io/data-alliance/edu-medical-monai:torch2.11-cuda13.0` | `ghcr.io/data-alliance/edu-medical-monai:torch2.11-cuda12.8` |
| 10 | edu-geo-gdal | `ghcr.io/data-alliance/edu-geo-gdal:torch2.11-cuda13.0` | `ghcr.io/data-alliance/edu-geo-gdal:torch2.11-cuda12.8` |
| 11 | edu-gnn-pyg | `ghcr.io/data-alliance/edu-gnn-pyg:torch2.11-cuda13.0` | `ghcr.io/data-alliance/edu-gnn-pyg:torch2.11-cuda12.8` |

Pick the address that matches the node's NVIDIA driver. The `Address` column is CUDA 13.0 (driver 580 or later; `edu-dl-tensorflow` is CUDA 12.8) and equals `latest`. Use the `Address (CUDA 12.8)` column on nodes with driver 570 or later. `edu-ml-data` also shows the Ubuntu version in its tags because its base image is provided per Ubuntu version. See each template folder's README for package versions per tag.

**Docker Hub**

The same images are also on Docker Hub [`gcubeai`](https://hub.docker.com/u/gcubeai) with the same names and tags.

| # | Image | Address | Address (CUDA 12.8) |
|---|---|---|---|
| 1 | edu-dl-tensorflow | `gcubeai/edu-dl-tensorflow:tf2.17-cuda12.8` | (same as left) |
| 2 | edu-cv-pytorch | `gcubeai/edu-cv-pytorch:torch2.11-cuda13.0` | `gcubeai/edu-cv-pytorch:torch2.11-cuda12.8` |
| 3 | edu-ml-data | `gcubeai/edu-ml-data:ubuntu24.04-cuda13.0` | `gcubeai/edu-ml-data:ubuntu24.04-cuda12.8` |
| 4 | edu-nlp-hf | `gcubeai/edu-nlp-hf:torch2.11-cuda13.0` | `gcubeai/edu-nlp-hf:torch2.11-cuda12.8` |
| 5 | edu-rl-pytorch | `gcubeai/edu-rl-pytorch:torch2.11-cuda13.0` | `gcubeai/edu-rl-pytorch:torch2.11-cuda12.8` |
| 6 | edu-genai-sd | `gcubeai/edu-genai-sd:torch2.11-cuda13.0` | `gcubeai/edu-genai-sd:torch2.11-cuda12.8` |
| 7 | edu-llm-train | `gcubeai/edu-llm-train:torch2.11-cuda13.0` | `gcubeai/edu-llm-train:torch2.11-cuda12.8` |
| 8 | edu-audio-pytorch | `gcubeai/edu-audio-pytorch:torch2.11-cuda13.0` | `gcubeai/edu-audio-pytorch:torch2.11-cuda12.8` |
| 9 | edu-medical-monai | `gcubeai/edu-medical-monai:torch2.11-cuda13.0` | `gcubeai/edu-medical-monai:torch2.11-cuda12.8` |
| 10 | edu-geo-gdal | `gcubeai/edu-geo-gdal:torch2.11-cuda13.0` | `gcubeai/edu-geo-gdal:torch2.11-cuda12.8` |
| 11 | edu-gnn-pyg | `gcubeai/edu-gnn-pyg:torch2.11-cuda13.0` | `gcubeai/edu-gnn-pyg:torch2.11-cuda12.8` |

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
