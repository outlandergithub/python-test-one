from collections import namedtuple
from timeit import default_timer, timeit
from datetime import datetime
import re
import json

if __name__ == '__main__':
    print("First output from function.py file, printed only if run from functions.py directly")

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

def c1a(*args, **kwargs):
    print(args, kwargs)

c1a(1, 2, 3, x = True, y = "Text")

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

def d4a(a, b, *args):
    print(a, b, args)

d4a(*[1, 2, 3, 4], 5)    #*[1, 2, 3, 4] list кожен елемент міг попасти в окрему позиційну змінну. Іменованих позиційних лише дві "a", "b", вказано args без *
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
replaced = re.sub('[Eeng]', 'a', s)
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

def list_of_integers(param:list[str])-> list[int]:
    print(list(param))
    return list(param)

list_of_integers(['one', '2', '3'])

alist:list[int] = [1, 2, 3, '4', 5] 

string = "   anakonda ana   "
string2 = string.strip()
print(string.strip())
print(string)
print(string2)

upper = "all lower"
upper2 = upper.upper()
print(upper.upper())
print(upper)
print(upper2)

one = "all lowel"
print(one.replace("l", "G"))

two = "one two three"
print(two.split())
print(list(two))
print(set(two))

three = "one, two, three , four "
print(three.strip().split(","))
print(''.join(three.split(",")))  

large_list = ['A']*1000000
start = default_timer()
#print(''.join(large_list))
print(timeit(stmt="['A']*100  ", number=1000000))
''.join(large_list)
end = default_timer()
print(end-start)

#oldstyle formatted string
pi = 3.14123
formatted = "pi value is %f" % pi

#oldstyle formatted string
pi = 3.14123
formatted = "pi value is %f" % pi
print(formatted)

#oldstyle formatted string with 2 digits=signs after decimal point in floating number
pi = 3.14123
formatted = "pi value is %.2f" % pi
print(formatted)

#oldstyle formatted string without decimal part of a floating number
pi = 3.14123
formatted = "pi rounded value is %d" % pi
print(formatted)

string = 'TEXT'
formatted = "here comes the %s" % string 
print(formatted)

#soso style formatted string with 2 digits=signs after decimal point in floating number and second positional variable
pi = 3.14123
r = 1
formatted = "pi value is {:.2f} and radius is {}".format(pi, r)
print(formatted)

#new style formatted string floating number and second positional variable
pi = 3.14123
r = 1
formatted = f"pi value is {pi} and radius is {r}"  
print(formatted)

list = [12, -2, 3, -4]
print(list)
print(list.sort()) #None
ordered = list.sort()
print(list)
print(ordered) #None
print(type(ordered)) #<class 'NoneType'>
sorted = sorted(list)
print(sorted)
#sorted2 = sorted(ordered) #error
#print(sorted2) #TypeError: 'list' object is not callable  

tuple1 = "one", 2, "three"
print(type(tuple1))

one, two, three = tuple1
print(one)
print(two)
print(three)

tuple2 = (False, 2, "string", 3.14123)

tuple3 = ("first"  )
print(type(tuple3))

Point = namedtuple('Point', 'x, y')
p = Point(4, -3)
print(p.x, p.y)

Dupa = namedtuple('Dupa', 'x, y')
d = Dupa(1, -2)
print(d.x, d.y)

person = {"name": "John Doe", "age": 22, "occupation": ["programmer", "entrepreneur"], "married": True, "children": [{"sex": "man", "name": "Rick", "age": 1, "status": "son"}, {"sex": "woman", "name": "Jinny", "age": 2, "status": "daughter"}]}
# dumps() method used to  present python data converted into json format specifically in string format
personJson = json.dumps(person, sort_keys=True, indent=4) 
print(personJson)
# loads() method used to deserialize json data presented in string format back to python object
personDictionary = json.loads(personJson)
print(personDictionary)

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def user_json_endode(self):
        if isinstance(self, User):
            return {'name': self.name, 'age': self.age, self.__class__.__name__: True}
        else:
            raise TypeError('Object is not serializable')

    def user_json_decode(self):
        if User.__name__ in self:
            return User(name=self['name'], age=self['age'])
        else:
            return self

test_user = User("Alan Wake", 42)

test_user_json = json.dumps(test_user, default=User.user_json_endode)
print(test_user_json)

from json import JSONEncoder

class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
        else:
            return JSONEncoder.default(self, o)

# usual method to encode python object to json
second_test_user = json.dumps(test_user, cls=UserEncoder)
print(second_test_user)
# usual method to decode json back to python object
deserialized_second_test_user = json.loads(second_test_user)
print(deserialized_second_test_user["name"])

# alternative method to encode python object to json
third_test_user = UserEncoder().encode(test_user)
print(third_test_user)
deserialized_third_test_user = json.loads(third_test_user)
print(deserialized_third_test_user["age"])

# alternative method to decode json back to python object
user_object = json.loads(third_test_user, object_hook=User.user_json_decode)
print(user_object.name)

def count_user_input():
    inputted = input("Enter any word: ")
#    length = len(inputted)
#   if length > 0:
#        print(f'You have entered {length} symbols')
    if (length := len(inputted)) > 0:
        print(f'You have entered {length} symbols')

def numbers_counter():
    numlist = [1, 2, 3, 4, 5]
#    length = len(numlist)
#    while length > 0:
    while (length := len(numlist)) > 0:
        print(f'{length} numbers in numlist')
        numlist.pop()
 #       length = len(numlist)

def booltest():
    if bool('') == bool(''):
        print(">>>>>>>>>>>>>>>>>>>>>>>>not equal")
    else:
        print("equal<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

def connect():
    current_datetime = datetime.now()
    print("------------ Connect function called here at "+current_datetime.strftime('%m-%d-%Y--%H-%M-%S')+" ------------")

if __name__ == '__main__':
    booltest()
    connect()
    numbers_counter()
    count_user_input()
    print("Last but one output from function.py file, printed only if run from functions.py directly")

print("Last output from function.py file")