ARG BASE_IMAGE
FROM ${BASE_IMAGE}

ENV PIP_BREAK_SYSTEM_PACKAGES=1

RUN pip install --no-cache-dir \
        jupyterlab \
        ipykernel \
        numpy \
        pandas \
        scipy \
        matplotlib \
        seaborn \
        scikit-learn \
        statsmodels \
        plotly \
        openpyxl \
        tqdm

EXPOSE 8888
CMD ["sh", "-c", "exec jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root --ServerApp.token=\"${JUPYTER_TOKEN:-}\" --ServerApp.root_dir=/workspace"]