#Error Handling
#Syntax Error -> compile error
#run_time error -> during execution it will happens
#logical error -> error in logic (it cant visible)
#syntax
'''for i in range(10)
print(i)'''

#run_time error
#print(5+9)
'''a=int(input("a val:"))
b=int(input("b val:"))
print(a//b)'''

#logical error
'''a=10
b=20
print(a-b)'''

'''a=4
b=8
if a<b:
    print("less")'''

'''a=4
b=8
if a>b:
    print("less")'''


#Exception handling - try, except, else and finally
#try - instructions from which we are expecting the exceptions.
#except - exceptions are raised in try block it will be handle by this block.
#else - optional(no exceptions)
#finally - always
'''while True:
    try:
        a=int(input("a val:"))
        b=int(input("b val:"))
        c=a//b
        print(c)
    except:
        print("exceptions are raised")
    else:
        print("NO exceptions")
    finally:
        print("program ends")'''

'''a=int(input("a val:"))
b=int(input("b val:"))
try:
    c=a//b
    print(c)
except:
    print("exceptions are raised")
else:
    print("NO exceptions")
finally:
    print("program ends")'''

#file handling
#write()
'''a=open("krishna.txt","w")
a.write("python full stack trainee")
a.close()'''

'''a=open("krishna.txt","w")
a.write("Codegnan")
a.close()'''

#append()
'''a=open("krishna.txt","a")
a.write("hyd\n")
a.close()'''

'''a=open("krishna.txt","w")
a.write(input())
a.close()'''

'''a=input()
b=open("krishna.txt","w")
b.write(a)
b.close()'''

#Read()
'''a=input("data:")
b=open("krishna.txt","w")
b.write(a)
b.close()'''

#readlines()
a=open("krishna.txt")
#print(a.read()) #it will display entire content
#print(a.readline()) #it will display first line
#print(a.readlines()) it will display with \n
#print(a.read(9)) #it will display no.of characters

#writelines() -> it makes every object side by side
'''a=open("python.txt","w")
b=["krishna","teja","lohith","hemanth"]
a.writelines("\n".join(b))
a.close()'''

'''a=open("functions.py")
print(a.read())'''

a=open("C:/Users/HP/Downloads/Python fullstack/CODE/loops.py")
print(a.read())
