# Лабораторная работа № 2 — Создание web-страницы с текстом

В архиве уже есть папка `lab2`. После распаковки не нужно создавать её вручную.

## Структура

- `firstwebpage/` — Django-проект.
- `firstwebpage/flatpages/templates/index.html` — базовая зелёная страница: 4 столбца и 5 строк данных.
- `firstwebpage/flatpages/templates/table_stage.html` — сохранённый промежуточный этап: таблица расширена до 6 столбцов и 7 строк данных, есть границы и заголовки списков уровня `h4`.
- `firstwebpage/flatpages/templates/static_handler.html` — шаблон последующего этапа на основе `table_stage.html`, с подключённым CSS и изображением.
- `firstwebpage/flatpages/static/index.css` — стили задания про статические файлы.
- `firstwebpage/flatpages/static/finance_chart.svg` — локальное изображение.

## Все этапы доступны в одном проекте

| URL | Что показывает |
|---|---|
| `/stage1/` | Начальный этап: простой текст `Привет, Мир!`, явно задан `text/plain` |
| `/hello/` | Тот же текст, явно задан `text/plain` |
| `/hello-plain/` | Тот же текст без `content_type`, Django применяет тип по умолчанию |
| `/` | Базовый зелёный `index.html`, 4 столбца и 5 строк данных |
| `/table-stage/` | Промежуточный этап таблицы: 6 столбцов, 7 строк данных, границы и заголовки `h4` |
| `/static-handler/` | Итоговый стилизованный `static_handler.html`, 6 столбцов, 7 строк данных, CSS и изображение 30 px |

Начальный ответ по корневому URL `/` сохранён на `/stage1/`, потому что по методичке позже тот же `home` изменяется на рендеринг HTML-шаблона. Один URL не может одновременно возвращать и простой текст, и HTML-страницу в итоговом запуске, поэтому ранний этап выделен в отдельный маршрут.

## Запуск в Windows PowerShell

1. Распакуй архив. Внутри уже будет папка `lab2`.
2. Открой PowerShell в папке `lab2`, рядом с `README.md` и `requirements.txt`.
3. Выполни команды:

```powershell
python -m pip install -r requirements.txt
cd firstwebpage
python manage.py migrate
python manage.py check
python manage.py test flatpages
python manage.py runserver
```

4. Перейди в браузере по адресам из таблицы выше.

## Проверки

Автоматические тесты проверяют сохранённый текстовый этап, оба варианта `HttpResponse`, базовый шаблон 4×5, промежуточную таблицу 6×7 и финальный `static_handler.html`.
