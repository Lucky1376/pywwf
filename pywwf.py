#Filework or WWF V0.0.1
#WWF | Working with files


#Файловая Математика
def math(path, sn):
    y = 0
    try:
        path += 1
        print("\n[FileNumber] The",path,"file is a number")
        exit(0)
    except:
        y = 1
    t = 0
    try:
        a = open(path, "r")
        a.close()
        t = 1
    except:
        print("\n[FileError] Can't find the file "+path)
        exit(0)
    o = 0
    try:
        a = open(path, "r")
        l = a.read()
        a.close()
        try:
            l = int(l)
            o = 1
        except:
            print("\n[ContentError] The file does not specify a number")
            exit(0)
    except:
        exit(0)
    ss = ["+", "-", "*", "/"]
    i = 0
    if sn[0:1] not in ss:
        print("\n[SignError] Couldn't find the sign")
        exit(0)
    else:
        i = 1
    u = 0
    try:
        sn2 = sn[1:]
        sn2 = int(sn2)
        sn2 += 1
        sn2 -= 1
        u = 1
    except:
        if sn2 == "":
            print("\n[NumberError] Do not indicate the number")
            exit(0)
        else:
            print("\n[NumberError] The",sn2,"is not a number")
            exit(0)
    if y == 1 and t == 1 and u == 1 and i == 1 and o == 1:
        sign = sn[0:1]
        number = sn[1:]
        with open(path, "r") as file1:
            file2 = file1.read()
        with open(path, "w") as file1:
            if sign == "+":
                file1.write(str(int(file2)+int(number)))
            elif sign == "-":
                file1.write(str(int(file2) - int(number)))
            elif sign == "*":
                file1.write(str(int(file2) * int(number)))
            elif sign == "/":
                if int(number) == 0:
                    print("[ZeroError] You can't divide by zero")
                    exit(0)
                else:
                    file1.write(str(int(file2) / int(number)))

#Проверка наличия файла
def check(file, new):
    file = str(file)
    new = str(new)
    if new == "pass":
        try:
            a = open(file, "r")
            a.close()
            return True
        except:
            return False
    elif new == "new":
        try:
            a = open(file, "r")
            a.close()
            print("[New File Error] This file already exists")
            ecit(0)
            return False
        except:
            a = open(file, "w")
            a.close()
            return True
    else:
        print("[Arg Error] Unknown argument")
        exit(0)

#Чтение файла
def read(file):
    try:
        a = open(str(file), "r")
        a2 = str(a.read())
        a.close()
        return a2
    except:
        print("[Open Error] No such file exists")
        exit(0)

#Запись в файл
def write(file, coding, content):
    file = str(file)
    content = str(content)
    coding = str(coding)
    if coding == "a" or coding == "w":
        a = open(file, coding)
        a.write(content)
        a.close()
        return True
    else:
        print('[Coding Error] You can only use the encoding "w" and "a"')
        exit(0)

def search(file, word):
    file = str(file)
    word = str(word)
    try:
        a = open(file, "r")
        a.close
    except:
        print("[Open Error] No such file exists")
        exit(0)
    if word == "":
        print("[Content Error] The content must not be empty")
        exit(0)
    a = open(file, "r")
    a2 = str(a.read())
    a.close()
    if len(a2)<len(word):
        print("[Len(Content) Error] The file content is smaller than the text")
        exit(0)

    #Алгоритм нахождения
    spisok = []
    ab = []
    col = 0
    a = 0
    b = len(word)
    for i in range(len(a2)):
        if a2[a:b] == word:
            col += 1
            ab.append(str(a)+":"+str(b))
        a += 1
        b += 1
    if col == 0:
        return False
    else:
        spisok.append(col)
        for syb in ab:
            spisok.append(syb)
        return spisok

def remove(*files):
    import os
    if len(files) == 0:
        print("[Arg Error] Do not specify any file")
        exit(0)
    success = 0
    fail = 0
    slovar = {"Success":0, "Fail":0}
    for file in files:
        try:
            os.remove(file)
            success += 1
        except:
            fail += 1
    slovar["Success"]+=success
    slovar["Fail"]+=fail
    return slovar



