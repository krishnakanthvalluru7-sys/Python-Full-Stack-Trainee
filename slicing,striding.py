Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a="codegnan"
a[0]+a[1]+a[2]+a[3]
'code'

#slicing
a[0:3]
'cod'
a[0:4]
'code'
a[:4]
'code'
a[5:8]
'nan'
a[4:8]
'gnan'

a="work until you suceed"
a[6:10]
'ntil'
a[5:10]
'until'
a[15:]
'suceed'
a[11:13]
'yo'
a[11:14]
'you'
a[0:3]
'wor'
a[0:4]
'work'

b="Vijayawada is a royal City"
b[21:]
' City'
b[22:]
'City'
b[16:20]
'roya'
b[16:21]
'royal'
b[0:9]
'Vijayawad'
b[0:10]
'Vijayawada'
b[11:13]
'is'
c="Happy Teachers Day"
c[14:]
' Day'
c[-14:-18]
''
c[-13]
' '
c[:-13]
'Happy'
c[-3:]
'Day'
c[-12:-5]
'Teacher'

d="Vizag is a city of destiny"
d[-26:-22]
'Viza'
d[-26:-23]
'Viz'
d[-26:-21]
'Vizag'
d[-15:-11]
'city'
d[-6:]
'estiny'
>>> d[-7:]
'destiny'
>>> d="Vizag is a city of destiny"
>>> 
>>> #striding
>>> a="Data Science"
>>> a=[::]
SyntaxError: invalid syntax
>>> a[::]
'Data Science'
>>> a="cloud computing"
>>> a[2:13:3]
'o mt'
>>> a[4:14:5]
'dp'
>>> a[3:12:6]
'up'
>>> 
>>> b="pyhton course"
>>> b[-2:-12:-4]
'sct'
>>> c="python course"
>>> c[-2:-12:-4]
'sch'
>>> c[-4:-13:-5]
'uo'
c[-6:-12:-2]
'cnh'

 
#do's dont's
a="python course"
a[7:3:2]
''
a[3:7:2]
'hn'
a[-9:-5:-2]
''
a[::1]
'python course'
a[::-1]
'esruoc nohtyp'
