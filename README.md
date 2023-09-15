# Currency_converter

Сервис "Конвертер валют" который работает по REST-API.

### Технологии 
- Python
- Django
- Django REST Framework
- Docker
- requests, bs4
- swagger

### Как развернуть проект

- Склонировать репозиторий
```commandline
git clone https://github.com/mishatar/currency_converter.git
```
- Для работы с проектом необходимо установить Docker и Docker-compose:

```commandline
sudo apt install docker.io 
```

- Создать и запустить контейнеры Docker, выполнить команду (версии команд "docker compose" или "docker-compose" отличаются в зависимости от установленной версии Docker Compose):
```
    docker compose up -d --build
```

 - Все готово. Пример get запроса: /api/rates?from=USD&to=RUB&value=1