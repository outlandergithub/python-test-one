import re

def a1(a, b, c = None):
    print(a,b)

a1(1, True, 999)

def a2(a, b, c = 10):
    print(a,b)

a2(1, True, 999)

#def b0(a,b, *args):
#    print(a,b, c) #NameError: name 'c' is not defined
#
#b0(1, True, 1, 12, 2,3)

def b1(a,b, *args):
    print(a,b, args)

b1(1, True, 1, 12, 2,3)

def b2(a,b, *args):
    print(a,b, *args)

b2(1, True, 1, 12, 2,3)

def c1(*args, **kwargs):
    print(args, kwargs)

c1()

def c1(*args, **kwargs):
    print(args, kwargs)

c1(1, 2, 3, x = True, y = "Text")

def c2(*args, **kwargs):
    print(*args, *kwargs)

c2(1, 2, 3, x = True, y = "Text")

def c3(*args, **kwargs):
    print(args[1], kwargs["y"])

c3(10, 200, 3000, x = True, y = "Text")

def d1(a, b, c = True, d = False):
    print(a, b, c, d)

d1(1, 2, 3, 4)

#def d2(a, b, c = True, d = False):
#    print(a, b, c, d)
#
#d2([1, 2, 3, 4])    #TypeError: d2() missing 1 required positional argument: 'b'

def d3(a, b, c = True, d = False):
    print(a, b, c, d)

d3([1, 2, 3, 4], 5)    #[1, 2, 3, 4] list повністю попапдає в змінну "a". Цифра 5 в змінну "b"

def d4(a, b, c = True, d = False):
    print(a, b, c, d)

d4(*[1, 2, 3], 5)    #[1, 2, 3] list кожен елемент попадає в окрему позиційну змінну . 5 попадає в змінну "d"

#def d41(a, b, c = True, d = False):
#    print(a, b, c, d)
#
#d41(*[1, 2, 3, 4], 5)    #*[1, 2, 3, 4] list кожен елемент попадає в окрему позиційну змінну. TypeError: d4() takes from 2 to 4 positional arguments but 5 were given

def d4(a, b, *args):
    print(a, b, args)

d4(*[1, 2, 3, 4], 5)    #*[1, 2, 3, 4] list кожен елемент міг попасти в окрему позиційну змінну. Іменованих позиційних лише дві "a", "b", вказано args без *
                        # Тому з *[1, 2, 3, 4] перші дві цифри попали в окремі позиційні змінні. Рерша попали в tuple

def d5(a, b, *args):
    print(a, b, *args)

d5(*[1, 2, 3, 4], 5)    #*[1, 2, 3, 4] list кожен елемент міг попасти в окрему позиційну змінну. Іменованих позиційних лише дві "a", "b", вказано *args з *
                        # Тому з *[1, 2, 3, 4] перші дві цифри попали в окремі позиційні змінні. Рерша також окремо, так само як і цифра 5. 

#def d6(a, b, c = True, d = False):
#    print(a, b, c, d)
#
#d6(*[1, 2, 3], **{"c":"first", "d":"second"})   #*[1, 2, 3] list кожен елемент попадає в окрему позиційну змінну . 3 попадає в змінну "c", 
#                                                #потім з **{"c":"first", "d":"second"} "c":"first" також пробує попасти в змінну "c", тому
#                                                #TypeError: d6() got multiple values for argument 'c'

def d6(a, b, c = True, d = False):
    print(a, b, c, d)

d6(*[1, 2], **{"c":"first", "d":"second"})   #*[1, 2] list кожен елемент попадає в окрему позиційну змінну.
                                                #потім з **{"c":"first", "d":"second"} "c":"first" пробує попасти в змінну "c", і так далі

s = "Example String"
replaced = re.sub('[ES]', 'a', s)
print(replaced)

#line = re.sub(
#           r"(?i)^.*interfaceOpDataFile.*$", 
#           "interfaceOpDataFile %s" % fileIn, 
#           line
#       )

#fileIn = "Alan Wake alan wake"
#regex = re.compile(r"^.*a.*$", re.IGNORECASE)
#list = ["Alan","Wake","2sa"]
#for line in list:
#    line = regex.sub("a" % fileIn, line)
#    # do something with the updated line
#    print(line)