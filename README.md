# Пульт охраны банка

Это внутренний репозиторий для сотрудников банка «Сияние». Если вы попали в этот репозиторий случайно, то не сможете его запустить, т.к. у вас нет доступа к БД, но можете свободно использовать код вёрстки или посмотреть как реализованы запросы к БД.

Пульт охраны — это сайт, который можно подключить к удалённой базе данных с визитами и карточками пропуска сотрудников нашего банка.

### Как установить

Запросите доступ к БД у менеджера вашего банка. Для доступа вам понадобятся хост, порт, название базы данных, ключ доступа, имя и пароль пользователя. Переменная `DEBUG` отвечает за режим работы `django`, по окончании разработки должна быть установлена в `False`. Сохраните эти данные в файле `.env` в корневой папке проекта.

```bash
DB_HOST=my.host.add.ress
DB_PORT=port_number
DB_NAME=db_name
DB_USER=login
DB_PASSWORD=password
DB_SECRET_KEY=REPLACE_ME
DEBUG=False
```

Python3 должен быть уже установлен.
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:

```bash
$ pip install -r requirements.txt
```

### Использование

Запустите сайт.

```bash
$ python manage.py runserver 0.0.0.0:8000
```

Наберите в браузере адрес `http://0.0.0.0:8000/`, сайт готов к использованию.

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
