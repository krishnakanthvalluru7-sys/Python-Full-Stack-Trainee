a=["apple","banana","grapes"]
#["APPLE","BANANA","GRAPES"]

#print(a.upper())

'''b=str(a)
print(b.upper())'''

'''for i in a:
    print(i.upper(),end=" ")'''

'''b=[]
for i in a:
    b.append(i.upper())
print(b)'''

#for loop
'''a=[10,20,30,40,50]
for i in a:
    print(i)

a=[10,20,30,40]
for i in a:
    print(a) #iterates upto size of set a

a=[10,20,30,40]
for i in a:
    print(i)
print(type(a))
print(type(i))

a={"year":2026,"month":"oct"}
for i in a:
    print(i)
for i in a.keys():
    print(i)
print(type(a))
print(type(i))
for in a.items():
    print(i)
for i in a.values():
    print(i)

a=["python","java"]
for i in a:
    print(i)
print(type(a))

a=["python","java"]
for i in a:
    print(i,end=" ")'''

#while loop

'''a=10
while a>1:
    print(a)'''

'''a=10
while a<1:
    print(a)'''

'''a=20
while a>=1:
    print(a)
    a=a-1'''

'''a=20
while a<1:
    a=a-1
    print(a)'''

'''a=15
while a>2:
    print(a)
    a=a-1'''

'''a=20
while a>1:
    a=a-1
print(a)'''

'''a=30
while a>1:
    print(a)
    a+=1'''

'''a=30
while a>1:
    print(a)
    a-=1'''

'''a=5
while a<15:
    print(a)
    a+=1'''

'''while True:
    age=int(input("enter the age"))
    if age>=18:
        print("eligible gor vote")
    else:
        print("not eligible for vote")'''

#range()
#start-stop-step

'''for i in range(10):
    print(i)'''

'''for i in range(15,30):
    print(i)'''

'''for i in range(0,20,2):
    print(i,end=" ")'''

'''for i in range(5,50,5):
    print(i,end=" ")'''

'''for i in range(3,30,3):
    print(i,end=" ")'''

'''for i in range(9,90,9):
    print(i,end=" ")'''

#task
'''while True:
    marks = int(input("Enter the marks"))
    if marks in range(91,101):
        print("Grade-A")
    elif marks in range(81,91):
        print("Grade-B")
    elif marks in range(71,81):
        print("Grade-B")
    elif marks in range(50,71):
        print("Grade-D")
    else:
        print("Fail")
        break'''


'''while True:
    students=int(input("enter the total no of students"))
    p=0
    a=0
    for i in range(1,students+1):
        att=input(f"students {i} (p/a)")
        if att=="p":
            p+=1
        elif att=="a":
            a+=1
    print(".......Attendence Tracker.....")
    print("total no of students",students)
    print("total no of presenties", p)
    print("total no of absenties",a)'''

#break
'''a=10
while a>1:
    print(a)
    a=a-1
    if a==7:
        break'''

'''a=10
while a>1:
    a=a-1
    if a==4:
        break
    print(a)'''


'''for i in range(10):
    if i == 8:
        break
    print(i)'''

'''a="python"
if a==h:
    break
print(a)'''#error

'''a="python"
for i in a:
    if i =="h":
        break
    print(i)'''

#continue
'''a=20
while a>5:
    a=a-1
    if a==12:
        continue
    print(a)'''

'''for i in range(15):
    if i==10:
        continue
    print(i)'''

'''a="course"
for i in a:
    if i=="r":
        continue
    print(i)'''

#pass
'''a=5
while a>1:
    print(a)
    a=a-1
    if a==2:
        pass'''

'''for i in range(20):
    if i ==10:
        pass
    print(i)'''

#task
#atm application
while True:
    balan=100000
    pwd=3456
    card=input("insert the card")
    if card=="c":
        print("Welcome krishna")
        password=int(input("enter the password"))
        if password==pwd:
            option=int(input('''choose the option
                                    1.balance enq
                                    2.withdraw'''))
            if option==1:
                print("your account bal is", balan)
            elif option==2:
                money=int(input("enter the amount"))
                print(money)
                balance=balan-money
                print("rem acc bal is", balance)
            else:
                print("invalid option")
        else:
            print("incorrect password")
    else:
        print("invalid card")





    
