import sys, re, os, shutil, random, zipfile, statistics, math
if os.name != "nt": #уже давно не поверял под линукс так-что поставил это
    print("ALTA не проверяется под linux и других системах")
    print("Если она вылетает то пишите ко мне Prosto_Maksim")
    input("Enter - для продолжения...")
def clear(mode): #Ну даже не знаю??? что это делает??? :D
    os.system('cls' if os.name == 'nt' else 'clear') 
    if mode != "0": #Если не авто чистка, то показать версию.
        print("Версия ALTA V5.2_2 от Prosto_Maksim")
print("Загрузка.    1/26")

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
    
    print("Игрок:" + file.readline().rstrip('\n')) #Показывает какой игрок
    
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
print("Загрузка..   2/26")

def lvlcal(fps,Timings,seting):
    Referencepoint = 40000
    Сounter = 0 #Сетчик таймингов
    HardestC = 99999999 #Сетчик самого сложного тайминга
    Mior = 0 #ср тайминг
    FreeC = 0
    point = 0
    Compression = 216
    Mior = 0
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
    Timings = str(Timings)
    for Timing in Timings.split(";"): #Делаем масив по ; и сразу заходим в цикл for
        try:
            mc = 1000 / (int(fps) / int(Timing)) #считает время тайминга
        except ZeroDivisionError:
            print("Лвл не проходим!")
            return 0
        except ValueError:
            print("Это точно тайминги?")
            return 0
        if mc <= 40:
            point = point + (Referencepoint / (mc/1.05)) #считаем баллы за время тайминга
        elif mc >= 41 and mc <= 60:
            point = point + (Referencepoint / (mc * 1.05))
        elif mc >= 60 and mc <= 65:
            point = point + (Referencepoint / (mc * 1.1))
        elif mc >= 65 and mc <= 70:
            point = point + (Referencepoint / (mc * 1.4))
        elif mc >= 70 and mc <= 100:
            point = point + (Referencepoint / (mc * 2.5))
        elif mc >= 100 and mc <= 150:
            point = point + (Referencepoint / (mc * 3.5))        
        else:
            point = point + (Referencepoint / (mc * (mc / 9)))
        if int(Timing) < int(HardestC): #Если тайминг сложнее старого, то он записывается
            HardestC = Timing
        
        if int(Timing) > int(FreeC): #Если тайминг легче старого, то он записывается
            FreeC = Timing
        
        Сounter = Сounter + 1 #сетчик таймингов
        Mior = Mior + int(Timing)
    result = point / Compression
    Mior = Mior / Сounter #Сумма таймингов на сумму кликов
    if seting != "2":
        print("\nВерсия ALTA V5.2_2 от Prosto_Maksim")
        print("Тайминги уровня:" + str(Timings) + "\nВсего таймингов:" + str(Сounter))
        print("Фпс измерения:" + str(fps) + "\n")
        print("Самый сложный тайминг:" + str(HardestC)+"кадр")
        print("Средний тайминг:" + str(Mior)+"кадр")
        print("Самый простой тайминг:" + str(FreeC)+"кадр\n")
    if seting == "1": #Вывод баланса
        balanceKZ(fps,Timings,"1")
    if seting != "2":
        print("pp:" + str(round(result, 1)) + "\n")
    return str(round(result, 1))

clear("0")
print("Загрузка...   3/26")

def debuglvlcal(): #создано чисто для проверки(не для обычного юзера)
    data = ''
    frame = 1    
    while 1 == 1:
        data = data + lvlcal("240",frame, "2") + "," 
        if frame == 40:
            return data
        frame = frame + 1

clear("0")
print("Загрузка...   4/26")

def settingfiles(mode, typE, Number): #Отвечает за сохранения настроек в файл. ГОВНО КОД потом перепишу!
    
    def reset(fist): #сброс файла
        if fist != "1": #ругатся если это был не первый запуск)
            print("Ошибка чтения файла настроек")
            print("Выполнен его сброс")
            print("Ошибка была по:" + str(typE))
            input()
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
print("Загрузка.     5/26")

def conv(Timings): #Ну... просто ; среть и все)
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
print("Загрузка..    6/26")

def Victors(lvl):
    try:
        files = os.listdir("Base") #В скобаках какой папке база.
    except FileNotFoundError:
        print("Датабаза не найдена")
        return 0
    all = []
    altapl = list(filter(lambda x: x.endswith('.altapl'), files)) #фильтр форматов(altapl - для игроков юзается)
    print("Лвл:" + str(lvl))
    print("Имеют его>", end=" ")
    
    for file in altapl:
        Scan = 1
        data = open("Base/" + file, 'r')
        while Scan != "0":
            Scan = data.readline().rstrip('\n')
            Scan = Scan.split(":")[0]
            if Scan.lower() == lvl.lower():
                print(file.split(".altapl")[0] + ",", end=" ") #Вывод всех у кого есть лвл в пройденных
                all.append(file.split(".altapl")[0])
    print("\n")
    return all

clear("0")
print("Загрузка...   7/26")

standard = settingfiles("read","fps",1) #фпс по умолчанию
autoclear = settingfiles("read", "clear", 1) #какой режим чистки
KZbalance = settingfiles("read", "lvlbanace", 1)
TPS = int(standard) #Переносится стандартный фпс в переменную где с ним будут работать.

clear("0")
print("Загрузка.     8/26")

def addlvl():

    try:
        print("Название лвла") #Это почти как заглушка, потом будет что-то нормальное)
        com1 = input(">")
        print("Автор(ы) лвла")
        com2 = input(">")
        print("Верификатор лвла(если нет, то - ?)")
        com3 = input(">")
        print("Тайминги лвла")
        com4 = input(">")
        print("FPS")
        com5 = input(">")
        print("idlvlvl:")
        com6 = input(">")
        pp = lvlcal(com5,com4,"2")
        if pp == 0:
            return 0
        fan = balanceKZ(int(com5),com4,"2")
    except KeyboardInterrupt:
        sys.exit()
    
    scan = 0
    try:
        data = open("Base/lvldatabase.altalvl", 'r')
    except FileNotFoundError:
        print("Датабаза не найдена")
        return 0
    while scan == 0:
        lvlscan = data.readline().rstrip('\n')
        if lvlscan.lower() == com1.lower():
            print("Он уже в базе")
            return 0
        if lvlscan == "":
            scan = 1
    data.close()
    try:
        data = open("Base/lvldatabase.altalvl", 'a')
    except FileNotFoundError:
        return 0
    data.write("" + str(com1.lower()))
    data.write("\nAuthor(S):" + str(com2.lower()))
    data.write("\nVerification:" + str(com3.lower()))
    data.write("\nTimings:" + str(com4.lower()))
    data.write("\nFPS:" + str(com5.lower()))
    data.write("\nbalance:" + str(fan.lower()))
    data.write("\nPP:" + str(pp.lower()))
    data.write("\nidlvlvl:" + str(com6.lower()))
    data.write("\nend\n")
    data.close()

clear("0")
print("Загрузка..    9/26")

def infolvl(lvl,setmode):
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
                lvlinfo = data.readline().rstrip('\n').lower()
                if setmode == "1":
                    print(lvlinfo)
                if info == 0:
                    return lvlinfo.split(":")[-1]
                scan = 1
                good = 1
        if lvlscan == "":
            scan = 1
    
    if good == 0:
        if setmode == "1":
            print("лвл не Найден в базе")
        return 0
    data.close()

clear("0")
print("Загрузка...   10/26")

def addvict(Player,lvld): #Дает добавить лвл игроку
    try:
        pp = float(infolvl(lvld, "0"))
    except ValueError:
        print("Точно вел пп?")
        return 0
    if pp == 0:
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
    for scan in lvl:
        if scan.split(":")[0] == lvld:
            print("У него уже он пройден")
            return 0
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
print("Загрузка.     11/26")

def createdb():
    files = os.listdir() #Проверка на наличие уже датабазы
    for scan in files:
        if scan == "Base": #если есть то -
            antidelete = random.randint(1000,9999)
            try:
                com = input("Вы уверенны удалить старую базу??(напишите в ответ>" + str(antidelete) + ") >" )
            except KeyboardInterrupt:
                sys.exit()
            if com == str(antidelete):
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
print("Загрузка..    12/26")

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
print("Загрузка...   13/26")

def loaddb():
    files = os.listdir() #Проверка на наличие уже датабазы
    for scan in files:
        if scan == "Base": #если есть то -
            antidelete = random.randint(1000,9999)
            try:
                com = input("Вы уверенны удалить старую базу??(напишите в ответ>" + str(antidelete) + ") >" )
            except KeyboardInterrupt:
                sys.exit()
            if com == str(antidelete):
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
print("Загрузка...   14/26")

def savedb():
    try:
        name = input("Название>")
        folder = input("Куда создать?(путь до любой папки)>").replace('"', '')
    except KeyboardInterrupt:
        sys.exit()
    zip = zipfile.ZipFile(name +".zip", "w") #Создает архив
    try:
        zip.write("Base") #Создает папку в нем
    except FileNotFoundError:
        print("Датабаза не найдена")
        return 0
    files = os.listdir("Base/") #Смотрит что у вас в базе
    
    for scan in files: #Смотрит что у вас в базе
        zip.write("Base/" + scan) #что нашел в ахрив
    
    zip.close() #закрывает ахрив
    shutil.copyfile(name + ".zip", folder + "/"+ name + ".zip") #копирует куда нужно
    os.remove(name + ".zip") #Удалает уже ненужный ахрив
    print("Датабаза сохранена!")

clear("0")
print("Загрузка.     15/26")

def infopla(pla):
    if pla == "0":
        try:
            files = os.listdir("Base/") #ищет в базе игроков
        except FileNotFoundError:
            print("Датабаза не найдена")
            return 0
        print("Все игроки в базе")
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
def plalvlcomm(requirements): #Для безопастности вынес это как функцию
            if requirements == "-l": #если лвл
                alllvl = scanallvl() #Получает все лвла
                print("Топ всех лвлов>")
                pplvl = []
                for lvl in alllvl:
                    pplvl.append(infolvl(lvl,"1")) #Получает пп
                top(alllvl,pplvl) #Делает топ
            
            if requirements == "-ver": #если лвл
                alllvl = scanallvl() #Получает все лвла
                safelllvl = scanallvl()
                print(safelllvl)
                print("Топ верифнутых лвлов>")
                pplvl = []
                for lvl in safelllvl:
                    if scanerpla(lvl, '2') != "?":
                        pplvl.append(infolvl(lvl,"1")) #Получает пп
                    else:
                        alllvl.remove(lvl)
                try:
                    print(alllvl,pplvl)
                    top(alllvl,pplvl) #Делает топ
                except IndexError:
                    print("А их нет :/")
            if requirements == "-p":
                Ramdonmane = os.listdir("Base/") #ищет в базе игроков
                Ramdonmane = filter(lambda x: x.endswith('.altapl'), Ramdonmane)
                print("Топ игроков>")
                pplvl = []
                alllvl = []
                for plaer in Ramdonmane:
                    wfr = plaer.split(".altapl")
                    alllvl.append(wfr[0])
                    pplvl.append(round(tophelper(plaer)[0])) #Получает пп
                top(alllvl,pplvl)#Делает топ

clear("0")
print("Загрузка..     16/26")

def tophelper(plaer):
        
        hardest = 1 #по название доложно понятно быть)
        folder = "base/" + plaer.replace('"', '')
        file = open(folder, 'r')
        pp = 0
        Scan = 1
        plarr = []
        pparr = []
        plarr.append(file.readline().rstrip('\n')) #Показывает какой игрок
    
        while Scan == 1:
            pp1 = re.findall(r'\d+', file.readline().rstrip(' ').rstrip('\n').rstrip(':'))
    
            lvl = int(pp1[-1]) #для удобства (чтоб не по сто раз писать [0]) + все таки я написал -1 и теперь можно и арабские цифрами позоваться
    
            if lvl != 0:
                pp = pp + lvl * 0.85**(hardest-1) #Формула расчета пп
                hardest = hardest + 1
    
            if lvl == 0:
                Scan = 0
                pparr.append(pp)
        return pparr
clear("0")
print("Загрузка...    17/26")

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
            try: #Баг фикс от меня '.'
                score=score+1-(((2*math.pi)**(statistics.mode(list)/int(k)))/fps)
            except OverflowError: #.
                score = 0 #.
                break #.
        elif k > statistics.mode(list):
            try: #.
                score=score+1-(((2*math.pi)**(int(k)/statistics.mode(list)))/fps)
            except OverflowError: #.
                score = 0 #.
                break #.
    points = score/len(list)*10
    if points < 0:
        points=0
    if lvlcalmode != "2":
        if lvlcalmode != "1":
            print('Ср тайминг:',str(round(statistics.mean(list),2)),'кадр')
        print('Баланс:',str(round(points,2))+'/10')
    return str(round(points,2))+'/10'

clear("0")
print("Загрузка.      18/26")

def scanpplvl(lvl):
    pp = lvlcal(scanerpla(lvl,"4"),scanerpla(lvl,"3"),"2")
    lvlcha(lvl,"5", pp)
    lvlcha(lvl,"4", str(balanceKZ(int(scanerpla(lvl,"4")),str(scanerpla(lvl,"3")),"2")))

    allvict = Victors(lvl)
    for plar in allvict:
        deleteplalvl(plar,lvl)
        addvict(plar,lvl)

clear("0")
print("Загрузка..     19/26")

def deleteplalvl(pla, lvl): #Дает удалить пройденный лвл у игрока
    pla = pla + ".altapl"
    
    try:
        data = open("Base/" + pla, 'r')
    except FileNotFoundError:
        print("такого игрока нет в датабазе или самой датабазы")
        return 0
    
    name = data.readline()
    lvlset = data.readlines()
    coutler = 0
    ok = 1
    antiass = 0
    
    while  ok == 1:
        for scan in lvlset:
            if scan.split(":")[0] == lvl:
                ok = coutler * 10
                antiass = 1
            coutler = coutler + 1
            if scan == "0" and antiass == 0:
                print("Этого лвла у него нет")
                return 0
    
    ok = ok / 10
    data.close()
    data = open("Base/" + pla, 'w')
    data.write(name)
    delet = 0
    
    for delete in lvlset:
        if delet != ok:
            data.write(delete)
        delet = delet + 1

clear("0")
print("Загрузка...    20/26")

def lvlcha(lvl,type,nyper): #дает менять данные в базе о лвле
    
    types = ["Author(S):","Verification:","Timings:","FPS:","balance:","PP:","idlvlvl:"]
    data = open("Base/lvldatabase.altalvl", 'r')
    lvls = data.readlines()
    data.close()
    data = open("Base/lvldatabase.altalvl", 'w')
    ok = 0
    cout = type
    
    for dated in lvls:
        if ok == 1:
            cout = int(cout) - 1
        if cout != 100:
            if dated.split("\n")[0] != lvl and cout != 0:
                data.write(dated)
            else: #находит лвл и..
                data.write(dated)
                ok = 1
        else:
            cout = 101
        if cout == 0:
            data.write(str(types[int(type)]) + str(nyper) + "\n") #..и записывет новые данные
            ok = 0
            cout = 100
    data.close()

clear("0")
print("Загрузка.      21/26")

def scanerpla(lvl,type):
    
    data = open("Base/lvldatabase.altalvl", 'r')
    lvls = data.readlines()
    data.close()
    cout = 0

    while lvls != "":
        try:
            if lvls[cout].split("\n")[0] == lvl:
                dl = lvls[cout + int(type)].split(":")[-1]
                return dl.rstrip('\n')
        except IndexError:
            return 0
        cout = cout + 1

clear("0")
print("Загрузка..     22/26")

def top(data,pp): #Делает топ
    datapp = ([])
    cont = 0
    for d in data:
        pp1 = float(pp[cont])
        datapp.append((d,pp1))
        cont = cont + 1
    datapp = sorted(datapp, key=lambda datapp: datapp[-1], reverse=True)
    cont = 1
    for printtop in datapp:
        if printtop[1] != 0:
            print("Топ-" + str(cont))
            print(" " + str(printtop[0]))
            print(" pp:" + str(printtop[1]) + '\n')
        cont = cont + 1

clear("0")
print("Загрузка...    23/26")

def scanallvl(): #Ищет все лвла
    
    data = open("Base/lvldatabase.altalvl", 'r')
    lvls = data.readlines()
    lvls.append("")
    data.close()
    scan = "0"
    cout = 0
    alllvl = []
    alllvl.append(lvls[0].rstrip("\n"))
    while scan != "":
        if (cout % 9) == 0: #если что-то хочу добавить в дб!!!
            alllvl.append(scan.rstrip("\n"))
        cout = cout + 1
        scan = lvls[cout]
    return alllvl

clear("0")
print("Загрузка...    24/26")

def freme(fps,Timings): #считает не точно но пойдет)
    Сounter = 0
    Counter2fp = 0
    Counter3fp = 0
    Fremere = [0,0,0]

    Timings = Timings.split('-')
    if len(Timings) == 1:
        Timings = str(Timings[0])

    elif Timings[1] == "l":  # если -l
        
        Timings = str(Timings[0]) #чистить название лвл от -l 
        if len(Timings) == 0:
            print("Ты точно ввел уровень?")
            return 0
        Lvl = Timings.rstrip(Timings[-1])
        
        oldTimings = Timings
        Timings = scanerpla(Lvl,"3") #Ищет тайминги в датабазе
        if Timings == 0:
            print("Уровень - " + oldTimings + "<не найден>")
            return 0    
    elif Timings:
        print("Ты точно ввел нужное?")
        return 0
    for T in Timings.split(";"):
        Сounter = Сounter + 1
        T = int(T)
        
        if T == 1: #первый фп(например 240фп)
            Fremere[0] = Fremere[0] + 1
        
        elif T == 2 or T == 3: #Второй фп(например 120фп)
            if T == 2:
                Fremere[1] = Fremere[1] + 1
            elif T == 3:
                if Counter2fp <= 1:
                    Fremere[1] = Fremere[1] + 1
                Counter2fp = Counter2fp + 1 #попытка эмулировать разные кадры))
                if Counter2fp >= 13:
                    Counter2fp = 0
        
        elif T >= 4 and T <= 5: #Третий фп(например 60фп)
            if T == 4:
                Fremere[2] = Fremere[2] + 1
            elif T == 5:
                if Counter3fp <= 2:
                    Fremere[2] = Fremere[2] + 1
                Counter3fp = Counter3fp + 1 #попытка эмулировать разные кадры))
                if Counter3fp >= 4:
                    Counter3fp = 0                
    print("\nВерсия ALTA V5.2_2 от Prosto_Maksim")
    print("Тайминги уровня:" + str(Timings) + "\nВсего таймингов:" + str(Сounter))
    print("Фпс измерения:" + str(fps) + "\n")
    print(str(fps) +" fps фреймы:"+ str(Fremere[0]))
    print(str(int(fps)/2) +" fps фреймы:"+ str(Fremere[1])+" +-")
    print(str(int(fps)/4) +" fps фреймы:"+ str(Fremere[2])+" +-")
clear("0")
print("Загрузка...    24/26")
def verdbtest(): #Сигналка на случай неправильной дб
    types = ["Author(S):","Verification:","Timings:","FPS:","balance:","PP:","idlvl:","end"]
    try:
        data = open("Base/lvldatabase.altalvl", 'r')
    except FileNotFoundError:
        return 0
    data.readline()
    count = 0
    while 1 == 1:
        datas = ""
        ttpyes = ""
        datas = data.readline()
        test = ''.join(datas.split(":")[0])
        test = test.split("\n")
        ttpyes = str("".join(types[count].split(":")[0].split("\n")))
        if test[0] != ttpyes:
            print(test[0], ttpyes)
            print("Внимание версия ващей дб НЕ подерживается!!!!!")
            print("Любые действия с ней скорее всего ее уничтожать!!!!")
            print("Я советую если хотите с ней работать написать команду 'convdb'")
            data.close()
            input("enter для продолжения>")
            return 1
        if test[0] == ttpyes == "end":
            data.close()
            return 2
        count = count + 1
verdbtest()
clear("0")
print("Загрузка...    25/26")

def convdb():
    data = open("Base/lvldatabase.altalvl", 'r')
    db = data.read()
    dblist = db.split("\n")
    endreal = 0
    countw = 0
    count = 0 
    data.close()
    while countw == 0:
        if dblist[count] == "end":
            countw = count
        count = count + 1
    if countw >= 9:
        print("дб новее чем алта, обнови алту!!!!!")
        return 9
    if countw == 8:
        print("дб уже текущей версии!")
        return 8
    if countw == 7:
        print("Обновление дб")
        data = open("Base/lvldatabase.altalvl", 'w')
        for dd in dblist:
            if dd == "end":
                data.write("idlvlvl:?\n")
            if dd != "":
                data.write(dd + "\n")
        print("Успешно!")
        data.close()
        return 7
clear("0")
print("Загрузка...    26/26")

clear("0")
print("Версия ALTA V5.2_2 от Prosto_Maksim")
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
            match requirements:
                case "help":
                    print(" Для посмотра всех команд водите help 'число' \n1 - Основные команды \n2 - Команды для Датабазы \n3 - Доп")
                    print(" Для помощи о конкретной комадны ведите так help 'нужная комадна'")
                case "1":
                    print(" Основные команды:")
                    print("  fps - меняет фпс расчета pp")
                    print("  fps.set - фпс который будет при запуске")
                    print("  Placal - измерение сумарного pp игрока по файлу")
                    print("  lvlcal - измерение пп лвла")
                    print("  balcal - измерение баланса лвла(от SpaceKZ)")
                case "2":
                    print(" Для датабазы:")
                    print("  add.pla - добавить игрока в датабазу")
                    print("  info.pla - Список игроков(если написать ник, то будет работать как placal)")
                    print("  victors - Ищет всех викторов нужного лвла")
                    print("  add.vict - добавить игроку пройденный лвл")
                    print("  del.vict - Удалить пройденный лвл у игрока")
                    print("  add.lvl - добавить лвл в датабазу")
                    print("  info.lvl - поиск и инфа о лвле")
                    print("  chatim - изменить тайминги у лвла(автоматом пересчитает и для игроков)")
                    print("  chaver - изменить верификатора(добавить/удалить) у лвла")
                    print("  rebal - повторно пересчитать ВСЮ ДАТАБАЗУ(если обновилась система пп)")
                    print("  top (-p = игроков) (-l = всех лвлов) (-ver топ верифнутых лвлов)")
                    print("  load.db - Загружить датабазу")
                    print("  save.db - Сохранить датабазу")
                    print("  create.db - создать новую датабазу(Удалить если она была)")
                    print("  delete.db - Просто удалить установленную датабазу")
                    print("  chaid - дает поменять id у лвла")
                    print("  convdb - конвертирует дб до текущей версии.")
                    print("!Внимание виктор и верифер не как сами не свазываются! если кто-то верифнул лвл, добавьте отдельно как верифер и как виктор!")
                case "3":
                    print(" Доп:")
                    print("  conv - конвертер c старого формата 12354 в новый формат 1;2;3;5;4 таймингов")
                    print("  clear - очистить комадную строку")
                    print("  clear.auto - оставляет в командной строке только последнюю команду")
                    print("  lvlcal.bal - встраивает в измерения lvlcal и balcal")
                    print("  exit - выйди из проги(можно юзать Ctrl + C )")
                    print("  dev - список всех кто принимал участие и так-далее")
                    print("  frep - примерное измерение фрейм перфектов")
                case "fps":
                    print("Команда FPS - для изменения фпса расчета пп")
                    print("  Еще при пропуска фпса в chatim будет фпс который вы указали в fps")
                    print("  Если написать фпс '0' то фпс будет сброшен по fps.set")
                case "fps.set":
                    print("Команда fps.set - стоковый фпс который будет выбиратся при запуске")
                    print("  Если написать фпс '0' то будет сохранятся 240")
                case "placal":
                    print("Комадна placal - считает сумарный пп у игрока по файлу")
                    print("  Для работы надо перекинуть в консоль файл и нажать ENTER")
                    print("  Файл должен иметь правильный формат -< ")
                    print("  Ник игрока")
                    print("  ЛВЛ(его хардест):пп(сколько выдало lvlcal)")
                    print("  ЛВЛ(его предхардест):пп(сколько выдало lvlcal)")
                    print("  и так далее")
                    print("  0 - в конце  >")
                    print("  % это солько всего дали от пп")
                    print("  The cube challenge 1:500пп 85% == 500пп*0.85%=425пп(425 сколько дали ему)")
                case "lvlcal":
                  print("Комадна lvlcal для измерения сложности лвла по пп")
                  print("   Для измерения нужно иметь гд с FrameStep и фпс байпасс(физикс байпасс в 2.2)")
                  print("   Ставим фпс(в gd и в alta(комадна fps)) на котором будуте мерить(тем больше фпс тем точнее(но дольше будет замер))")
                  print("   Дальше начинаем замерать сколько каждый тайминг имеет кадров для пролета и записывать его через ;")
                  print("   После замеров у вас будет примерно вот-это 4;7;3;6;2;10;1;2")
                  print("   После жмем Enter и получаем результат")
                case "balcal":
                    print("Комадна balcal для измерения баланса лвла")
                    print("  Измерается так-же как и lvlcal")
                    print("-  -  -  -  -  -")
                    print(" Для измерения нужно иметь гд с FrameStep и фпс байпасс(физикс байпасс в 2.2)")
                    print(" Ставим фпс(в gd и в alta(комадна fps)) на котором будуте мерить")
                    print(" Дальше начинаем замерать сколько каждый тайминг имеет кадров для пролета и записывать его через ;")
                    print(" После замеров у вас будет примерно вот-это 4;7;3;6;2;10;1;2")
                    print(" После жмем Enter и получаем результат")
                    print("-  -  -  -  -  -")
                case "frep":
                    print("Комадна frep для измерения количества фреймов в лвле")
                    print("  Измерается так-же как и lvlcal")
                    print("-  -  -  -  -  -")
                    print(" Для измерения нужно иметь гд с FrameStep и фпс байпасс(физикс байпасс в 2.2)")
                    print(" Ставим фпс(в gd и в alta(комадна fps)) на котором будуте мерить")
                    print(" Дальше начинаем замерать сколько каждый тайминг имеет кадров для пролета и записывать его через ;")
                    print(" После замеров у вас будет примерно вот-это 4;7;3;6;2;10;1;2")
                    print(" После жмем Enter и получаем результат")
                    print("-  -  -  -  -  -")
                    print("А если у вас лвл уже есть в датабазе то")
                    print("/frep (уровень) -l")
                    print("-l = lvl, тоесь поиск в датабазе по названию")                    
                case "add.pla":
                    print("Команда add.pla добавляет в датабазу игрока.\nПосле этого с ним можно будет работать")
                case "info.pla":
                    print("Комадна info.pla, при пустом вводе показывает всех кто датабазе")
                    print(" Если дописать ник, то будет работать как примерно placal")
                case "victors":
                    print("Комадна victors 'лвл' - показывает всех викторов лвла в базе, без порядка")
                case "add.vict":
                    print("Комадна add.vict - добавлает игроку пройденный лвл")
                    print("  Для этого водим")
                    print("  1 - Ник виктора в базе")
                    print("  2 - Пройденный лвл (он должен быть в базе)")
                case "del.vict":
                    print("Комадна del.vict - удалает игроку пройденный лвл")
                    print("  Для этого водим")
                    print("  1 - Ник виктора в базе")
                    print("  2 - Пройденный лвл")
                case "add.lvl":
                    print("Команда add.lvl - добавляет лвл в базу")
                    print("  Для этого водим")
                    print("  1 - Название лвла")
                    print("  2 - Автора(ы) или хоста(ов) лвла")
                    print("  3 - Ник верификатора лвла")
                    print("  4 - Тайминги который получились после замера лвла, тоесь например'2;3;6;3;7;4;3;7")
                    print("  5 - Фпс на которым вы замеряли")
                case "info.lvl":
                    print("Команда info.lvl 'Искомый лвл' - показывает основные данные об лвле")
                case "chatim":
                    print("Команда chatim - дает изменить тайминги у лвла в базе")
                    print("И автоматом меняет у всех викторов пп за него")
                    print(" Для этого водим")
                    print("  1 - Название лвла")
                    print("  2 - фпс(если вести 0 то будет выбиратся который поставленный в fps или fps.set)")
                    print("  3 - Тайминги")
                case "chaver":
                    print("Команда chaver - дает изменить верифера у лвла в базе")
                    print(" Для этого водим")
                    print("  1 - Название лвла")
                    print("  2 - Верифера(если убрать - '?')")
                case "rebal":
                    print("Команда rebal - служить для быстрого пересчета при изменения пп системы")
                    print("  Пересчитывает все лвл и перечисляет пп игрокам")
                case "top":
                    print("Команда top -l(все лвла),-ver(все верифнутые лвла), -p(игроки) - Сортирует игроков или лвла по пп и делает топ")
                case "load.db":
                    print("Команда load.db - дает загружить датабазу из файла(zip)")
                    print("  Для Загрузки он удалить старую базу(для защиты он попросить вести капчу)")
                    print("  После этого он попросить кинуть в окно программы файл датабазы(zip)")
                    print("  И он загружить ее")
                case "save.db":
                    print("Комадна save.db - дает сохранить базу, чтоб потом можно было загружить через load.db")
                    print(" Для сохранения надо")
                    print("  1 - Назвать датабазу")
                    print("  2 - Назвать датабазу")
                    print("  3 - Путь куда ее сохранить(можно кинуть в окно нужную папку)")
                case "create.db":
                    print("Команда create.db - создает датабазу(если ее нет) или очисить(если она то этого была)")
                    print("Если она была - то она попросить вести капчу")
                case "delete.db":
                    print("Комадна delete.db - удалить датабазу(попросить вести капчу)")
                case "conv":
                    print("conv - Если у вас остались тайминги от старых версий ALTA, где тайминги были максимум до 9 кадров")
                case "clear":
                    print("Чистить консоль")
                case "clear.auto":
                    print("Чистить после каждой команды(это настройка сохраняется даже после перезапуска ALTA)")
                case "lvlcal.bal":
                    print("встраивает в измерения lvlcal и balcal(это настройка сохраняется даже после перезапуска ALTA)")
                case "exit":
                    print("выйди из проги(можно юзать Ctrl + C )")
                case "dev":
                    print("О разработчиках ALTA и помощников")
                case "chaid":
                    print("Дает помеять id лвла")
                    print("для этого водим")
                    print("1 - Название лвла")
                    print("2 - id(если убрать - '?')")
                case "convdb":
                    print("convdb - конвертирует дб до текущей версии.")
                    print(" Для конвертации тупо напишите ее и все!")
                    print(" ЕСЛИ ДБ НОВЕЕ АЛТЫ то оно не сможет конвертнуть!")
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
                    infolvl(com, "1")
                else: #если с ней что-то еще написано
                    infolvl(requirements, "1")
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
            except KeyboardInterrupt:
                sys.exit()
            addvict(plar.lower(),lvl.lower())
        
        case "delete.db":
            antidelete = random.randint(1000,9999)
            try:
                com = input("Вы уверенны??(напишите в ответ>" + str(antidelete) + ") >" )
            except KeyboardInterrupt:
                sys.exit()
            if com == str(antidelete):
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
        case "frep":
            try:
                if auto == 4: #если только команда
                    com = input(">>")
                    freme(TPS,com)
                else: #если с ней что-то еще написано
                    freme(TPS,requirements)
            except ValueError: #защита от идиота
                print("Ты точно ввел нужное?")
            except KeyboardInterrupt:
                sys.exit()        
        case "del.vict":
            com = input("У кого?>")
            com2 = input("Какой лвл?>")
            deleteplalvl(com.lower(),com2.lower())
        
        case "chatim":
            com = input("Какой лвл?>").lower()
            com3 = input("Какой фпс?(0 если обычный)")
            if com3 == "0" or com3 == "": #Если ничего то обычный фпс
                com3 = TPS
            com2 = input("Какие тайминги?>")
            try:
                lvlcha(com,"2",com2)
                lvlcha(com,"3",com3)
                scanpplvl(com)
            except FileNotFoundError:
                print("Датабаза не найдена")
        
        case "chaver":
            com = input("Какой лвл?>").lower()
            com3 = input("Кто верифер?(знак ? чтоб убрать)>")
            try:
                lvlcha(com, "1", com3)
            except FileNotFoundError:
             print("Датабаза не найдена")   
        case "rebal":
            try:
                com = scanallvl()
            except FileNotFoundError:
                    print("Датабаза не найдена")            
            
            for lvl in com:
                if lvl != "0":
                    try:
                        scanpplvl(lvl)
                    except FileNotFoundError:
                        print
        case "chaid":
            com = input("Какой лвл?>").lower()
            com3 = input("Новый id( '?' - если приватный)>")
            try:
                lvlcha(com, "6", com3)
            except FileNotFoundError:
             print("Датабаза не найдена")   
        case "convdb":
            convdb()        
        case "top":
            try:
                plalvlcomm(requirements)
            except FileNotFoundError:
                print("Датабаза не найдена")
        case "dev":
            print("Главный - Prosto_Maksim - https://youtube.com/@Prosto_Maksim\n")
            print("Спасибо - SpaceKZ за идею и за (balcal) - https://www.youtube.com/@spaceKZ1\n")
            print("Лицензия - GNU GPL v3 - https://www.gnu.org/licenses/quick-guide-gplv3.ru.html")
        case "debug.1":
            print(debuglvlcal()[:-1])
        