# ДЗ №0. Настройка рабочего пространства и первая работа с Git

**Темы:** Git, Python, виртуальное окружение, зависимости.

## Цель

Подготовить рабочее пространство для курса и проверить, что Python и основные библиотеки установлены корректно.

## Задание

1. Получите собственную копию репозитория курса способом, указанным преподавателем.
2. Клонируйте свой репозиторий на компьютер.
3. В корне проекта создайте виртуальное окружение `.venv`:

   ```text
   python -m venv .venv
   ```

4. Активируйте окружение.

   Windows PowerShell:

   ```text
   .\.venv\Scripts\Activate.ps1
   ```

   macOS/Linux:

   ```text
   source .venv/bin/activate
   ```

5. Установите NumPy, Pandas и Matplotlib:

   ```text
   python -m pip install --upgrade pip
   python -m pip install numpy pandas matplotlib
   ```

6. В папке `homeworks/hw00` создайте файл `hello.py`.
7. Программа должна вывести:

   - версию Python;
   - версию NumPy;
   - версию Pandas;
   - версию Matplotlib.

8. В корне репозитория создайте файл `requirements.txt`:

   ```text
   python -m pip freeze > requirements.txt
   ```

9. Запустите программу из корня репозитория:

   ```text
   python homeworks/hw00/hello.py
   ```

10. Добавьте файлы в Git, создайте коммит и отправьте изменения:

    ```text
    git status
    git add homeworks/hw00/hello.py requirements.txt
    git commit -m "Complete homework 0"
    git push
    ```

## Ожидаемая структура

```text
homeworks/
└── hw00/
    ├── README.md
    └── hello.py
requirements.txt
```

Каталог `.venv` в репозиторий не добавляется.

## Что показать при сдаче

- ссылку на собственный репозиторий;
- успешный запуск `hello.py`;
- файл `requirements.txt`;
- коммит с выполненным заданием;
- умение объяснить назначение команд `clone`, `add`, `commit` и `push`.

## Критерий готовности

Задание готово, если преподаватель может клонировать репозиторий, установить зависимости из `requirements.txt` и запустить `hello.py` без ручного исправления путей или кода.

