# Инфраструктура для работы с Airflow

Перейдем в директорию с конфигурацией для деплоя:

```bash
cd deploy
```

Создадим базовые директории для Airflow:

```bash
mkdir -p content/dags content/logs content/plugins content/config
```

Создадим дополнительную директорию для скриптов:

```bash
mkdir -p content/scripts
```

Скопируем пример файла окружения для Kaggle:

```bash
cp .kaggle.env.example .kaggle.env
```

> ⚠️ Для доступа к Kaggle необходимо получить API ключ в настройках и внести его в `.kaggle.env`.

Запустим инфраструктуру через Docker Compose:

```bash
docker-compose up -d
```

Доступ к сервисам:

* **Airflow**: [http://localhost:8080](http://localhost:8080)
  *login: admin / password: admin*

* **MLflow**: [http://localhost:5000](http://localhost:5000)

* **Prometheus**: [http://localhost:9090](http://localhost:9090)

* **Grafana**: [http://localhost:3000](http://localhost:3000)
  *login: admin / password: admin*
