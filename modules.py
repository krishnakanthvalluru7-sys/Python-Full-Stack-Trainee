#diff btw module, library and package
#modlue -
'''A module is a single python file it consisits python code.
a module contains variables, functions and classes
examples of modules such as :My-module.py-math.py-random.py'''
#package-
'''A package contains collection of modules is known as package.
ex-Requests,numpy,pandas'''
#Library-
'''it consists both modules and packages
ex-numpy,pandas,Django,matplotlib'''
#Note:every python file is a module and import is a keyword ,every python is a saved internally with variable
#name as __main__

'''def greetings(name):
    print("Welcome",name)'''

'''a=10
b=20
print("sum is ", a+b)'''

'''a=int(input("a val:"))
b=int(input("b val:"))
print(a*b)'''

'''details={"idno's":[10,20,30],"names":["hemanth","teja","lohith"],"marks":[60,40,80]}'''

'''if __name__=="__main__":
    a=[10,20,30,40]
    a.append("gnan")
    print(a)'''

'''def dummy():
    if __name__=="__main__":
        print("this program is run as script")
    else:
        print("this program is run as module")
dummy()'''

#math module
'''import math
print(math.pi)
print(math.pi*3)
print(math.sqrt(3))
print(math.pow(2,6))
print(math.log(10))
print(math.sin(90))
print(math.cos(90))
print(math.tan(45))
print(math.ceil(5.2))
print(math.ceil(9.12))
print(math.floor(6.2))'''

'''from math import pi,log,sqrt,tan
print(pi,log(4),sqrt(3),tan(90)) #pow(3,1),float(3)'''

#sys module
'''import sys
print(sys.path)

for i in sys.path:
    print(i)

print(sys.version)
'''

#OS module
'''import os
#print(os.path)
#print(os.getcwd())
#print(os.listdir())
#print(os.mkdir("oct5"))
#print(os.listdir())
#print(os.chdir("C:\\Users\\HP\\Downloads\\New folder"))
#print(os.listdir())
#print(os.getcwd())'''

#random module -> random module is used to generate random numbers in python , randint() funtion is used and
#this function is defined in ranadom module.
#sample
'''import random
a=random.sample(range(6,27),6)
print(a)'''

#randint()
'''import random
a=random.randint(6,17)
print(a)'''

#choice()
'''import random 
a=[20,30,40,60,10]
b=random.choice(a)
print(b)'''

#task -> Dice
'''while True:
    import random
    a=int(input("role the dice:"))
    a=random.randint(1,6)
    print(a)
    opt=int(input(options are :\n 1.yes\n 2.NO\n))
    if opt==1:
        continue
    else:
        break'''

#calendar
'''import calendar
year = 2025
month=12
print(calendar.month(year,month))'''

'''import calendar
year=2026
print(calendar.calendar(year))'''

'''import calendar
while True:
    a=int(input("enter the year:"))
    b=int(input("enter the month:"))
    print(calendar.month(a,b))'''

#date & time
'''from datetime import date
a=date.today()
print(a)'''

'''import datetime
a=datetime.datetime.now()
print(a)'''

'''import time
a=time.time()
print(a)  #epoch time

b=time.localtime(a)
print(b)

print(f"today date is {b.tm_mday}-{b.tm_mon}-{b.tm_year}")
print(f"today is in  {b.tm_hour}-{b.tm_min}-{b.tm_sec}")
print(f"is {b.tm_wday}-{b.tm_yday}-{b.tm_isdst}")'''


#task
'''import random
import time
for i in range(10):
    i=random.randint(1,50)
    print(i)
    time.sleep(2)'''

#regular expressions(regex)
#rege exp are powerfull tools (module)embedded in python which is mainly used to find a pattern with in a given string or statements or files and mainly use it for text manulplation.
'''a="codegnan is in vja"
print(a)

a="codegnan\nis\tin\nvja"
print(a)'''

'''a=r"codegnan\nis\tin\nvja"
print(a)'''

#compile(),search(),findall(),split(),sub()
#sequence characters
'''\w-> it  matches alphanumeric
\W-> it matches non-qlphqnumeric
\d-> it matches any didgit
\D-> it matches non-digits
\s-> it represents white spaces
\S-> it represents non-white spaces'''

#compile()
import re
'''a="code map money cash cap maths cat maths cup cat mug mat"
b=re.compile(r"m\w\w\w\w")
print(b)

#search()
c=b.search(a)
print(c)

c=re.search(r"m\w+",a)
print(c)'''

#findall
''''b=re.findall(r"m\w+",a)
print(b)

c=re.findall(r"c\w+",a)
print(c)'''

#split()
'''c=re.split(r"m",a)
print(c)

d=re.split(r"m\s",a)
print(d)'''

#sub() - replace
'''e=re.sub(r"maths","science",a)
print(e)'''

'''c="codegnan123, code456,python44"
d=re.findall(r"\d+",c)
e=re.findall(r"\d",c)
print(d)
print(e)'''
