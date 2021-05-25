# API YamDb_Final
Проект YaMDb собирает отзывы пользователей на произведения. Произведения делятся на категории: «Книги», «Фильмы», «Музыка». Произведению может быть присвоен жанр из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»). Новые жанры может создавать только администратор. Благодарные или возмущённые читатели оставляют к произведениям текстовые отзывы и выставляют произведению рейтинг (оценку в диапазоне от одного до десяти). Из множества оценок автоматически высчитывается средняя оценка произведения.

# Стек технологий
Автоматизация и тестирование:
- github actions, pytest
Сборка и хранение:
- docker, docker-compose, docker-hub
Хостинг:
- Яндекс Облако
Оповещение:
- Telegram API
Контейнеры:
1. Web:
    - Python + Django REST Framework
    - Simple JWT - работа с токеном
    - Django-filter - фильтрация запросов
    - Git - система контроля версий
2. Nginx
3. Postgresql

# Установка
1. Клонирйте репозиторий с проектом
```sh
git clone https://github.com/ne4istii/yamdb_final.git
```
2. Подготовить удаленный сервер для работы:
- Установите docker:
```sh
sudo apt install docker.io 
```
- Установите [docker-compose](https://docs.docker.com/compose/install/):
```sh
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```
- Скопируйте подготовленные файлы docker-compose.yaml и nginx/default.conf из вашего проекта на сервер в home/<ваш_username>/docker-compose.yaml и home/<ваш_username>/nginx/default.conf соответственно.
- Добавьте в Secrets GitHub Actions переменные окружения
3. При пуше в ветку main код автоматически деплоится на сервер

# Доступ к проекту
- Полная документация проекта (redoc.yaml) доступна по адресу: http://84.252.137.223/redoc/
- Доступ в админку проекта: http://84.252.137.223/admin/
- Автор: [ne4istii](https://github.com/ne4istii)

![yamdb_workflow Actions Status](https://github.com/ne4istii/yamdb_final/actions/workflows/yamdb_workflow.yaml/badge.svg)
