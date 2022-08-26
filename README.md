# Учебный проект API yatube

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
- [Почта](mr.drodel@gmail.com)
