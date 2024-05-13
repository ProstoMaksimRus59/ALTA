import sys, random
import re, os
def Placal(): #Писал пиздец давно, так-что помню только часть, еще писал на приколе(пришлось переменные другими именами называть :D )
    hardest = 1 #по название доложно понятно быть)
    try:
        folder = input("Перетащите файл сюда>").replace('"', '')
    except KeyboardInterrupt:
        sys.exit()
    try:
        file = open(folder, 'r')
    except FileNotFoundError:
        print("Файл не найден или не читается")
        return 0
    pp = 0
    Scan = 1
    print("Player:" + file.readline().rstrip('\n')) #Показывает какой игрок
    while Scan == 1:
        pp1 = re.findall(r'\d+', file.readline().rstrip(' ').rstrip('\n').rstrip(':'))
        try:
            lvl = int(pp1[-1]) #для удобства (чтоб не по сто раз писать [0]) + все таки я написал -1 и теперь можно и арабские цифрами позоваться
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
    print("Версия ALTA v1.3 by Prosto_Maksim")
def lvlcal(F,ALLT): #На время просто через копипасту сделано, убранно только выбор фпс в этом коде)
    def hrub(E): #Осталось для соместимости Раньше все было в rub
        y = 0
        frame = 0
        h1 = 0
        for F in E:
            if int(F) == 0:
                y = 1
            frame = (int(F) + frame)
            h1 = h1 + 1
        frame = frame / h1
        print("Ср тайминг:" + str(frame) + " Кадр")
        if y != 1:
            return frame
        else:
            return 0
    def rub(Level): #Самое главное)
        protection = 0 #Ставить переменную(для проверки возможности лвла))
        score = 0
        for timing in Level:
            try:
                if int(timing) == 0: #Система анти идиот
                    protection = 1 #Записывает ту переменную 1
            except ValueError:
                return 0
            #        - imp- 240   120  80  60   48  40  34  30 26 - фреймы
            Eball = [99999,10000,5000,2500,1250,625,312,156,78,39] #Таблица выдочей ОЧЕЙ) новая
            score = score + Eball[int(timing)]
        if protection != 1: #если 0 - выдать результат, если нет послать нах)
            return score
        else:
            return 0 #направляет в нах
    def ppy(E): #тут раньше было больше строк)))))
        counter = 0
        for F in E:
            counter = counter + 1
        print("Всего таймингов:" + str(counter))
        return counter
    if ALLT == "0":
        print("Пометка - Невидимые тайминги = сам тайминг / 2(В округление больше сторону)")
        print("Пометка - Любые клики которым просто достаточно нажать заранее - не должны учитываться никак")
        print("Пометка - Если тайминги слишком простые поставьте фпс ниже")
        print("Пометка - Если тайминги в лвле слишком разные и нельзя изменить фпс то тайминги которые ушли чуть за 9 \n(напрмер 11) можно так-же писать как 9")
        print("Пометка - Если их дохуя таких проверять их отдельно, а потом просто умножать(надеюсь с матаном у вас все збс)")
        print("Пометка - Если у вас 0 кадров поставьте фпс больше")
    try:
        if ALLT == "0":
            ALLT = input(">")
        else:
            print("\n")
    except KeyboardInterrupt:
        sys.exit()
    print("Версия ALTA v1.3 by Prosto_Maksim")
    print("Тайминги уровня:" + str(ALLT))
    print("Фпс измерения:" + str(F))
    print("")
    T = rub(ALLT) #Коф тайминга
    C = ppy(ALLT) #скок таймингов
    raw = (T * F) #тайминги на фпс
    try:
        frame = F/hrub(ALLT) #еще осколок от старой версии) Считает средний фрейм по больнице
    except ZeroDivisionError:
        print("Это невозможно пройди!")
        print("Сделай больше фпс")
        return 0
    except ValueError:
        print("Мне кажется, что это не тайминги")
        return 0
    MC = 1000 / frame #Считает средний тайминг по больнице
    print("Лвл как " + str(C) + " Фреймов на " + str(round(frame, 2)) + "фпс(" + str(round(MC, 2)) + ")Мс")
    result = raw / 27000
    print("")
    print("PP:" + str(round(result, 1)))


TPS = 240 #фпс по умолчанию
print("Версия ALTA v1.3 by Prosto_Maksim")
print("Для помощи напишите help")
while 1 == 1:
    try:
        com = input("/") #ждет команд
    except KeyboardInterrupt:
        sys.exit()
    com = com.lower() #убирает высокий регистр
    main = com.split(' ')
    auto = len(com) #сетчик буквЬ)
    requirements = com.split(' ') #делает массив по пробелам
    match main[0]:
        
        case "help":
            print(" Основные команды:")
            print("  fps - меняет фпс расчета пп")
            print("  Placal - измерение сумарного пп игрока по файлу")
            print("  lvlcal - измерение пп лвла")
            print(" Доп:")
            print("  clear - очистить комадную строку")
            print("  exit - выйди из проги(можно юзать Ctrl + C )")
            print("  dev - список всех кто принимал участвие и так-далее")
        
        case "clear":
            clear()
        
        case "placal":
            Placal()
        
        case "fps": #Выбор кастом фпс
            try:
                if auto == 3: #если только команда
                    TPS = float(input(">>"))
                else: #если с ней что-то еще написано
                    TPS = int(requirements[-1])   #Выбирает последную из всего массива и считает как за выбранный фпс
            except ValueError: #защита от идиота
                print("Ты точно ввел фпс?")
            except KeyboardInterrupt:
                sys.exit()
            print("Фпс поставлен на " + str(TPS))
        
        case "lvlcal":
            if auto == 6:#если только команда
                lvlcal(TPS,"0")
            else: #если с ней что-то еще написано
                lvlcal(TPS,requirements[-1]) #Выбирает последную из всего массива и считает как за тайминги
        
        case "exit": #выход из проги
            sys.exit()
        
        case "dev":
            print("Главный - Prosto_Maksim - https://youtube.com/@Prosto_Maksim\n")
            print("Спасибо - SpaceKZ за идею - https://www.youtube.com/@spaceKZ1\n")
            print("Лицензия - GNU GPL v3 - https://www.gnu.org/licenses/quick-guide-gplv3.ru.html")