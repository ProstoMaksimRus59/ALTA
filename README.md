
![v2logoalta](https://github.com/ProstoMaksimRus59/ALTA/assets/102693495/505ff144-1093-4abd-bf47-5bc47f99aa60)



Математический расчет сложности для Geometry Dash

C Osu!(https://github.com/ppy) подобным методом

Для ее работы нужна заранее устоновленный GDMegaOverlay(https://github.com/maxnut/GDMegaOverlay)

За идею спасибо SpaceKZ(https://www.youtube.com/@spaceKZ1)
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
> -Нексторые антивирусы ругаются

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
