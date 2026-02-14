FROM ghcr.io/mlflow/mlflow:v2.8.1

RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/* \
    && pip install psycopg2-binary boto3

CMD ["mlflow", "server", \
     "--host", "0.0.0.0", \
     "--backend-store-uri", "/mlflow/mlruns", \
     "--default-artifact-root", "/mlflow/artifacts"]
