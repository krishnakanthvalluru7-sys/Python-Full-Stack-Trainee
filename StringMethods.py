Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #replace
>>> a="wait until you succeed"
>>> a.replace("wait","work")
'work until you succeed'
>>> 
...  
>>> #upper()
>>> a="python"
>>> a.upper()
'PYTHON'
>>> #lower
>>> b="CODE"
>>> b.lower()
'code'
>>> c="java"
>>> c.upper(0)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    c.upper(0)
TypeError: str.upper() takes no arguments (1 given)
>>> c.capatalize()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    c.capatalize()
AttributeError: 'str' object has no attribute 'capatalize'. Did you mean: 'capitalize'?
c[0].upper()
'J'
#capatalize
c.capatalize()
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    c.capatalize()
AttributeError: 'str' object has no attribute 'capatalize'. Did you mean: 'capitalize'?
c.capitalize()
'Java'
'Java'd=
SyntaxError: invalid syntax
c.capitalize()
'Java'
d="python course"
d.title()
'Python Course'
e="i am in class"
e.title()
'I Am In Class'
e.capitalize()
'I am in class'

#conditions
a="hello world"
a.startswith("h")
True
a.endswith("d")
True
a.isalpha()
False
b="helloworld"
b.isalpha()
True
a.isdigit()
False
b=1234
b.isdigit()
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    b.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
b="12345"
b.isdigit()
True
a.isdigit()
False
a.isalnum()
False
c="java"
c.isalnum()
True
d="krishna1234")
SyntaxError: unmatched ')'
d="krishna1234"
d.isalnum()
True


#strip()
#lstrip(),rstrip()
a="    krishna     "
a.tsrip()
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    a.tsrip()
AttributeError: 'str' object has no attribute 'tsrip'. Did you mean: 'lstrip'?
a.strip()
'krishna'
a.lstrip()
'krishna     '
a.rstrip()
'    krishna'

#concatenation
 a="code"
 
SyntaxError: unexpected indent
a="code"
b="gnan"
print(a+b)
codegnan
a="python"
b="fullstack"
print(a+b)
pythonfullstack
print(a+" "+b)
python fullstack
print(a.title()+" "+b.title())
Python Fullstack

fname="krishna"
lname="kanth"
print(fnmae+lname)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    print(fnmae+lname)
NameError: name 'fnmae' is not defined. Did you mean: 'fname'?
print(fname+lname)
krishnakanth
print(fname+" "+lname)
krishna kanth
print(fnmae.titile()+" "+lname.title())
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    print(fnmae.titile()+" "+lname.title())
NameError: name 'fnmae' is not defined. Did you mean: 'fname'?
print(fname.title()+" "+lname.title())
Krishna Kanth
print((fname+" "+lname).title())
Krishna Kanth

#split()
a="python java c"
a.split()
['python', 'java', 'c']
b="i am learning python"
b.split()
['i', 'am', 'learning', 'python']

#join()
b="vij","aya","wada"
"".join(b)
'vijayawada'
" ".join(b)
'vij aya wada'
"k".join(b)
'vijkayakwada'
join(b).""
SyntaxError: invalid syntax
c="hello"
"a".join
<built-in method join of str object at 0x00007FFD5FC188F8>
"a".join(c)
'haealalao'

#formatting
a=4
b=2
print
<built-in function print>
(
print(a+b)
6
print("the sum is",a+b)
the sum is 6
print("the sum is,a+b")
the sum is,a+b
city="tnl"
print("city is",city)
city is tnl

#format method()
a="motu"
b="patlu"
print("hello {}{}".format(a,b))
hello motupatlu
print("hello {} {}".format(a,b))
hello motu patlu
print("hello {} hello {}".format(a,b))
hello motu hello patlu
print("hello {} {}".title(a,b).format(a,b))
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    print("hello {} {}".title(a,b).format(a,b))
TypeError: str.title() takes no arguments (2 given)

#fstring()
a="ms"
b="dhoni"
print(f"hello {a}{b}")
hello msdhoni
print(f"hello {a} {b}")
hello ms dhoni

a="krihna"
lname="kant
SyntaxError: unterminated string literal (detected at line 1)
fname="krishna"
lname="kanth"
print(fname+lname)
krishnakanth
print("Hi {}{}".format(fname,lname))
Hi krishnakanth
print("Hi {} {}".format(fname,lname))
Hi krishna kanth

print(f"Hello {fname} {lname}")
Hello krishna kanth

a=3
b=5
c=a+b
print("the sum is {}".format(c))
the sum is 8
print(f"the sum is {a+b}")
the sum is 8
print("the sum is {} {} {}".format(a),(b),(a+b))
Traceback (most recent call last):
  File "<pyshell#130>", line 1, in <module>
    print("the sum is {} {} {}".format(a),(b),(a+b))
IndexError: Replacement index 1 out of range for positional args tuple
print("the sum is {}".format(a+b))
the sum is 8
