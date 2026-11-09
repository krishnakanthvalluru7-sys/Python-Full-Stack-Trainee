#if condition by using comparison operator
#<,>,<=,>=,!=,==
'''a=20
b=40
if a>b:
    print("False")'''

'''a=20
b=40
if a<b:
    print("True")'''

'''a=30
b=60
if a>=b:
    print("False")'''

'''a=30
b=60
if b<=a:
    print("True")'''

'''a=30
b=20
if a!=b:
    print("True")'''

'''a=6
b=6
if b==a:
    print("Equal")'''

'''a="python"
if a!="python":
    print("True")'''

'''a="java"
if a=="python":
    print("true")'''

'''a=int(input("a value"))
b=int(input("b value"))
if a>b:
    print("less")'''

'''a=int(input("a value"))
if a>30:
    print("True")'''

#if condition by logical operators
#and,or,not
'''a=5
b=9
if a<b and b>a:
    print("true")'''

'''a=5
b=8
if a<=b and b>=a:
    print("true")'''

'''a=9
b=15
if a!=b and b!=a:
    print("false")'''

'''a=9
b=15
if a==b and b==a:
    print("false")'''

'''a=12
b=16
if a<b or b>a:
    print("true")'''

'''a=12
b=14
if a<=b or b>=a:
    print("true")'''

'''a=10
b=15
if a!=b or b==a:
    print("false")'''

'''a=3
b=6
if not a<b:
    print("false")'''

'''a=3
b=6
if not a>b:
    print("true")'''

'''a=3
b=4
if not a<b and b>a:
    print("false")'''

'''a=int(input("The value of a is"))
b=int(input("The value of b is"))
if not b>a:
    print("True")'''

#if condition by using identify operator
#is,is not
'''a= 15
if type(a) is int:
    print("int")'''
    
'''a= 15
if type(a) is not int:
    print("int")'''

'''a=3.6
if type(a) is not int:
    print("float")'''

'''a=int(input("the value is"))
if type(a) is float:
    print("int")'''

#if condition by using Membership operators
#in,not in

'''a=[1,2,3,4,5,6,7]
if 3 in a:
    print("is in")'''

'''a=[1,2,3,4,5,6,7]
if 5 not in a:
    print("is in")'''

'''a=[1,2,3,4,5,6,7]
if 30 not in a:
    print("is in")'''

'''a=[1,2,3,4,5,6,7]
b=int(input("value is"))
if b in a:
    print("true")'''

#if-else condition by using comparison operators
'''a=5
b=8
if a<b:
    print("true")
else:
    print("false")'''

'''a=5
b=8
if a>b:
    print("true")
else:
    print("false")'''

'''a=5
b=8
if a!=b:
    print("true")
else:
    print("false")'''

'''a=8
b=8
if a==b:
    print("true")
else:
    print("false")'''

#if-else condition by using logical operators

'''a=5
b=8
if a<b and b>a:
    print("true")
else:
    print("false")'''

'''a=5
b=8
if a!=b or b==a:
    print("true")
else:
    print("false")'''

'''a=5
b=8
if not b>a:
    print("true")
else:
    print("false")'''

'''a=5
b=8
if not a<b and b>a:
    print("true")
else:
    print("false")'''

#if-else condition by using identify operators

'''a=5
if type(a)is int:
    print("true")
else:
    print("false")'''

'''a=5.4
if type(a)is not int:
    print("true")
else:
    print("false")'''

'''a=5.4
if type(a)is float:
    print("true")
else:
    print("false")'''

#if-else condition by using membership operators

'''b=[1,5,7,9,3,7,9]
if 7 in b:
    print("true")
else:
    print("false")'''

'''b=[1,5,7,9,3,7,9]
if 2 not in b:
    print("true")
else:
    print("false")'''

'''b=[1,5,7,9,3,7,9]
if  20 in b:
    print("true")
else:
    print("false")'''

#if-elif-else conditions by using comparison operators
'''a=2
b=4
if a<b:
    print("less")
elif b>a:
    print("greater")
else:
    print("true")'''

'''a=6
b=8
if a>b:
    print("less")
elif b>a:
    print("greater")
else:
    print("true")'''

'''a=12
b=14
if a==b:
    print("less")
elif b<a:
    print("greater")
else:
    print("true")'''

'''a=5
b=8
if a<b:
    print("less")
elif b>a:
    print("greater")
elif a!=b:
    print("not equal")    
else:
    print("true")'''

#if-elif-else conditions by using logical operators 
'''a=5
b=3
if a<b and b>a:
    print("less")
elif a>=b or b!=a:
    print("greater")
elif not b<a:
    print("true")
else:
    print("false")'''

#if-elif-else conditions by using identify operators
'''a=15
if type(a)is int:
    print("true")
elif type(a)is not float:
    print("greater")
else:
    print("false")'''

#if-elif-else conditions by using membership operators
'''a=[2,4,6,8,9,2,10]
if 16 in a:
    print("true")
elif 4 not in a:
    print("greater")
else:
    print("false")'''

#multiple -if
'''a=5
b=10
if a<b:
    print("less")
if b>a:
    print("greater")
if a!=b:
    print("true")'''

'''a=5
b=10
if a<b:
    print("less")
elif b>a:
    print("greater")
if a!=b:
    print("true")'''

#mutiple-if condition by using logical operators
'''a=4
b=2
if a>b and b<a:
    print("true")
if b>a or a!=b:
    print("greater")
if not b>a:
    print("false")'''

#multiple-if condition by using identify operators
'''a=40
if type(a) is int:
    print("true")
if type(a)is not int:
    print("greater")
if type(a) is complex:
    print("false")'''

#multiple-if conditions by using membership operators
'''b=[20,21,22,23,24,26]
if 19 in b:
    print("false")
if 24 not in b:
    print("true")
if 26 in b:
    print("in")'''

#nested-if
'''a=6
b=12
if a<b:
    print("less")
    if b>a:
        print("greater")'''

'''a=6
b=12
if a>b:
    print("less")
if b>a:
    print("greater")'''

'''a=6
b=12
if a==b:
    print("less")
    if b>a:
        print("greater")'''

'''a=10
b=20
if a>b:
    print("less")
    if b==a:
        print("equal")'''

'''a=10
b=20
if a<b:
    print("less")
    if b==a:
        print("equal")
    else:
        print("true")'''

'''a=30
b=50
if a>b:
    print("less")
    if b>a:
        print("equal")
else:
    print("true")'''

'''a=60
b=80
if a<b:
    print("less")
    if b>a:
        print("equal")
    else:
        print("false")
else:
    print("true")'''

'''a=60
b=80
if a>b:
    print("less")
    if b==a:
        print("equal")
    else:
        print("false")
else:
    print("true")'''

'''a=60
b=80
if a<b:
    print("less")
    if b==a:
        print("equal")
    if a!=b:
        print("not equal")
    else:
        print("false")
else:
    print("true")'''

#voting
'''age = int(input("The age is"))
if age>18:
    print("Eligible for voting")
else:
    print("Not eligible for voting")'''

#even and odd
'''b =int(input("the number is"))
if b%2==0:
    print("it is even")
else:
    print("it is odd")'''

#leap year
'''year=int(input("enter year"))
if year%4==0:
    print("Leap Year")
else:
    print("not Leap Year")'''

    #vowel
'''vowels=["a","e","i","o","u"]
letter = input("enter the letter").lower()
if letter in vowels:
    print("Vowel")
else:
    print("consonants")'''

#guest code
'''name=input("enter the name").lower()
if name=="krishna":
    print("welcome",name)
else:
    print("welcome guest")'''

#multiple users
'''names = ["teja","lohith","hemanth","gopi","kartheek"]
b =input("enter a name")
if b in names:
    print("welcome ",b)
else:
    print("Welcome Guest")'''

#Bakery prices
'''item = int(input("enter price"))
if item==1200:
    print("redvolvet cake")
elif item==1000:
    print("choco almond")
elif item==800:
    print("choclate cake")
elif item==600:
    print("butter scotch")
else:
    print("sorry cake is not available")'''

#pizza name
name=input("enter pizza name")
if name=="crispy chicken":
    print("price is 800")
elif name=="bbq":
    print("price is 600")
elif name=="panner":
    print("price is 400")
elif name=="corn":
    print("price is 200")
else:
    print("item is greater than 200 only")
    

