'''a=10
b=20
print("the sum is ",a+b)
print("the diff is ", a-b)
print("the product  is", a*b)
a=100
b=200
print("the sum is ",a+b)
print("the diff is ", a-b)
print("the product  is", a*b)
a=1000
b=2000
print("the sum is ",a+b)
print("the diff is ", a-b)
print("the product  is", a*b)'''

#function calling

'''def calculate(a,b):
    print("the sum is ",a+b)
    print("the diff is ", a-b)
    print("the product  is", a*b)
calculate(10,20)
calculate(100,200)
calculate(1000,2000)'''

#//,**,%
'''def calculate(a,b):
    print("the sum is ",a+b)
    print("the diff is ", a-b)
    print("the product  is", a*b)
calculate(10,20)
calculate(100,200)
calculate(1000,2000)'''

'''def add(a,b):
    c=a+b
    print(c)
add(3,4)'''

'''while True:
    def add():
        a=int(input("a value"))
        b=int(input("b value"))
        print(a+b)
    add()'''

'''def add():
    a=int(input("a value"))
    b=int(input("b value"))
    print(a+b)
    add()
add()'''

'''def fullname():
    fname=input("fname")
    lname=input("lname")
    print((fname+" "+lname).title())
fullname()'''

'''def mul(a,b):
    print(a*b)
mul(3,4)'''

'''def mul(a,b):
    return a*b
print(mul(2,3))'''

#print vs Return
'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    print(c)
    print(d)
    print(e)
cal(2,4)'''

'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    #return c
    #return d
    #return e
    return c,d,e
print(cal(5,4))'''

'''def opt():
    a=int(input("a value  is"))
    b=int(input("b value is"))
    opt =int(input(choose the opt
                                     1 add
                                     2 sub
                                     3 mul))
    if opt==1:
        print(a+b)
    elif opt==2:
        print(a-b)
    elif opt==3:
        print(a*b)
opt()'''

'''while True:
    def cal():
        a=int(input("a value"))
        b=int(input("b value"))
        option=int(input(choose the option
                                   1 add
                                   2 sub
                                   3 mul))
        if option==1:
            print(a+b)
        elif option==2:
            print(a-b)
        elif option==3:
            print(a*b)
    cal()'''

'''def add():
    print(a+b)
def sub():
    print(a-b)
def mul():
    print(a*b)
a= int(input("a value"))
b=int(input("b value"))
option=int(input(choose the option
                            1.add
                            2.sub
                            3.mul))
if option==1:
    add()
elif option==2:
    sub()
elif option==3:
    mul()'''

#splitbill
'''def splitbill():
    a=int(input("Enter the total members: "))
    b=int(input("Enter the total amount: "))
    print("per head bill is ",b//a)
splitbill()'''

'''def splitbill():
    a=int(input("Enter the total mem: "))
    b=int(input("Enter the total amt: "))
    print(f"per person bill is :{b//a}")
    print("per head bill is: {} ".format(b//a))
splitbill()'''

'''def splitbill():
    a=int(input("Enter the total mem: "))
    b=int(input("Enter the total amt: "))
    c=b//a
    print(f"per person bill is :{c}")
    print("per head bill is: {} ".format(c))
splitbill()'''

#keyword and positional arguments
'''def Details(idno,name,mailid):
    idno=20
    name="krishna"
    mailid="krishna@code.com"
    print(idno,name,mailid)
Details(idno="idno",name="name",mailid="mailid")'''

'''def Details(idno,name,mailid):
    print(idno,name,mailid)
Details(idno="idno",name="name",mailid="mailid")
Details(idno=30,name="krishna",mailid="krish@code.com")
Details(40,"kanth","kanth@cod.com")
Details("hello","hel@oo.com",50)
Details(name="chintu",idno=60,mailid="chintu@chin.com")'''

#task-empployee->name,salary,designation
'''def employee(name,salary,designation):
    print(name,salary,designation)
employee(name="name",salary="salary",designation="designation")
employee(name="krishna",salary=500000,designation="HR")
employee(salary=300000,designation="manager",name="kanth")'''


#default Arguments
'''def grocery(item,price):
    print("item is %s" %item)
    print("price is %.2f" %price)
grocery("rice",1250)'''

'''def grocery(item="sugar",price=150):
    print("item is %s" %item)
    print("price is %.2f" %price)
grocery()'''

'''def grocery(item,price=200):
    print("item is %s" %item)
    print("price is %.2f" %price)
grocery("wheat")'''

'''def grocery(item="ghee",price):
    #non-def arg follows def arg
    print("item is %s" %item)
    print("price is %.2f" %price)
grocery(120)'''

#bakery->cake,price,qty
'''def bakery(cake,price,qty):
    print("cake is %s" %cake)
    print("price is %.2f" %price)
    print("qty is %s kg" %qty)
bakery("redwalvet",800,1)'''

'''def bakery(cake,price=600,qty=2):
    print("cake is %s" %cake)
    print("price is %.2f" %price)
    print("qty is %s kg" %qty)
bakery("butter scotch")'''

'''def bakery(cake="choclate",price=900,qty=4):
    print("cake is %s" %cake)
    print("price is %.2f" %price)
    print("qty is %s kg" %qty)
bakery()'''

#* arg -> is used to unpack the elements
'''a=[2,3,4,5,6]
print(a)
print(*a)'''

'''b=(2,3,4,5,6)
print(b)
print(*b)'''

'''d={6,7,4,9,4}
print(d)
print(*d)'''

'''e={"name":"krishna","year":2026}
print(e)
print(*e)'''

'''c="codegnan"
print(c)
print(*c)'''

'''x,y,z=2,4,6,7,8,9,1,3
print(x)
print(y)
print(z)
#error'''

'''a,b,c=2,4,7
print(a)
print(b)
print(c)'''

'''a,b,*c=2,4,7,5,6,8,10
print(a)
print(b)
print(*c)'''

'''a,*b,c=2,4,7,5,6,8,10,1,11,15
print(a)
print(*b)
print(c)'''

'''a="krishna"
print(a)
print(*a)'''

'''*a,b,c="krishna"
print(*a)
print(b)
print(c)'''

'''*a,*b,c="krishna"
print(*a)
print(*b)
#multi ** not accept
print(c)'''

#variable length arguments
'''def check(*a):
    print(a)
    print(type(a))
check()
b=[2,3,4,5,6]
check(*b)
c={1,2,3,8}
check(*c)
d=(5,6,7,8,9)
check(*d)
e={"year":2006,"month":"nov"}
check(*e)'''

'''def check1(*a):
    d=1 #creating a variable
    print(a)
    print(type(a))
    for i in a:
        d=d+i
        print(d)
check1()
check1(2,4,6,8,10)
check1(3,5,7,2.1,6.1)
check1(2,4,1,3,6,7,2.4,1.7,"krishna")'''

'''def check1(*a):
    d=1 #creating a variable
    print(a)
    print(type(a))
    for i in a:
        if type(i) in (int,float):
            d=d+i
        print(d)
check1()
check1(2,4,6,8,10)
check1(3,5,7,2.1,6.1)
check1(2,4,1,3,6,7,2.4,1.7,"krishna")'''

#kwargs(**)
'''def details(**a):
    print(a)
    print(type(a))
details()
d={"names":["krishna","teja","lohith","hemanth"],"marks":[60,70,40,30],"status":["p","a","p","a"]}
details(**d)'''

'''def details(**a):
    print(a)
    print(type(a))
    for i in a:
        print(i)
    for i in a.keys():
        print(i)
    for i in a:
        print(a[i])
    for i in a.values():
        print(i)
    for i in a:
        print(i,a[i])
    for i in a.items():
        print(i)
details()
d={"names":["krishna","teja","lohith","hemanth"],"marks":[60,70,40,30],"status":["p","a","p","a"]}
details(**d)'''

#both * and **
'''def final(*a,**b):
    d=2
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    for i in a:
        d=d+i
        print(d)
    for i,j in b.items():
        print("key is",i)
        print("value is",j)
final()
data=(2,3,4,5.3,2.1)
final(*data)
det={"names":["kanth","durga"],"marks":[20,40,30]}
final(**det)
final(*data,**det)'''

#global and local variables
#first case of global var
'''a=5
def check():
    print("inside the value:",a)
check()
print("outside the value:",a)'''

#second case of global var
'''a=6
def check1():
    a=10
    a=a**2
    print("inside the value:",a)
check1()
print("outside the value:",a)'''

#third case of both global and local 
'''a=4
def check3():
    a=7
    print("inside the value:",a)
    a=10
    print("updated the value:",a+5)
    b=12   #local var
    b=b+a
    print("value of b is:",b)
check3()
print("a value is ",a)
print("b value is ",b)'''  #error

#usage of global keyword
'''a=6
def final():
    global a,b
    print("inside value is :",a)
    a=7
    print("updated value is:",a)
    b=14
    b=b+a
    print("b value is:",b)
final()
print("a value is:",a)
print("b value is:",b)''' 

#ASCII - American Standard Code for Information Interchange
# CHR , ORD
'''print(chr(65))

print(chr(90))

print(chr(92))

print(ord("a"))

print(ord("z"))'''

#print(ord(98))  error-accept character only
#print(chr("a"))  error-accept numbers only

#task (A-Z,a-z)
'''for i in range(ord("A"),ord("Z")+1):
    print(chr(i),end=" ")

for i in range(97,123):
    print(chr(i),end=" ")'''

#name in ASCII values
'''n = input("Enter name:")
for i in n:
    print(i,ord(i))'''

#application
#railway ticket
'''while True:
    price=1000
    gen=input("Enter Gender:")
    def gender():
        gender=="male"
        age=int(input("Enter your age:"))
        if age > 60:
            a=(30/100)*price
            print("the ticket price is :",price-a)
        elif:
            print(price)
        gender=="female"
        age=int(input("Enter your age:"))
        elif age > 60:
            a=(50/100)*price
            print("the ticket price is:",price-a)
        elif age < 60:
            a=(30/100)*price
            print("the ticket price is:",price-a)
    gender()'''

#generators ->No tuple comprehension in above cases if we remove those cases and key paranthesis and the
#outcome is generator.
#a=[expr in var in collection/range]
'''a=[i for i in range(16)]
print(a)
print(type(a))'''

a=(i for i in range(16))
print(a)
print(*a)
print(type(a))

'''a=(i for i in range(16))
#print(list(a))
#print(tuple(a))
print(set(a))'''

#A Generator is also a function which cna be used as an iterator(loop) by producing group of values,where
#we can use yield keyword.
#Yield vs return- return will terminate the function where as yield can pass the function and go-on with
#every successive iteration.

'''a,b = [int(x) for x in input("enter the values").split(",")]
def check(a,b):
    while a<b:
        yield a
        a=a+1
        yield a
print(*check(a,b))'''

'''a,b = [int(x) for x in input("enter the values").split(",")]
def check(a,b):
    while a<b:
        return a
print(check(a,b))'''

#yield vs return
'''def mygen():
    #return "python"
    #return "java"
    return "python","java"
print(*mygen())'''

'''def mygen():
    yield "vja"
    yield "tnl"
    #yield "vja","tnl"
print(*mygen())

#next()
b=mygen()
print(next(b))
print(next(b))
print(next(b))'''

#built-in functions
#max(),min(),sum(),len(),print(),input(),type(),next(),range()
'''a=[1,2,3,4,5,7]
print(max(a))
print(min(a))
print(sum(a))
print(len(a))
a=int(input("Enter:"))
print(type(a))
if a[1] in range(10):
    print("true")'''

#fromkeys()
'''a="codegnan"
print(a)
print(list(a))
print(tuple(a))
print(set(a))
#print(dict(a))

b=dict.fromkeys(a)
print(b)

c=dict.fromkeys(a,"krishna")
print(c)

c["g"]="python"
print(c)'''

#eval()
'''while True:
    a=int(input("a val:"))
    b=int(input("b val:"))
    print(a+b)'''

'''while True:
    a=float(input("a val:"))
    b=float(input("b val:"))
    print(a+b)'''

'''while True:
    a=input("a val:")
    b=input("b val:")
    print(a+b)'''

'''while True:
    a=eval(input("a val:"))
    b=eval(input("b val:"))
    print(a+b)'''

#zip()-> wecan combine multiple collections into one collection.
'''a=[50,40,30,20,10]
names=["krishna","teja","lohith","venaktesh","hemanth"]
print(a+names)

b=zip(a,names)
print(b)

c=list(zip(a,names))
print(c)

d=tuple(zip(a,names))
print(d)

e=set(zip(a,names))
print(e)

g=dict(zip(a,names))
print(g)'''

#enumerate()->we can give counter to the collection
'''names=["krishna","teja","lohith","venaktesh","hemanth"]
for i in range(len(names)):
    print(i)

for i in range(len(names)):
    print(i,names[i])

b=list(enumerate(names))
print(b)

c=tuple(enumerate(names))
print(c)

d=set(enumerate(names))
print(d)

e=dict(enumerate(names))
print(e)'''

#annonymous fnuctions->annonymous functions are name less function and we use a keyword called as
#"LAMBDA" to create annonymous fnction.

#task->
'''def cal(x):
    print(2*x+5)
cal(5)

def f():
    x=int(input("enter val:"))
    print(2*x+5)
f()'''

#suntax -> a=lambda arg:expr

'''a=lambda x:2*x+5
print(a(5))

a=int(input("a value"))
b=lambda x:2*x+5
print(b(a))'''

'''a=lambda a,b:b*a
print(a(3,2))'''

'''a=lambda x:x.upper()
print(a("python"))'''

'''b=lambda fname,lname:fname+" "+lname
print(b("krishna","kanth"))'''

'''c,d=[x for x in input("Enter:").split()]
a=lambda c,d:(c.capitalize+" "+d).()
print(a(c,d))'''

#filter
a=[2,6,7,9,10,12,15,20,40,55,60,80]
'''if a%2==0:
    print(a)
    
for i in a:
    if i%2==0:
        print(i)

b=list(filter(lambda a:a%2==0,a))
print(b)'''

#[],(),{},set()
'''a=[]
print(type(a))

b=()
print(type(b))

c={}
print(type(c))

d=set()
print(type(d))'''

'''a=[[],(), {}, set(),"",None,5.6,3,"python",4+2j,True,False]
b=list(filter(None,a))
print(b)'''

#map() -> each object from a collection and forms a new collection
'''a=[2,4,6,8,9,10,30,40]
b=[3,1,5,7,9,11,15,50]
c=list(map(max,a,b))
print(c)

a=[2,4,6,8,9,10,30,40]
b=[3,1,5,7,9,11,15,50]
c=list(map(min,a,b))
print(c)'''


#run_time inputs()

'''a=int(input("a val:"))
b=int(input("b val:"))
print(a+b)'''

'''a,b=[int(x) for x in input("vals").split(",")]
print(a+b)'''

'''a,b=int(input("vals:").split(","))
print(a+b)''' #error

'''a,b=map(int, input("vals:").split(","))
print(a+b)'''

'''a=input("data1")
b=input("data2")
print(a+b)'''

'''a,b=[x for x in input().split()]
print(a+b)'''

'''a,b=input("data").split(",")
print(a,b)'''

'''a,b=map(str,input("data").split(","))
print(a+b)'''

'''a=list(map(int,input().split()))
print(a)

a=tuple(map(int,input().split()))
print(a)

a=set(map(int,input().split()))
print(a)'''

'''a=list(map(int, input("data").split(",")))
print(a)

a=tuple(map(int, input("data").split(",")))
print(a)

a=set(map(int, input("data").split(",")))
print(a)

a=list(map(str, input("data").split(",")))
print(a)

a=list(map(eval, input("data").split(",")))
print(a)'''

'''a=input("enter vals:")
b=dict(i.split(":")for i in a.split(","))
print(b)

a=dict(map(lambda x:x.split(":"),input().split(","))'''
