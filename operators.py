Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#arthematic
a=2
b=5
print(a+b)
7
print(a-b)
-3
print(a*b)
10
print(a//b)
0
print(a/b)
0.4
print(a%b)
2

#assignment
a=4
b=3
a+=b
a
7
a-=b
a
4
a*=4
a
16
a//=1
a
16
a/=2
a
8.0
a%=1
a
0.0
a**=2
a
0.0

b+=1
b
4
b-=2
b
2
b*=
SyntaxError: invalid syntax
b*=3
b
6
b/=3
b
2.0
b//=2
b
1.0
b**=1
b
1.0

#comparison
a=9
b=10
a>b
False
b<a
False
a!=b
True
a==b
False
a<=b
True
b>=a
True
a>=b
False
b<=a
False
a==b
False

#logical
a=5
b=10
a<b and b>a
True
a>b and b>a
False
a<=b and b>=a
True
a!=b
True
a!b and a==b
SyntaxError: invalid syntax
a!=b and a==b
False
a<b or b>a
True
a<=b or b<=a
True
a!=b or a==b
True
not True
False
not False
True

#identify
a=5
type(a) is int
True
type(a) is not int
False
type(a) is float
False
b=5.6
type(b) is float
True
type(b) is not float
False

 
#membership
b=2,4,5,6,3,9,7
9 in b
True
2 in b
True
3 in b
True
11 in b
False

#bitwise
a=2
b=5
a&b
0
ain(2)
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    ain(2)
NameError: name 'ain' is not defined. Did you mean: 'bin'?
bin(2)
'0b10'
bin(5)
'0b101'
a=3
b=4
bin(3)
'0b11'
bin(4)
'0b100'
a&b
0

a=4
b=
SyntaxError: invalid syntax
a=9
b=7
bin(9)
'0b1001'
bin(7)
'0b111'
a/b
1.2857142857142858
a|b
15

a=6
~a
-7
-(a+1)
-7
>>> b=5
>>> ~b
-6
>>> c=-4
>>> ~c
3
>>> 
...  
>>> #^
>>> a=6
>>> b=8
>>> a^b
14
>>> 
>>> #<<
>>> a=
SyntaxError: invalid syntax
>>> a=6
>>> a<<3
48
>>> 
>>> a=3
>>> a>>2
0
