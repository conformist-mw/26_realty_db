# Real Estate Site
Данный проект представляет собой доску объявлений. Доступен поиск по региону, цене и дате застройки здания. 

Были реализованы следующие функции:
- подключена реляционная СУБД
- создан скрипт загрузки данных из json, обновления (если объявления появилось - ещё раз — помечается активным)
- подключена фильтрация объявлений по цене, городу
- подключена пагинация объявлений

## Установка
Для использования требуется установить зависимости, например так:
```
pip3 install -r requirements.txt
```

## Для создания БД перед первым запуском выполнить:
```python
from server import db, create_app
db.create_all(app=create_app())
```

## Запуск
Для запуска выполняем:
```
python3 server.py
```
переходим по [ссылке](http://localhost:5000), готово.

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)