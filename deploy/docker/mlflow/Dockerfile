FROM ghcr.io/mlflow/mlflow:v3.8.1

ARG AIRFLOW_UID
ARG AIRFLOW_GID=0

RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/* \
    && pip install psycopg2-binary boto3

RUN mkdir -p /mlflow && \
    chown -R ${AIRFLOW_UID}:${AIRFLOW_GID} /mlflow/

CMD ["mlflow", "server", \
     "--host", "0.0.0.0", \
     "--backend-store-uri", "/mlflow/mlruns", \
     "--default-artifact-root", "/mlflow/artifacts"]
