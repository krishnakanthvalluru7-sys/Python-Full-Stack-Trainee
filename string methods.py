Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#string methods
#length len()
a="Python"
len(a)
6
b="python course"
len(b)
13
c=""
len(c)
0
d=" "
len(d)
1

#count()
a="twinkle twinkle little star"
count(a)]
SyntaxError: unmatched ']'
count(a)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    count(a)
NameError: name 'count' is not defined. Did you mean: 'round'?
a.count("twinkle")
2
a.count("e")
3
a.count("a")
1
a.count(" ")
3

#find a string
a="python"
a[1]
'y'
a.find("t")
2
a.find("n")
5
>>> 
>>> #escape sequences
>>> #\n->new line
>>> #\t->tab space
>>> a="idno\nname\tmobileno\nmailid\nbranch\tcollege"
>>> print(a)
idno
name	mobileno
mailid
branch	college
>>> b="10\nkrishna\123456789\nkrishna@code.com\nCSE\tKHIT"
>>> print(b)
10
krishnaS456789
krishna@code.com
CSE	KHIT
>>> b="10\nkrishna\n12345678\nkrishna@code.com\nCSE\tKHIT"
>>> print(b)
10
krishna
12345678
krishna@code.com
CSE	KHIT
