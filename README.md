# Инфраструктура для работы с Airflow

Перейдем в директорию с конфигурацией для деплоя:

```bash
cd deploy
```

## Создание необходимых директорий

Для работы Airflow создадим базовые папки:

```bash
mkdir -p content/dags content/logs content/plugins content/config
```

Создадим отдельную директорию для скриптов:

```bash
mkdir -p content/scripts
```

## Настройка окружения для Kaggle

Скопируем пример файла окружения:

```bash
cp .kaggle.env.example .kaggle.env
```

> ⚠️ Для доступа к Kaggle необходимо получить API ключ в настройках и добавить его в `.kaggle.env`.

## Запуск инфраструктуры

Поднимаем сервисы через Docker Compose:

```bash
docker-compose up -d
```

## Доступ к сервисам

| Сервис     | URL                                                        | Логин / Пароль |
|------------|------------------------------------------------------------|----------------|
| Airflow    | [http://airflow.localhost](http://airflow.localhost)       | admin / admin  |
| MLflow     | [http://mlflow.localhost](http://mlflow.localhost)         | —              |
| Prometheus | [http://prometheus.localhost](http://prometheus.localhost) | —              |
| Grafana    | [http://grafana.localhost](http://grafana.localhost)       | admin / admin  |

## Разработка

### Dags

Все `DAG`-файлы для `Airflow` необходимо помещать в директорию `content/dags`.

`Airflow` будет автоматически их подхватывать и отображать в интерфейсе.
