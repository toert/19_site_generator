﻿
# Генератор сайтов

Данный скрипт сконвертирует статьи из .md в HTML и сделает из них небольшой статический сайт в папке `pages`. Главная страница с навигацией по всем статьям — `index.html`.
Для возвращения со страницы статьи обратно на `index.html` нажмите HOME в шапке сайта.

## Запуск

Разместите ваши статьи в папке `папка_со_скриптом/articles/имя_темы/название_статьи.md`, затем внесите данные о них в файл config.json(можете выбрать другое название).

Затем введите в терминале:

    python3.5 site_generator.py путь_до_конфига


## Зависимости

Скрипт написан на языке Python 3, поэтому требует его наличия.

• Для обработки параметров в командной строке должен быть установлен модуль argparse.

• Для генерации сайта — шаблонизатор Jinja2

• Для распознавания markdown — модуль markdown

## Поддержка

Если у вас возникли сложности или вопросы по использованию скрипта, напишите на электронную почту 
<pw177@mail.ru> или в скайп toerting.

