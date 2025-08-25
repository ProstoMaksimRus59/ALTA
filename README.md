
<img width="128" height="128" alt="logoalta5" src="https://github.com/user-attachments/assets/a931e556-a2c5-41c5-9fa6-ad13aa7d6dd2" />





Математический расчет сложности для Geometry Dash

C Osu!(https://github.com/ppy) подобным методом

Для ее работы(расчета сложности) нужна заранее устоновленный какой-то "Frame step" Можно от EclipseMenu(https://github.com/EclipseMenu/)

За идею спасибо SpaceKZ (и за balcal)(https://www.youtube.com/@spaceKZ1)

Гайд - https://youtu.be/mJTOHU9eb0w?si=chv7xQWFy7MvxHmB (устарел)

.

.

.

.

.

.

Для сборки программы можно юзать -

1.Через PyInstaller
> Устоновка PyInstaller
>
> pip install PyInstaller
>
> Компиляция exe
> 
> pyinstaller '.\ALTA public.by' -i logo.ico -F

2.Через Nuitka - текущий с v1.3
> Устоновка Nuitka
>
> pip install nuitka
>
> !Питон из Microsoft store не подойдет!
> !Ставьте обычную версию!
>
> Компиляция exe
>
> python -m nuitka --follow-imports --windows-icon-from-ico=logo.ico '.\ALTA public.py'

-- Помощь к выбору --

Плюсы PyInstaller
> +Простота(работает без танцов с бубном)
>
> +Надежность и точность(что написали - что и будет)
>
Минусы PyInstaller
> -Скорость(медленные Nuitka)
>
> -размер файла(он все-таки на самом деле не компилятор)
>
> -совместимость(у кого ос старше, она может не запускатся)
>
> -Некоторые антивирусы ругаются

Плюсы Nuitka
> +Скорость(быстрее PyInstaller)
>
> +Размер файла
>
> +Запускается почти всегда(ей особо не важна версия ос)
>
Минусы Nuitka
> -Сложность(бывает нужны танцы)
>
> -Точность(может начать криво работать код после сборки)

p.s для работы(если ошибка при запуске) ALTA -- скачайте python 3.11

https://apps.microsoft.com/detail/9nrwmjp3717k?hl=ru-RU&gl=RU
