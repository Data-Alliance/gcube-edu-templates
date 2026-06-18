ARG BASE_IMAGE
FROM ${BASE_IMAGE}

ENV PIP_BREAK_SYSTEM_PACKAGES=1
ENV JUPYTERLAB_DIR=/usr/local/lib/python3.12/dist-packages/jupyterlab

RUN pip install --no-cache-dir \
        jupyterlab \
        ipykernel \
        monai \
        nibabel \
        pydicom \
        SimpleITK \
        scikit-image \
        matplotlib \
        tqdm

RUN rm -rf ~/.cache/matplotlib && python -c "import matplotlib.font_manager"

EXPOSE 8888
CMD ["sh", "-c", "exec jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root --ServerApp.token=\"${JUPYTER_TOKEN:-}\" --ServerApp.root_dir=/workspace"]