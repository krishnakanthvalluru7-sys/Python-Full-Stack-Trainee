#list comprehension
a=["python","java","dsa"]
#["PYTHON","JAVA","DSA"]
#print(a.upper())

'''for i in a:
    print(i.upper(),end=" ")'''

'''b=[]
for i in a:
    b.append(i.upper())
print(b)'''

#syntax
#a=[expr for var in collection/range]
'''b=[i.upper() for i in a]
print(b)'''

'''c=["apple","mango"]
c=[i.capitalize() for i in c]
print(c)'''

'''a=[1,2,3,5,6,8,12,13]
a=[i*i for i in a]
print(a)'''

'''b=[c for c in range(0,21)]
print(b)'''

'''x=[i for i in range(16) if i%2==0]
print(x)'''

'''x=[i**2 for i in range(31) if i%2==0]
print(x)'''

'''a=["grapes","berry","kiwi","mango","dragon","apple"]
a=[i.capitalize() for i in a if "a" in i]
print(a)'''

#no elif usage in list comprehension
#if-else usage in  "          "
'''c=[i**2 if i%2==0 else i*5 for i in range(21)]
print(c)'''

a=[1,2,3,4,5]
b=[5,4,3,2,1]
x=[a[i]+b[i] for i in range(5)]
print(x)
