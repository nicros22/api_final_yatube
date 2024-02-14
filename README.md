# Я.Практикум. Проект «API для Yatube».

## Описание

API для Yatube представляет собой социальную сеть в которой можно публиковать, комментировать записи,
и так же имеет возможность подписки/отписки пользователей.

## Стек технологий

* Python
* Django
* DRF
* JWT
* Djoser

## Запуск проекта

- Клонировать репозиторий и перейти в него в командной строке:

```bash
git clone git@github.com:nicros22/api_final_yatube.git
```

```bash
cd api_final_yatube
```

- Cоздать и активировать виртуальное окружение:

```bash
python -m venv venv
```

```bash
source venv/Scripts/activate
```

```bash
python -m pip install --upgrade pip
```

- Установить зависимости из файла requirements.txt:

```bash
cd yatube_api
```

```bash
pip install -r requirements.txt
```

- Выполнить миграции:

```bash
python manage.py migrate
```

- Запустить проект:

```bash
python manage.py runserver
```

## Примеры работы с API

Для неавторизованных пользователей работа с API доступна только в режиме чтения.

```r
GET api/v1/posts/ - получить список всех публикаций.
При указании параметров limit и offset выдача должна работать с пагинацией
GET api/v1/posts/{id}/ - получение публикации по id
GET api/v1/groups/ - получение списка доступных сообществ
GET api/v1/groups/{id}/ - получение информации о сообществе по id
GET api/v1/{post_id}/comments/ - получение всех комментариев к публикации
GET api/v1/{post_id}/comments/{id}/ - Получение комментария к публикации по id
```
## Остальные примеры работы с API:

Когда вы запустите проект, по адресу http://127.0.0.1:8000/redoc/ будет доступна вся документация для API Yatube. Документация представлена в формате Redoc.

## Автор: 
Никита Пономаренко
