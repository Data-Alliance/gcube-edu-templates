ARG BASE_IMAGE
FROM ${BASE_IMAGE}

ENV PIP_BREAK_SYSTEM_PACKAGES=1
ENV JUPYTERLAB_DIR=/usr/local/lib/python3.12/dist-packages/jupyterlab

# Pin the torch stack shipped by the base image so later pip installs
# (here or by users in notebooks) can't swap it for a different CUDA build.
RUN pip freeze | grep -E '^(torch|torchvision|torchaudio|triton)==' > /etc/pip-constraints.txt \
    && test -s /etc/pip-constraints.txt && cat /etc/pip-constraints.txt
ENV PIP_CONSTRAINT=/etc/pip-constraints.txt

# Package versions are pinned in requirements.txt (see the comment at its top).
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

RUN rm -rf ~/.cache/matplotlib && python -c "import matplotlib.font_manager"

EXPOSE 8888
CMD ["sh", "-c", "exec jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root --ServerApp.token=\"${JUPYTER_TOKEN:-}\" --ServerApp.root_dir=/workspace"]