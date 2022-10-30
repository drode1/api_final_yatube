# Учебный проект API yatube
Учебный проект по написанию и изучению Django Rest Framework. В рамках него можно делать запросы к API, что позволит публиковать новые посты пользователей, добавлять их в группу, а также, комментировать.

### **Стек**

![python version](https://img.shields.io/badge/Python-3.7-green)
![django version](https://img.shields.io/badge/Django-2.2-green)
![djangorestframework version](https://img.shields.io/badge/DRF-3.12-green)
![simplejwt version](https://img.shields.io/badge/DRFsimplejwt-4.7-green)


### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:drode1/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
. env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

## Список доступных эндпоинтов:

```
- api/v1/posts/ – список всех постов;
- api/v1/groups/ – список всех групп (Admin add only);
- api/v1/{post_id}/comments/ – список комментариев поста;
- api/v1/follows/ – список ваших подписчиков (Auth only);
- api/v1/jwt/ – создание и получение токенов;
```
### Автор проекта

- Егор Ремезов
  - [Telegram](https://t.me/e_remezov)
  - [Почта](mailto:mr.drodel@gmail.com>)
