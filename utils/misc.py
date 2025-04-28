import datetime
import os
import re
import time
import decimal

context = decimal.getcontext()
context.rounding = decimal.ROUND_DOWN
print(context)

a = decimal.Decimal('0.3')
print(a)

current_time = datetime.datetime.now()                                                      # returns date with time with nanoseconds 2025-04-26 15:05:34.250872
string_from_time1 = datetime.datetime.strftime(current_time, '%Y-%M-%d')                    # takes 2 arguments, returns formatted date 2025-05-26
string_from_time2 = datetime.datetime.now().strftime('%Y-%M-%d')                            # takes 1 argument, returns same formatted date 2025-05-26
print(string_from_time1)
print(string_from_time2)
#string_from_time3 = datetime.datetime.now().timestamp().strftime(current_time, '%Y-%M-%D')
timespamp1 = datetime.datetime.now().timestamp()                                            # returns 1745669134.2509 seconds with nanoseconds
current_time_from_timespamp1 = datetime.datetime.fromtimestamp(timespamp1)                  # returns date with time with nanoseconds 2025-04-26 15:05:34.250872
timespamp2 = time.time()                                                                    # returns 1745669134.2509 seconds with nanoseconds
local_time = time.localtime()
UTCtime = time.gmtime()
readable_UTC_time = time.strftime("%Y-%M-%d", UTCtime)                                 # takes 2 arguments, returns formatted date 2025-05-26
print(readable_UTC_time + " readable UTC time")
# print(UTCtime)                      # time.struct_time(tm_year=2025, tm_mon=4, tm_mday=28, tm_hour=13, tm_min=55, tm_sec=38, tm_wday=0, tm_yday=118, tm_isdst=1)
readable_local_time = time.strftime("%Y-%M-%d", local_time)                                 # takes 2 arguments, returns formatted date 2025-05-26
# print(local_time)                   # time.struct_time(tm_year=2025, tm_mon=4, tm_mday=28, tm_hour=13, tm_min=55, tm_sec=38, tm_wday=0, tm_yday=118, tm_isdst=1)
print(readable_local_time + " readable_local_time")
current_time_from_timespamp2 = datetime.datetime.fromtimestamp(timespamp2)                  # returns date with time with nanoseconds 2025-04-26 15:05:34.250872
print(timespamp1)
print(timespamp2)
print(current_time)
print(current_time_from_timespamp1)
print(current_time_from_timespamp2)

print([*os.path.split('')])
print(os.path.split(''))
os.system("echo 123")
encoded = 'asdasdfas'.encode(encoding="utf-8")
print(encoded)
decoded = encoded.decode(encoding="utf-8")
print(decoded)

today = datetime.date.today()                                                               # returns date
print(today)
tomorrow = today + datetime.timedelta(days=1)                                               # returns date
print(tomorrow)

regex1 = re.compile('cool')
regex2 = re.compile(r'^.*(cool).*$')
regex3 = re.compile(r'^.*(col).*$')
list1 = ['acoola', 'cool', 'col', 'be-cool-a', 'cool2', 'cool']
list2 = ['acoola', 'cool', 'col', 'be-cool-a', 'cool2', 'cool']
list3 = ['acoola', 'cool', 'col', 'be-cool-a', 'cool2', 'cool']
matches1 = [i for i in list1 if re.match(regex1, i)]
matches2 = [i for i in list2 if re.match(regex2, i)]
matches3 = [i for i in list3 if re.match(regex3, i)]
print(matches1)
print(matches2)
print(matches3)

