
<img width="128" height="128" alt="logo6" src="https://github.com/user-attachments/assets/a626ccdc-80a4-4df5-be06-76e4e10b2b0e" />





**Математический расчет сложности для Geometry Dash**

C Osu!(https://github.com/ppy) подобным методом

Для ее работы(расчета сложности) нужна заранее устоновленный какой-то "Frame step и frame counter" Можно от EclipseMenu(https://github.com/EclipseMenu/)

За идею спасибо SpaceKZ (и за balcal)(https://www.youtube.com/@spaceKZ1)

Гайд - (https://youtu.be/SoG0P0cJfTI?si=K7qLz3IlGcEuBMqO)

возможности ALTA (Advanced Level Timing Analyzer)

>Расчет Сложности уровня в pp.

>Работа с файлами своего формата (.altapl и .altalvl)

>Работа с датабазой тоесь 'создовать, удалять, сохранять, читать, модифицировать(добавлять уровни и игроков, добавлять и удалять викторов с уровня, смотреть викторов на определенном уровне, изменять данные уровня(тайминги, верифера,id),Пересчитывать, обновлять), c силамами самой ALTA'

>Работа с файлом .kdenlive - для создания видео с ALTA

.

.

>С v6.1 появилась возможность переводить ALTA без пересбоки ее.

>файл перевода - translation.alta

>; - как первая в строке делает строку коментарием.

>Перевод делается виде

>Ориг текст

>Сдедущая строка - new text

>И так весь перевод.

>для перевода все таки придется в исходнике покапатся зато. оно даст менять если даже файл ориг на русском.

.

.

>Через lite или дс bot версии создовать полноценный лист.

>https://github.com/ProstoMaksimRus59/ALTA-LITE

>https://github.com/ProstoMaksimRus59/alta-txt-list-generator

Для листа через lite нужно его будет самостоятельно собрать файл в exe

Для через бота нужно будет или написать своего более нормальнго бота и ипользовать мои библиотеки. или просто все от меня(там есть архив с ботом базовым)
.

.

.

.

.

.

**Для сборки**
>1.pip instal colorama

>2.выбор между PyInstaller или nuitka

1.Через PyInstaller
> Устоновка PyInstaller
>
> pip install PyInstaller
>
> Сборка в exe
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
> Компиляция в exe
>
> python -m nuitka --follow-imports --windows-icon-from-ico=logo.ico '.\ALTA public.py' --onefile

p.s для работы(если ошибка при запуске) ALTA -- скачайте python 3.10 или 3.11

https://www.python.org/downloads/release/python-31011/
