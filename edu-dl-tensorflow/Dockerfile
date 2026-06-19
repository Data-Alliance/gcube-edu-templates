ARG BASE_IMAGE
FROM ${BASE_IMAGE}

ENV PIP_BREAK_SYSTEM_PACKAGES=1

RUN pip install --no-cache-dir \
        jupyterlab \
        ipywidgets \
        scipy \
        scikit-learn \
        matplotlib \
        pillow \
        tqdm \
        "numpy<2"

RUN rm -rf ~/.cache/matplotlib && python -c "import matplotlib.font_manager"

ENV JUPYTERLAB_DIR=/usr/local/lib/python3.12/dist-packages/jupyterlab

EXPOSE 8888
CMD ["sh", "-c", "exec jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root --ServerApp.token=\"${JUPYTER_TOKEN:-}\" --ServerApp.root_dir=/workspace"]