import sys, re, os, statistics

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
            pp = pp + lvl * 0.85**(hardest-1) #Формула расчета пп
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
                total = 0.85**(hardest-1) #Формула расчета % для вывода)
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
        print("Версия ALTA V3.0 by Prosto_Maksim")

def lvlcal(fps,Timings):
    ReferenceFps = 240 #главный фпс
    ForReferencePoints = 10000 #балы за 240
    Compression = 225 #для выравнивания
    Points = 0 #балы
    Сounter = 0 #Сетчик таймингов
    HardestC = 99999999 #Сетчик самого сложного тайминга
    Mior = 0 #ср тайминг
    FreeC = 0 #Сетчик самого легкого тайминга

    if Timings == "0": #если ничего нет, то повторно попросить вести тайминги.
        print("\nПометка - Невидимые тайминги = сам тайминг / 2(В округление больше сторону)")
        print("Пометка - Любые клики которым просто достаточно нажать заранее - не должны учитываться никак")
        print("Пометка - Если тайминги слишком простые поставьте фпс ниже")
        print("Пометка - Если у вас 0 кадров поставьте фпс больше")        
        print("Тайминги так записываются - \n Тайминг;Тайминг;Тайминг;Тайминг | например 1;3;56;1;3 ")        

        try:
            Timings = input(">")
        except ValueError:
            print("Неправильный формат!")
            return 0
    
    for Timing in Timings.split(";"): #Делаем масив по ; и сразу заходим в цикл for
        try:
            Points = Points + ForReferencePoints / int(Timing) #считает балы за тайминг
        
        except ZeroDivisionError:
            print("Лвл не проходим!")
            return 0
        except ValueError:
            print("Это точно тайминги?")
            return 0
        
        if int(Timing) < int(HardestC): #Если тайминг сложнее старого, то он записывается
            HardestC = Timing
        
        if int(Timing) > int(FreeC): #Если тайминг легче старого, то он записывается
            FreeC = Timing
        
        Сounter = Сounter + 1 #сетчик таймингов
        Mior = Mior + int(Timing)
    
    Points = Points / (ReferenceFps / int(fps)) #Выравнивает балы по фпс
    result = Points / Compression #Выравнивем по эталону
    Mior = Mior / Сounter #Сумма таймингов на сумму кликов
    print("\nВерсия ALTA V3.0 by Prosto_Maksim")
    print("Тайминги уровня:" + str(Timings) + "\nВсего таймингов:" + str(Сounter))
    print("Фпс измерения:" + str(fps) + "\n")
    print("Самый сложный тайминг:" + str(HardestC)+"кадр")
    print("Средний тайминг:" + str(Mior)+"кадр")
    print("Самый простой тайминг:" + str(FreeC)+"кадр")
    print("\npp:" + str(round(result, 1)) + "\n")

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

def conv(Timings):
    coun = len(str(Timings))
    coun = coun - 1
    for Timing in str(Timings):
        if coun != 0:
            print(Timing, end=";")
        else:
            print(Timing, end="\n")
            print("Готово!")
        coun = coun - 1

standard = settingfiles("read","fps",1) #фпс по умолчанию
autoclear = settingfiles("read", "clear", 1) #какой режим чистки
TPS = int(standard) #Переносится стандартный фпс в переменную где с ним будут работать.

print("Версия ALTA V3.0 by Prosto_Maksim")
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
            print("  conv - конвертер c старого формата 12354 в новый формат 1;2;3;5;4 таймингов")
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
                TPS = int(standard)
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

        case "conv":
            try:
                if auto == 4: #если только команда
                    standard = input(">>")
                    conv(standard)
                else: #если с ней что-то еще написано
                    standard = requirements[-1]
                    conv(requirements[-1])
            except ValueError: #защита от идиота
                print("Ты точно ввел нужное?")
            except KeyboardInterrupt:
                sys.exit()
        case "dev":
            print("Главный - Prosto_Maksim - https://youtube.com/@Prosto_Maksim\n")
            print("Спасибо - SpaceKZ за идею - https://www.youtube.com/@spaceKZ1\n")
            print("Лицензия - GNU GPL v3 - https://www.gnu.org/licenses/quick-guide-gplv3.ru.html")
        