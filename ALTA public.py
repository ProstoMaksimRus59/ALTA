import sys, re, os, shutil,random,zipfile,statistics,math

def clear(mode): #Ну даже не знаю??? что это делает??? :D
    os.system('cls' if os.name == 'nt' else 'clear') 
    if mode != "0": #Если не авто чистка, то показать версию.
        print("Версия ALTA V3.4 by Prosto_Maksim")
print("Загрузка.    1/15")

def Placal(folder,data): #Писал пиздец давно, так-что помню только часть, еще писал на приколе(пришлось переменные другими именами называть :D )
    hardest = 1 #по название доложно понятно быть)
    if folder == "0":
        try:
            folder = input("Перетащите файл сюда>").replace('"', '')
        except KeyboardInterrupt:
            sys.exit()
    try:
        file = open(folder, 'r')
    except FileNotFoundError:
        if data == "1":
            print("Не найденно в базе")
        else:
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
                if data == "0":
                    print("все!")
                file.close()
clear("0")
print("Загрузка..   2/15")

def lvlcal(fps,Timings,seting):
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
        except KeyboardInterrupt:
            sys.exit()
    
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
    print("\nВерсия ALTA V3.4 by Prosto_Maksim")
    print("Тайминги уровня:" + str(Timings) + "\nВсего таймингов:" + str(Сounter))
    print("Фпс измерения:" + str(fps) + "\n")
    print("Самый сложный тайминг:" + str(HardestC)+"кадр")
    print("Средний тайминг:" + str(Mior)+"кадр")
    print("Самый простой тайминг:" + str(FreeC)+"кадр\n")
    if seting == "1": #Вывод баланса
        balanceKZ(fps,Timings,"1")
    print("pp:" + str(round(result, 1)) + "\n")

clear("0")
print("Загрузка...   3/15")

def settingfiles(mode, typE, Number): #Отвечает за сохранения настроек в файл.
    
    def reset(fist): #сброс файла
        if fist != "1": #ругатся если это был не первый запуск)
            print("Ошибка чтения файла настроек")
            print("Выполнен его сброс")
            print("Ошибка была по:" + str(typE))
        Filesetting = open('setting.alta', 'w') #Создает стоковый файл
        Filesetting.write("FPS:240 \n")
        Filesetting.write("Clear:0 \n")
        Filesetting.write("lvlbanace:0")
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
                
                case "lvlbanace":
                    Filesetting.readline()
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
            oldbanace = Filesetting.readline().rstrip('\n')
            Filesetting.close()
            
            match typE: #Какую настройку изменить
                
                case "fps": #создает новые настройки с новым фпс
                  Filesetting = open('setting.alta', 'w')  
                  Filesetting.write("FPS:" + str(Number) + "\n")
                  Filesetting.write(oldclean + "\n")
                  Filesetting.write(str(oldbanace) + "\n")
                  Filesetting.close()
                
                case "clear": #создает новые настройки с другим режимом чистки
                  Filesetting = open('setting.alta', 'w')  
                  Filesetting.write(str(oldfps) + "\n")
                  Filesetting.write("Clear:" + str(Number) + "\n")
                  Filesetting.write(str(oldbanace) + "\n")
                  Filesetting.close()                    

                case "lvlbanace": #создает новые настройки с другим режимом чистки
                  Filesetting = open('setting.alta', 'w')  
                  Filesetting.write(str(oldfps) + "\n")
                  Filesetting.write(oldclean + "\n")
                  Filesetting.write("lvlbanace:" + str(Number) + "\n")
                  Filesetting.close()  
clear("0")
print("Загрузка.     4/15")

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

clear("0")
print("Загрузка..    5/15")

def Victors(lvl):
    try:
        files = os.listdir("Base") #В скобаках какой папке база.
    except FileNotFoundError:
        print("Датабаза не найдена")
        return 0
    
    altapl = list(filter(lambda x: x.endswith('.altapl'), files)) #фильтр форматов
    print("Имеют его>", end=" ")
    
    for file in altapl:
        Scan = 1
        data = open("Base/" + file, 'r')
        while Scan != "0":
            Scan = data.readline().rstrip('\n')
            Scan = Scan.split(":")[0]
            if Scan.lower() == lvl.lower():
                print(file.split(".altapl")[0] + ",", end=" ") #Вывод всех у кого есть лвл в пройденных 
    print("\n")

clear("0")
print("Загрузка...   6/15")

standard = settingfiles("read","fps",1) #фпс по умолчанию
autoclear = settingfiles("read", "clear", 1) #какой режим чистки
KZbalance = settingfiles("read", "lvlbanace", 1)
TPS = int(standard) #Переносится стандартный фпс в переменную где с ним будут работать.

clear("0")
print("Загрузка.     7/15")

def addlvl():
    try:
        data = open("Base/lvldatabase.altalvl", 'a')
    except FileNotFoundError:
        print("Датабазa не найдена")
        return 0
    try:
        print("Название лвла") #Это почти как заглушка, потом будет что-то нормальное)
        com1 = input(">")
        print("Автор(ы) лвла")
        com2 = input(">")
        print("Верификатор лвла")
        com3 = input(">")
        print("Тайминги лвла")
        com4 = input(">")
        print("FPS")
        com5 = input(">")
        print("Баланс>")
        fan = input(">")
        print("PP у лвла")
        com6 = input(">")
    except KeyboardInterrupt:
        sys.exit()
    data.write("" + str(com1.lower()))
    data.write("\nAuthor(S):" + str(com2.lower()))
    data.write("\nVerification:" + str(com3.lower()))
    data.write("\nTimings:" + str(com4.lower()))
    data.write("\nFPS:" + str(com5.lower()))
    data.write("\nbalance:" + str(fan.lower()))
    data.write("\nPP:" + str(com6.lower()))
    data.write("\nend\n")
    data.close

clear("0")
print("Загрузка..    8/15")

def infolvl(lvl):
    good = 0
    try:
        data = open("Base/lvldatabase.altalvl", 'r')
    except FileNotFoundError:
        print("Датабаза не найдена")
        return 0
    scan = 0
    while scan == 0:
        lvlscan = data.readline().rstrip('\n')
        if lvlscan.lower() == lvl.lower():
            info = 6
            while info != 0:
                info = info - 1
                print(data.readline().rstrip('\n').lower())
                scan = 1
                good = 1
        if lvlscan == "":
            scan = 1
    
    if good == 0:
        print("лвл не Найден в базе")
    data.close()

clear("0")
print("Загрузка...   9/15")

def addvict(Player,lvld,pp):
    try:
        pp = float(pp)
    except ValueError:
        print("Точно вел пп?")
        return 0
    pp = round(pp)
    Player = Player + ".altapl"
    
    try:
        data = open("Base/" + Player, 'r')
    except FileNotFoundError:
        print("такого игрока нет в датабазе или самой датабазы")
        return 0
    name = data.readline()
    lvl = data.readlines()
    hardest = 0
    Comlit = 1
    
    while Comlit == 1:
        ll = lvl[hardest].split(":")[-1].rstrip('\n')
        hardest = hardest + 1
        if pp > int(ll):
            New = (hardest - 1)
            Comlit = 0
    data.close()
    data = open("Base/" + Player, 'w')
    data.write(name)
    hardest = 0
    
    print("Новый топ", end=" ")
    print(New + 1, end=" ")
    print("У " + str(name))
    
    if New == 0:
        data.write(str(lvld) + ":" + str(pp) + "\n")
    
    while New != 0:
        New = New - 1
        data.write(lvl[hardest])
        hardest = hardest + 1
        if New == 0:
            data.write(str(lvld) + ":" + str(pp) + "\n")
    scan = "1"
    
    while scan != "0":
        scan = lvl[hardest]
        data.write(lvl[hardest])
        hardest = hardest + 1
    data.close()

clear("0")
print("Загрузка.     10/15")

def createdb():
    files = os.listdir() #Проверка на наличие уже датабазы
    for scan in files:
        if scan == "Base": #если есть то -
            antidelete = random.randint(1000,9999)
            try:
                com = input("Вы уверенны удалить старую базу??(напишите в ответ>" + str(antidelete) + ") >" )
            except KeyboardInterrupt:
                sys.exit()
            if int(com) == antidelete:
                shutil.rmtree("Base")
                print("Датабаза удаленна!")
            else:
                print("Неправильно!")
                return 0
    os.mkdir("Base")
    new = open("Base/lvldatabase.altalvl", 'w')
    new.close()
    print("Датабаза создана!")

clear("0")
print("Загрузка..    11/15")

def addpla(pla):
    files = os.listdir("Base/")
    for scan in files: #не дает повторно создать профиль.
        if pla == scan.split(".")[0]:
            print("Игрок уже есть в базе")
            return 0
    
    new = open("Base/"+str(pla)+".altapl", 'w') #если все-таки его нет, то это-
    new.write(pla)
    new.write("\n0")
    new.close()
    print("Игрок добавлен")

clear("0")
print("Загрузка...   12/15")

def loaddb():
    files = os.listdir() #Проверка на наличие уже датабазы
    for scan in files:
        if scan == "Base": #если есть то -
            antidelete = random.randint(1000,9999)
            try:
                com = input("Вы уверенны удалить старую базу??(напишите в ответ>" + str(antidelete) + ") >" )
            except KeyboardInterrupt:
                sys.exit()
            if int(com) == antidelete:
                shutil.rmtree("Base")
                print("Датабаза удаленна!")
            else:
                print("Неправильно!")
                return 0
    try:
        db = input("Перетащите датабазу сюда>").replace('"', '')
    except KeyboardInterrupt:
        sys.exit()
    try:
        zip = zipfile.ZipFile(db, 'r')
    except FileNotFoundError:
        print("Не найденно")
        return 0
    zip.extractall('')
    zip.close()
    print("Датабаза загружена!")

clear("0")
print("Загрузка...   13/15")

def savedb():
    try:
        name = input("Название>")
        folder = input("Куда создать?(путь до любой папки)>").replace('"', '')
    except KeyboardInterrupt:
        sys.exit()
    zip = zipfile.ZipFile(name +".zip", "w") #Создает архив
    zip.write("Base") #Создает папку в нем
    files = os.listdir("Base/") #Смотрит что у вас в базе
    
    for scan in files: #Смотрит что у вас в базе
        zip.write("Base/" + scan) #что нашел в ахрив
    
    zip.close() #закрывает ахрив
    shutil.copyfile(name + ".zip", folder + "/"+ name + ".zip") #копирует куда нужно
    os.remove(name + ".zip") #Удалает уже ненужный ахрив
    print("Датабаза сохранена!")

clear("0")
print("Загрузка.     14/15")

def infopla(pla):
    if pla == "0":
        
        print("Все игроки в базе")
        files = os.listdir("Base/") #ищет в базе игроков
        files = filter(lambda x: x.endswith('.altapl'), files)
        
        for plaer in files: #Кусок от placal
            hardest = 1 #по название доложно понятно быть)
            folder = "base/" + plaer.replace('"', '')
            file = open(folder, 'r')
            pp = 0
            Scan = 1
            print("\nPlayer:" + file.readline().rstrip('\n')) #Показывает какой игрок
    
            while Scan == 1:
                pp1 = re.findall(r'\d+', file.readline().rstrip(' ').rstrip('\n').rstrip(':'))
        
                lvl = int(pp1[-1]) #для удобства (чтоб не по сто раз писать [0]) + все таки я написал -1 и теперь можно и арабские цифрами позоваться
        
                if lvl != 0:
                    pp = pp + lvl * 0.85**(hardest-1) #Формула расчета пп
                    hardest = hardest + 1
        
                if lvl == 0:
                    Scan = 0
            print("PP:" + str(round(pp)))
    else:
        pla = pla + '.altapl'
        
        Placal("Base/" + pla, "1")

clear("0")
print("Загрузка..     15/15")

def balanceKZ(fps,sequence,lvlcalmode): #Не мое, так-что писать ничего не буду)
    score = 0
    points = 0
    list = []
    for i in sequence.split(";"):
        list.append(int(i))
    for k in list:
        if k == statistics.mode(list):
            score=score+1
        elif k < statistics.mode(list):
            score=score+1-(((2*math.pi)**(statistics.mode(list)/int(k)))/fps)
        elif k > statistics.mode(list):
            score=score+1-(((2*math.pi)**(int(k)/statistics.mode(list)))/fps)
    points = score/len(list)*10
    if points < 0:
        points=0
    if lvlcalmode != "1":
        print('Ср тайминг:',str(round(statistics.mean(list),2)),'кадр')
    print('Баланс:',str(round(points,2))+'/10')

clear("0")

print("Версия ALTA V3.4 by Prosto_Maksim")
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
    requirementscalving = com.split(' ') #делает массив по пробелам
    Length = len(requirementscalving) - 1 #Смотрить сколько в массиве элементов.
    if Length != 0: #Смотрить если их не один, то
        requirements = str(requirementscalving[Length])
        Length = Length - 1
    else:
        requirements = str(requirementscalving[-1])
    while Length != 0: #Смотрить если их больше двух, то
        requirements = str(requirementscalving[Length] + " " + str(requirements))
        Length = Length - 1
    match main[0]:
        
        case "help":
            print(" Основные команды:")
            print("  fps - меняет фпс расчета pp")
            print("  fps.set - фпс который будет при запуске")
            print("  Placal - измерение сумарного pp игрока по файлу")
            print("  lvlcal - измерение пп лвла")
            print("  balcal - измерение баланса лвла(by SpaceKZ)")
            print(" Для датабазы:")
            print("  add.pla - добавить игрока в датабазу")
            print("  info.pla - Список игроков(если написать ник, то будет работать как placal)")
            print("  victors - Ищет всех викторов нужного лвла")
            print("  add.vict - добавить игроку пройденный лвл")
            print("  add.lvl - добавить лвл в датабазу")
            print("  info.lvl - поиск и инфа о лвле")
            print("  load.db - Загружить датабазу")
            print("  save.db - Сохранить датабазу")
            print("  create.db - создать новую датабазу(Удалить если она была)")
            print("  delete.db - Просто удалить установленную датабазу")
            print(" Доп:")
            print("  conv - конвертер c старого формата 12354 в новый формат 1;2;3;5;4 таймингов")
            print("  clear - очистить комадную строку")
            print("  clear.auto - оставляет в командной строке только последнюю команду")
            print("  lvlcal.bal - встраивает в измерения lvlcal и balcal")
            print("  exit - выйди из проги(можно юзать Ctrl + C )")
            print("  dev - список всех кто принимал участие и так-далее")
        case "clear":
            clear("1")
        
        case "placal":
            Placal("0","0")
        
        case "fps": #Выбор кастом фпс
            try:
                if auto == 3: #если только команда
                    TPS = float(input(">>"))
                else: #если с ней что-то еще написано
                    TPS = int(requirements)   #Выбирает последную из всего массива и считает как за выбранный фпс
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
                    standard = int(requirements)
                    settingfiles("white","fps", int(requirements))  #Выбирает последную из всего массива и считает как за выбранный фпс
            except ValueError: #защита от идиота
                print("Ты точно ввел фпс?")
                standard = settingfiles("read","fps",1)
            except KeyboardInterrupt:
                sys.exit()
            if standard == 0: #cброс
                print("сброшено!")
                settingfiles("white","fps","240")
                standard = 240
            print("Фпс по умолчанию>" + str(round(int(standard), 1)))
        
        case "clear.auto": #Переключение режимов чистки
            if autoclear == "1":
                autoclear = "0"
                settingfiles("white","clear", "0")
                print("Авто чистка - выкл") #Выкл
            else:
                autoclear = "1" 
                settingfiles("white","clear", "1")
                print("Авто чистка - вкл") #Вкл
        
        case "lvlcal.bal": #Переключение режимов чистки
            if KZbalance == "1":
                KZbalance = "0"
                settingfiles("white","lvlbanace", "0")
                print("Показ баланса - выкл") #Выкл
            else:
                KZbalance = "1" 
                settingfiles("white","lvlbanace", "1")
                print("Показ баланса - вкл") #Вкл        
        
        case "lvlcal":
            if auto == 6:#если только команда
                lvlcal(TPS,"0",KZbalance)
            else: #если с ней что-то еще написано
                lvlcal(TPS,requirements,KZbalance) #Выбирает последную из всего массива и считает как за тайминги
        
        case "exit": #выход из проги
            sys.exit()

        case "conv":
            try:
                if auto == 4: #если только команда
                    com = input(">>")
                    conv(com)
                else: #если с ней что-то еще написано
                    conv(requirements)
            except ValueError: #защита от идиота
                print("Ты точно ввел нужное?")
            except KeyboardInterrupt:
                sys.exit()
        
        case "victors":
            try:
                if auto == 7: #если только команда
                    com = input(">>")
                    Victors(com)
                else: #если с ней что-то еще написано
                    Victors(requirements)
            except ValueError: #защита от идиота
                print("Ты точно ввел нужное?")
            except KeyboardInterrupt:
                sys.exit()
        
        case "info.lvl":
            try:
                if auto == 8: #если только команда
                    com = input(">>")
                    infolvl(com)
                else: #если с ней что-то еще написано
                    infolvl(requirements)
            except ValueError: #защита от идиота
                print("Ты точно ввел нужное?")
            except KeyboardInterrupt:
                sys.exit()        
        
        case "add.lvl":
            addlvl()
        
        case "add.vict":
            try:
                plar = input("Какой игрок?>")
                lvl = input("Какой лвл?>")
                pp = input("Сколько пп?>")
            except KeyboardInterrupt:
                sys.exit()
            addvict(plar,lvl,pp)
        
        case "delete.db":
            antidelete = random.randint(1000,9999)
            try:
                com = input("Вы уверенны??(напишите в ответ>" + str(antidelete) + ") >" )
            except KeyboardInterrupt:
                sys.exit()
            if int(com) == antidelete:
                shutil.rmtree("Base")
                print("Датабаза удаленна")
            else:
                print("Неправильно!")
        
        case "create.db":
            createdb()
        
        case "add.pla":
            try:
                if auto == 7: #если только команда
                    com = input(">>")
                    addpla(com)
                else: #если с ней что-то еще написано
                    addpla(requirements)
            except ValueError: #защита от идиота
                print("Ты точно ввел нужное?")
            except KeyboardInterrupt:
                sys.exit()
        
        case "info.pla":
            try:
                if auto == 8: #если только команда
                    infopla("0")
                else: #если с ней что-то еще написано                    
                    infopla(requirements)
            except ValueError: #защита от идиота
                print("Ты точно ввел нужное?")
            except KeyboardInterrupt:
                sys.exit()           
        
        case "load.db":
            loaddb()
        case "save.db":
            savedb()
        
        case "balcal":
            try:
                if auto == 6: #если только команда
                    com = input(">>")
                    balanceKZ(TPS,com,"0")
                else: #если с ней что-то еще написано
                    balanceKZ(TPS,requirements,"0")
            except ValueError: #защита от идиота
                print("Ты точно ввел нужное?")
            except KeyboardInterrupt:
                sys.exit()
        case "dev":
            print("Главный - Prosto_Maksim - https://youtube.com/@Prosto_Maksim\n")
            print("Спасибо - SpaceKZ за идею и за (balcal) - https://www.youtube.com/@spaceKZ1\n")
            print("Лицензия - GNU GPL v3 - https://www.gnu.org/licenses/quick-guide-gplv3.ru.html")
        