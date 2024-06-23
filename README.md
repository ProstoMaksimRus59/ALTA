
![logoalta](https://github.com/ProstoMaksimRus59/ALTA/assets/102693495/7f4e2a94-aa17-4dad-825f-74e74c47a355)



Математический расчет сложности для Geometry Dash

C Osu!(https://github.com/ppy) подобным методом

Для ее работы нужна заранее устоновленный какой-то "Frame step" Можно от GDMegaOverlay(https://github.com/maxnut/GDMegaOverlay)

За идею спасибо SpaceKZ (и за balcal)(https://www.youtube.com/@spaceKZ1)

Гайд - https://youtu.be/mJTOHU9eb0w?si=chv7xQWFy7MvxHmB (Частично устарел)

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
