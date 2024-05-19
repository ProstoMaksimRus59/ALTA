import sys, re, os

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

def clear(mode): #Ну даже не знаю??? что это делает??? :D
    os.system('cls' if os.name == 'nt' else 'clear') 
    if mode != "0": #Если не авто чистка, то показать версию.
        print("Версия ALTA V2.1 by Prosto_Maksim")

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
    
    def rub(Level,TPS): #Самое главное)
        protection = 0 #Ставить переменную(для проверки возможности лвла))
        score = 0
        
        for timing in Level:
            try:
                if int(timing) == 0: #Система анти идиот
                    protection = 1 #Записывает ту переменную 1
            except ValueError:
                return 0
            #  - баллы(240)  240  120  80   60  48    40   34   30   26
            
            Eball = [99999,10000,5000,3333,2500,2000,1666,1428,1250,1111] #Таблица выдочей ОЧЕЙ) новая
            score = score + Eball[int(timing)] / (240/TPS) #считает балы и заодно адаптирует таблицу сверху для всех фпс)
        
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
    
    print("Версия ALTA V2.1 by Prosto_Maksim")
    print("Тайминги уровня:" + str(ALLT))
    print("Фпс измерения:" + str(F))
    print("")
    
    raw = rub(ALLT,F) #сырые балы
    C = ppy(ALLT) #скок таймингов
   
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
    result = raw / 225 #выравнивание балов по TCC1

    print("Лвл как " + str(C) + " Фреймов на " + str(round(frame, 2)) + "фпс(" + str(round(MC, 2)) + ")Мс")
    print("")
    print("PP:" + str(round(result, 1)))

def settingfiles(mode, typE, Number): #Отвечает за сохранения настроек в файл.
    
    def reset(fist): #сброс файла
        if fist != "1": #ругатся если это был не первый запуск)
            print("Ошибка чтения файла настроек")
            print("Выполнен его сброс")
            print("Ошибка была по:" + str(typE))
        Filesetting = open('setting.alta', 'w') #Создает стоковый файл
        Filesetting.write("FPS:240 \n")
        Filesetting.write("Clear:0")
        Filesetting.close()
    
    Ok = 0
    
    folder = os.listdir() #ищет файл
    for files in folder:
        match files:
            case "setting.alta": #если нашел
                Ok = 1 #          все значить супер
    if Ok != 1: # если его нет, то сброс
        reset("1")
    
    match mode: #Какой режим - чтение или запись.
        
        case "read":            
            Filesetting = open('setting.alta', 'r')
            
            match typE: #Какую настройку считать
                
                case "fps":
                    read = re.findall(r'\d+', Filesetting.readline().rstrip(' ').rstrip('\n').rstrip(':'))
                    Filesetting.close()
                    if not read or read[-1] == "0": #если битый файл
                            reset("0")
                            return 240
                    Filesetting.close()
                    return read[-1]
                
                case "clear":
                    Filesetting.readline()
                    read = re.findall(r'\d+', Filesetting.readline().rstrip(' ').rstrip('\n').rstrip(':'))
                    Filesetting.close()
                    if not read: #если битый файл
                            reset("0")
                            return 0
                    Filesetting.close()
                    return read[-1]
        
        case "white": #режим записи
            Filesetting = open('setting.alta', 'r') #сохраняет настройки
            oldfps = Filesetting.readline().rstrip('\n')
            oldclean = Filesetting.readline().rstrip('\n')
            Filesetting.close()
            
            match typE: #Какую настройку изменить
                
                case "fps": #создает новые настройки с новым фпс
                  Filesetting = open('setting.alta', 'w')  
                  Filesetting.write("FPS:" + str(Number) + "\n")
                  Filesetting.write(oldclean)
                  Filesetting.close()
                
                case "clear": #создает новые настройки с другим режимом чистки
                  Filesetting = open('setting.alta', 'w')  
                  Filesetting.write(str(oldfps) + "\n")
                  Filesetting.write("Clear:" + str(Number))
                  Filesetting.close()                    

standard = settingfiles("read","fps",1) #фпс по умолчанию
autoclear = settingfiles("read", "clear", 1) #какой режим чистки
TPS = int(standard) #Переносится стандартный фпс в переменную где с ним будут работать.

print("Версия ALTA V2.1 by Prosto_Maksim")
print("Для помощи напишите help")

while 1 == 1:
    
    try:
        com = input("/") #ждет команд
        if autoclear == "1":
            clear("0")
    except KeyboardInterrupt:
        sys.exit()
    com = com.lower() #убирает высокий регистр
    main = com.split(' ')
    auto = len(com) #сетчик буквЬ)
    requirements = com.split(' ') #делает массив по пробелам
    
    match main[0]:
        
        case "help":
            print(" Основные команды:")
            print("  fps - меняет фпс расчета pp")
            print("  fps.set - фпс который будет при запуске")
            print("  Placal - измерение сумарного pp игрока по файлу")
            print("  lvlcal - измерение пп лвла")
            print(" Доп:")
            print("  clear - очистить комадную строку")
            print("  clear.auto - оставляет в командной строке только последнюю команду")
            print("  exit - выйди из проги(можно юзать Ctrl + C )")
            print("  dev - список всех кто принимал участие и так-далее")
        
        case "clear":
            clear("1")
        
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
            if TPS == 0: #cброс
                print("сброшено!")
                TPS = standard
            print("Фпс поставлен на " + str(TPS))
        
        case "fps.set":
            try:
                if auto == 7: #если только команда
                    standard = round(float(input(">>")))
                    settingfiles("white","fps", standard)
                else: #если с ней что-то еще написано
                    standard = int(requirements[-1])
                    settingfiles("white","fps", int(requirements[-1]))  #Выбирает последную из всего массива и считает как за выбранный фпс
            except ValueError: #защита от идиота
                print("Ты точно ввел фпс?")
            except KeyboardInterrupt:
                sys.exit()
            if standard == 0: #cброс
                print("сброшено!")
                settingfiles("white","fps","240")
                standard = 240
            print("Фпс по умолчанию>" + str(round(standard)))
        
        case "clear.auto": #Переключение режимов чистки
            if autoclear == "1":
                autoclear = "0"
                settingfiles("white","clear", "0")
                print("Авто чистка - выкл") #Выкл
            else:
                autoclear = "1" 
                settingfiles("white","clear", "1")
                print("Авто чистка - вкл") #Вкл
        
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