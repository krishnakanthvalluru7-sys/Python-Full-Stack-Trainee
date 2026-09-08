Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #tuple
>>> a=(4,2.3,"krishna",2+4j,True)
>>> print(a)
(4, 2.3, 'krishna', (2+4j), True)
>>> type(a)
<class 'tuple'>
>>> len(a)
5
>>> a.count(2.3)
1
>>> a.index(True)
4
>>> 
>>> #sets{}
>>> a={3,6.2,"java",3+5j}
>>> print(a)
{'java', (3+5j), 3, 6.2}
>>> type(a)
<class 'set'>
>>> b={2,4,5,2,8,4,0}
>>> print(b)
{0, 2, 4, 5, 8}

a={2,4,6,8,7}
a.add(10)
a
{2, 4, 6, 7, 8, 10}
a={2,4,6,8,9,10}
b={8,9,10}
b.issubset(a)
True
True
True
a={2,4,6,8,9,10}
b={8,9,10}
SyntaxError: multiple statements found while compiling a single statement
a={2,4,6,8,9,10,11}
b={8,9,10}

a.issuperset(b)
True
b.issuperset(a)
False
a={1,2,4,6,8,9}
b={4,6,8}
a.union(b)
{1, 2, 4, 6, 8, 9}
a={10,12,13,14,15,16,17}
b={13,14,16}
a.intersection(b)
{16, 13, 14}
a={2,3,4,5,6,7,8}
b={5,6,7,8,9}
a.update(b)
a
{2, 3, 4, 5, 6, 7, 8, 9}
a
{2, 3, 4, 5, 6, 7, 8, 9}
b.update(a)
a
{2, 3, 4, 5, 6, 7, 8, 9}
b
{2, 3, 4, 5, 6, 7, 8, 9}
a={3,4,5,6,7,8}
b={1,2,3,7,8,9,10}
a.difference(b)
{4, 5, 6}
b.difference(a)
{1, 2, 10, 9}
a={4,5,6,14,16,18,19}
b={1,2,4,19,21,22}
a.symmetric_difference(b)
{1, 2, 5, 6, 14, 16, 18, 21, 22}
a={4,5,6,7,8}
b={1,2,3,4,5,6,7}
a.difference_update(b)
a
{8}
a
{8}
b.difference_update(a)
b
{1, 2, 3, 4, 5, 6, 7}

a={4,5,6,7,8,9}
b={6,7,8,9,10}
a.intersection_update(b)
a
{8, 9, 6, 7}
b.intersection_updatea(a)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    b.intersection_updatea(a)
AttributeError: 'set' object has no attribute 'intersection_updatea'. Did you mean: 'intersection_update'?
b.intersection_update(a)
b
{8, 9, 6, 7}
a
{8, 9, 6, 7}
b
{8, 9, 6, 7}

a={3,4,5,6,7,8,9,10}
b={1,2,3,4,5,6,7}
a.symmetric_difference_update(a)
a
set()

a.symmetric_difference_update(b)
a
{1, 2, 3, 4, 5, 6, 7}
a={1,2,3,4,5,6,7,8,9}
b={5,6,7,8,9,20,10}
a.symmetric_difference_update(b)
a
{1, 2, 3, 4, 10, 20}
b.symmetric_difference_update(a)
b
{1, 2, 3, 4, 5, 6, 7, 8, 9}

a={10,20,30,40,50}
a.pop()
50
a.pop()
20
a.remove(2)
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    a.remove(2)
KeyError: 2
a.remove(20)
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    a.remove(20)
KeyError: 20
a.remove(10)
a
{40, 30}

a={3,4,5,6,7,8}
a.discard(5)
a
{3, 4, 6, 7, 8}
a.copy()
{3, 4, 6, 7, 8}
b=a.copy()
b
{3, 4, 6, 7, 8}

a={5,6,7,8,9}
a.clear()
a
set()
b=set()
b
set()
b.add(40)
b
{40}

a={3,4,5,6,7}
len(a)
5
a.index(4)
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    a.index(4)
AttributeError: 'set' object has no attribute 'index'
a.count(3)
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    a.count(3)
AttributeError: 'set' object has no attribute 'count'

a={1,2,3,4}
b={6,7,8,9}
a.isdisjoint(b)
True
