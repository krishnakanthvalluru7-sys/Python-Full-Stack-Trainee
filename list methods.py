Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list[]
a=[2,2.6,"python",(4+1j), True,False]
print(a)
[2, 2.6, 'python', (4+1j), True, False]
type(a)
<class 'list'>
b=3.2
type(b)
<class 'float'>
c=[4.3]
type(c)
<class 'list'>

a=["python","java","c"]
a.append("c++")
a
['python', 'java', 'c', 'c++']
a.append("ml","ai")
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a.append("ml","ai")
TypeError: list.append() takes exactly one argument (2 given)
a.append(["ml","ai"])
a
['python', 'java', 'c', 'c++', ['ml', 'ai']]

#extend
a=["ds","ai"]
a.extend(["c","c++"])
a
['ds', 'ai', 'c', 'c++']

#insert()
a=["black","white"]
a.insert(1,"green")
a
['black', 'green', 'white']

#index
a=["apple","banana","grapes"]
a.index("banana")
1

#copy
a.copy()
['apple', 'banana', 'grapes']
b=a.copy()
b
['apple', 'banana', 'grapes']

a=["hi","hello","you"]
a.pop()
'you'
a
['hi', 'hello']
a.pop("hi")
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    a.pop("hi")
TypeError: 'str' object cannot be interpreted as an integer

#remove
a.remove("hi")
a
['hello']
a.pop(1)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    a.pop(1)
IndexError: pop index out of range
a.copy(a)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    a.copy(a)
TypeError: list.copy() takes no arguments (1 given)
a.copy()
['hello']
a.pop(0)
'hello'
a
[]
#sort
a=["vij","tnl","vzg","rpl"]
a.sort()
a
['rpl', 'tnl', 'vij', 'vzg']
b=[2,6,9,2,10,20,40,4,1]
b.sort()
b
[1, 2, 2, 4, 6, 9, 10, 20, 40]
c=[2,2.3,"python",1+3j,True]
c.sort()
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    c.sort()
TypeError: '<' not supported between instances of 'str' and 'float'
#reverse
a=["orange","cherry","berry"]
a.reverse()
a
['berry', 'cherry', 'orange']
Traceback (most recent call last):
    
SyntaxError: invalid syntax. Perhaps you forgot a comma?
a=["c","java","python"]
#len()
a.len(a)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    a.len(a)
AttributeError: 'list' object has no attribute 'len'
len(a)
3
b="python"
len(b)
6
c=["c++"]
len(c)
1
>>> d="c++"
>>> len(d)
3
>>> a.count("a")
0
>>> a.count("c")
1
>>> 
>>> #clear
>>> a=["python","java","c++"]
>>> a.clear()
>>> a
[]
>>> b=[]
>>> b.append("krishna")
>>> b
['krishna']
>>> a.count(python)
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    a.count(python)
NameError: name 'python' is not defined
>>> a.count("python")
0
#tuple
a=(2,3.4,"c++")
len(a)
