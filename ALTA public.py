from time import sleep
import sys, random
import re, os
def Placal(): #Писал пиздец давно, так-что помню только часть, еще писал на приколе(пришлось переменные другими именами называть :D )
    hardest = 1 #по название доложно понятно быть)
    try:
        folder = input("Перетащите файл сюда>").replace('"', '')
    except KeyboardInterrupt:
        sys.exit()
    #print(folder)
    try:
        file = open(folder, 'r')
    except FileNotFoundError:
        print("Файл не найден или не читается")
        return 0
    pp = 0
    Scan = 1
    print("Player:" + file.readline().rstrip('\n')) #Показывает какой игрок
    while Scan == 1:
        #pp1 = p.readline().rstrip('\n')
        pp1 = re.findall(r'\d+', file.readline().rstrip(' ').rstrip('\n').rstrip(':'))
        #print(pp1)
        try:
            lvl = int(pp1[0]) #для удобства (чтоб не по сто раз писать [0])
        except IndexError:
            print("Файл поврежден")
            return 0
        if lvl != 0:
            pp = pp + lvl * 0.75**(hardest-1) #Формула расчета пп
            hardest = hardest + 1
        if lvl == 0:
            Scan = 0
    print("PP:" + str(round(pp)))
    file.close()
    Scan = "1"
    file = open(folder, 'r')
    file.readline().rstrip('\n') #Убирает данные о имени игрока
    total = 0
    hardest = 1
    while Scan != "0": #Повторно обротока для вывода % от всех лвлов
            if Scan != "0":
                total = 0.75**(hardest-1) #Формула расчета % для вывода)
                Scan = file.readline().rstrip('\n') #Чтение строки из файла
                if Scan != "0":
                    print(str(Scan) + "pp " + str(round(total * 100, 2)) + "%")
                hardest = hardest + 1
            if Scan == "0": #if else лень :D
                Scan = "0"
                print("все!")
                file.close()

def clear(): #Ну даже не знаю??? что это делает??? :D
    os.system('cls' if os.name == 'nt' else 'clear') 
    print("Версия ALTA v1.1 by Prosto_Maksim")
def lvlcal(F): #На время просто через копипасту сделано, убранно только выбор фпс в этом коде)
    def hrub(E): #Осталось для соместимости Раньше все было в rub
        y = 0
        hh = 0
        h1 = 0
        for F in E:
            if int(F) == 0:
                y = 1
            hh = (int(F) + hh)
            h1 = h1 + 1
        hh = hh / h1
        print("Ср тайминг:" + str(hh) + " Кадр")
        if y != 1:
            return hh
        else:
            return 0
    def rub(Level): #Самое главное)
        protection = 0 #Ставить переменную(для проверки возможности лвла))
        score = 0
        #h1 = 0
        for timing in Level:
            try:
                if int(timing) == 0: #Система анти идиот
                    protection = 1 #Записывает ту переменную 1
            except ValueError:
                return 0
            if int(timing) == 0: #Таблица выдочей ОЧЕЙ)
                score = score + 99999 #Сделал для чтоб потроллить хороших кодеров(как и всю прогу))))))
            if int(timing) == 1:
                score = score + 10000 #за 240фпс фрейм
            if int(timing) == 2:
                score = score + 5000 #за 120фпс фрейм
            if int(timing) == 3:
                score = score + 2500 #за 80фпс фрейм
            if int(timing) == 4:
                score = score + 1250 #за 60фпс фрейм
            if int(timing) == 5:
                score = score + 625 #за 48фпс фрейм
            if int(timing) == 6:
                score = score + 312 #за 40фпс фрейм
            if int(timing) == 7:
                score = score + 156 #за 34фпс фрейм
            if int(timing) == 8:
                score = score + 78 #за 30фпс фрейм
            if int(timing) == 9:
                score = score + 39 #за 26фпс фрейм
            #hh = (int(F) + hh) # остаток от старой системы                         за предыдущие мне доложны выдать премию - фанат яндеры дева :D еше бля я писал для прикола(случайно вышло что он стал серьезным проектом) еще в час ночи)
            #h1 = h1 + 1
        if protection != 1: #если 0 - выдать результат, если нет послать нах)
            return score
        else:
            return 0 #направляет в нах
    def ppy(E): #тут раньше было больше строк)))))
        h1 = 0
        for F in E:
            h1 = h1 + 1
        print("Всего таймингов:" + str(h1))
        return h1
    print("Пометка - Невидимые тайминги = сам тайминг / 2(В округление больше сторону)")
    print("Пометка - Любые клики которым просто достаточно нажать заранее - не должны учитываться никак")
    print("Пометка - Если тайминги слишком простые поставьте фпс ниже")
    print("Пометка - Если тайминги в лвле слишком разные и нельзя изменить фпс то тайминги которые ушли чуть за 9 \n(напрмер 11) можно так-же писать как 9")
    print("Пометка - Если их дохуя таких проверять их отдельно, а потом просто умножать(надеюсь с матаном у вас все збс)")
    print("Пометка - Если у вас 0 кадров поставьте фпс больше")
    try:
        ALLT = input(">")
    except KeyboardInterrupt:
        sys.exit()
    print("Версия ALTA v1.1 by Prosto_Maksim")
    print("Тайминги уровня:" + str(ALLT))
    print("Фпс измерения:" + str(F))
    print("")
    T = rub(ALLT) #Коф тайминга
    C = ppy(ALLT) #скок таймингов
    TF = (T * F) #тайминги на фпс
    try:
        jj1 = F/hrub(ALLT) #еще осколок от старой версии) Считает средний фрейм по больнице
    except ZeroDivisionError:
        print("Это невозможно пройди!")
        print("Сделай больше фпс")
        return 0
    except ValueError:
        print("Мне кажется, что это не тайминги")
        return 0
    jj = 1000 / jj1 #Считает средний тайминг по больнице
    print("Лвл как " + str(C) + " Фреймов на " + str(round(jj1, 2)) + "фпс(" + str(round(jj, 2)) + ")Мс")
    TTF = TF / 27000
    print("")
    print("PP:" + str(round(TTF, 1)))


TPS = 240 #фпс по умолчанию
print("Версия ALTA v1.1 by Prosto_Maksim")
print("Для помощи напишите help")
while 1 == 1:
    try:
        com = input("/") #ждет команд
    except KeyboardInterrupt:
        sys.exit()
    com = com.lower() #убирает высокий регистр
    match com:
        case "help":
            print(" Все команды:")
            print(" fps - меняет фпс расчета пп")
            print(" Placal - измерение сумарного пп игрока по файлу")
            print(" lvlcal - измерение пп лвла")
            print(" clear - очистить комадную строку")
        case "clear":
            clear()
        case "placal":
            Placal()
        case "fps": #Выбор кастом фпс
            try:
                TPS = float(input(">>"))
            except ValueError: #защита от идиота
                print("Ты точно ввел фпс?")
            except KeyboardInterrupt:
                sys.exit()
            print("Фпс поставлен на " + str(TPS))
        case "lvlcal":
            lvlcal(TPS)