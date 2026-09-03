Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#datatypes
a=7
type(a)
<class 'int'>
b=6.7
type(b)
<class 'float'>
c='python'
type(c)
<class 'str'>
d="codegnan"

type(d)
<class 'str'>
e='''course'''
type(e)
<class 'str'>
f=1+4j
type(f)
<class 'complex'>
f=j+2
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    f=j+2
NameError: name 'j' is not defined
f=3j+3
type(f)
<class 'complex'>
>>> g=True
>>> type(g)
<class 'bool'>
>>> h=False
>>> type(h)
<class 'bool'>
>>> i=('j+3')
>>> type(i)
<class 'str'>
>>> 
>>> #int
>>> int(7)
7
>>> int(6.7)
6
>>> int('hello')
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    int('hello')
ValueError: invalid literal for int() with base 10: 'hello'
>>> int(4+7j)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    int(4+7j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(False)
0

#float
float(7)
7.0
float(7.3)
7.3
float('hi')
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    float('hi')
ValueError: could not convert string to float: 'hi'
float(4+7j)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    float(4+7j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
float(False)
0.0

#str
str(7)
'7'
str(7.3)
'7.3'
str('Hi python')
'Hi python'
str(4+9j)
'(4+9j)'
str(True)
'True'
str(False)
'False'

#complex
complex(7)
(7+0j)
complex(7.6)
(7.6+0j)
complex(3+7j)
(3+7j)
complex('hello python')
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    complex('hello python')
ValueError: complex() arg is a malformed string
complex(True)
(1+0j)
complex(False)
0j

#bool
bool(7)
True
bool(7.4)
True
bool('hi')
True
bool(4+8j)
True
bool(True)
True
bool(False)
False
