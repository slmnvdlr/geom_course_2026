# Настройка рабочего пространства

## Рекомендуемый вариант

- Python 3.11 или 3.12;
- Git;
- VS Code с расширениями Python и Jupyter либо PyCharm/JupyterLab;
- отдельное виртуальное окружение `.venv` внутри проекта.

Не рекомендуется устанавливать библиотеки курса в системный Python.

## Установка через `venv`

```text
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r environment/requirements-core.txt
python homeworks/hw00/hello.py
```

Для практикума по интерактивной графике:

```text
python -m pip install -r environment/requirements-dash.txt
```

## Альтернатива через Conda

```text
conda env create -f environment/environment.yml
conda activate scientific-graphics
python homeworks/hw00/hello.py
```

Выберите один способ управления окружением и придерживайтесь его весь семестр.

## Отдельные программы

ParaView и Inkscape устанавливаются до соответствующих практикумов. Их лучше не включать в первую пару: установка тяжёлая и может занять всё занятие. Преподаватель заранее публикует проверенные ссылки и версии, а на практикумах 7 и 8 проводится только короткая проверка запуска.

## Что приложить к первому чекпоинту

- вывод `python --version`;
- вывод `python -m pip --version`;
- результат запуска `homeworks/hw00/hello.py`;
- первый коммит в Git;
- короткий `README` с выбранным набором данных или пометкой «набор ещё выбирается».
