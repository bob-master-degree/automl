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

| Сервис     | URL                                            | Логин / Пароль |
|------------|------------------------------------------------|----------------|
| Airflow    | [http://localhost:8080](http://localhost:8080) | admin / admin  |
| MLflow     | [http://localhost:5000](http://localhost:5000) | —              |
| Prometheus | [http://localhost:9090](http://localhost:9090) | —              |
| Grafana    | [http://localhost:3000](http://localhost:3000) | admin / admin  |
