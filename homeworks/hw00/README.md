# ДЗ №0. Git, GitHub и настройка Python

**Темы:** Git, GitHub, репозиторий, виртуальное окружение Python, зависимости.

Задание выполняется после того, как преподаватель открыл доступ к репозиторию курса.

## Результат задания

После выполнения у вас будут:

- личный репозиторий в вашем аккаунте GitHub;
- локальная папка репозитория на компьютере;
- виртуальное окружение `.venv`;
- файл `hello.py`;
- файл `requirements.txt`;
- первый commit, отправленный на GitHub.

## Шаг 0. Что должно быть установлено

До начала работы нужны:

1. аккаунт на [GitHub](https://github.com/);
2. Git;
3. Python 3.11 или 3.12;
4. редактор кода, например VS Code или PyCharm.

Проверьте Git и Python в PowerShell:

```powershell
git --version
python --version
```

Обе команды должны вывести номер версии. Если команда не найдена, остановитесь и обратитесь к преподавателю: следующие шаги пока выполнять нельзя.

## Шаг 1. Создайте личную копию на GitHub

1. Войдите в свой аккаунт GitHub.
2. Откройте [репозиторий курса](https://github.com/slmnvdlr/geom_course_2026).
3. В правом верхнем углу страницы нажмите **Fork**.
4. На странице создания Fork:

   - в поле **Owner** выберите свой аккаунт;
   - название репозитория можно оставить `geom_course_2026`;
   - нажмите **Create fork**.

5. Дождитесь открытия созданного репозитория.
6. Проверьте адрес страницы. После `github.com/` должно стоять **ваше имя пользователя**, например:

   ```text
   https://github.com/student-name/geom_course_2026
   ```

Теперь на GitHub есть ваша удалённая копия. Все домашние задания вы будете отправлять именно в неё.

## Шаг 2. Скопируйте ссылку для клонирования

На странице **своего** репозитория:

1. нажмите зелёную кнопку **Code**;
2. выберите вкладку **Local**;
3. выберите **HTTPS**;
4. нажмите кнопку копирования рядом со ссылкой.

Ссылка должна содержать ваше имя пользователя:

```text
https://github.com/student-name/geom_course_2026.git
```

## Шаг 3. Клонируйте репозиторий на компьютер

Откройте PowerShell и перейдите в папку, где будут храниться учебные проекты. Например:

```powershell
cd "$env:USERPROFILE\Documents"
```

Выполните команду, подставив скопированную ссылку:

```powershell
git clone https://github.com/student-name/geom_course_2026.git
```

После клонирования перейдите внутрь созданной папки:

```powershell
cd geom_course_2026
```

Проверьте текущее расположение и состояние Git:

```powershell
Get-Location
git status
```

Ожидаемый результат `git status` начинается примерно так:

```text
On branch main
nothing to commit, working tree clean
```

### Если появилась ошибка `not a git repository`

Эта ошибка означает, что PowerShell открыт не внутри папки репозитория. Выполните:

```powershell
cd "$env:USERPROFILE\Documents\geom_course_2026"
git status
```

Не скачивайте проект кнопкой **Download ZIP**: ZIP-архив не содержит папку `.git` и не подходит для выполнения этого задания.

## Шаг 4. Укажите автора коммитов

Один раз настройте имя и электронную почту:

```powershell
git config --global user.name "Ваше Имя Фамилия"
git config --global user.email "ваша-почта@example.com"
```

Проверьте настройки:

```powershell
git config --global user.name
git config --global user.email
```

## Шаг 5. Создайте виртуальное окружение

Убедитесь, что PowerShell по-прежнему находится в папке `geom_course_2026`, затем выполните:

```powershell
python -m venv .venv
```

Активируйте окружение.

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

macOS/Linux:

```text
source .venv/bin/activate
```

После активации в начале строки терминала обычно появляется `(.venv)`.

## Шаг 6. Установите библиотеки

```powershell
python -m pip install --upgrade pip
python -m pip install numpy pandas matplotlib
```

## Шаг 7. Создайте программу

В папке `homeworks/hw00` создайте файл `hello.py`.

При запуске программа должна вывести:

- версию Python;
- версию NumPy;
- версию Pandas;
- версию Matplotlib.

Запустите программу из корня репозитория:

```powershell
python homeworks/hw00/hello.py
```

## Шаг 8. Сохраните зависимости

В корне репозитория выполните:

```powershell
python -m pip freeze > requirements.txt
```

После этого рядом с `README.md` должен появиться файл `requirements.txt`.

## Шаг 9. Создайте commit

Сначала посмотрите, какие файлы изменились:

```powershell
git status
```

Добавьте только файлы задания:

```powershell
git add homeworks/hw00/hello.py requirements.txt
```

Создайте commit:

```powershell
git commit -m "Complete homework 0"
```

Commit — это сохранённая точка в истории проекта. Пока он находится только на вашем компьютере.

## Шаг 10. Отправьте изменения на GitHub

```powershell
git push
```

Откройте свой репозиторий в браузере и обновите страницу. Проверьте, что появились:

- `requirements.txt`;
- `homeworks/hw00/hello.py`;
- commit с сообщением `Complete homework 0`.

## Что показать при сдаче

1. Ссылку на свой репозиторий GitHub.
2. Вывод программы `hello.py`.
3. Файл `requirements.txt`.
4. Commit `Complete homework 0` на GitHub.
5. Умение своими словами объяснить `fork`, `clone`, `commit` и `push`.

## Критерий готовности

Задание готово, если преподаватель может открыть ваш репозиторий, увидеть commit, клонировать проект, установить зависимости из `requirements.txt` и запустить `hello.py` без ручного исправления путей или кода.
