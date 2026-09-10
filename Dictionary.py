Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #dict{}
>>> a={"name":"krishna","city":"tnl"}
>>> print(a)
{'name': 'krishna', 'city': 'tnl'}
>>> type(a)
<class 'dict'>
>>> b={"name","city"}
>>> type(b)
<class 'set'>
>>> 
>>> #methods
>>> a={"year":2026,"month":"oct","date":12}
>>> a.keys()
dict_keys(['year', 'month', 'date'])
>>> a.items()
dict_items([('year', 2026), ('month', 'oct'), ('date', 12)])
>>> a.values()
dict_values([2026, 'oct', 12])
>>> a["month"]
'oct'
>>> a[2026]
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a[2026]
KeyError: 2026
a.get("year")
2026

#update (adding)
a={"name":"krishna","city":"tnl"}
a.update({"mailid":"krishna@gmai.com"})
a
{'name': 'krishna', 'city': 'tnl', 'mailid': 'krishna@gmai.com'}
a.update({"year":2026},{"time":6})
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    a.update({"year":2026},{"time":6})
TypeError: update expected at most 1 argument, got 2
a.update({"year":2026,"time":6})
a
{'name': 'krishna', 'city': 'tnl', 'mailid': 'krishna@gmai.com', 'year': 2026, 'time': 6}

#setdefault
a={"hour":12,"min":10}
a.setdefault("sec",6)
6
a
{'hour': 12, 'min': 10, 'sec': 6}

#pop & popitem
a={"week":"wed","date":9}
a.pop()
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
a.pop("week")
'wed'
a
{'date': 9}
a
{'date': 9}
=
a={"country":"india","state":"ap"}
a.popitem
<built-in method popitem of dict object at 0x0000028181BF2CC0>
a.popitem()
('state', 'ap')

a
{'country': 'india'}

a={"name":"krishna","course":"pythhon","duration":100}
a.copy()
{'name': 'krishna', 'course': 'pythhon', 'duration': 100}
len(a)
3
a.count()
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    a.count()
AttributeError: 'dict' object has no attribute 'count'
a.index()
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    a.index()
AttributeError: 'dict' object has no attribute 'index'
a.count("name")
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    a.count("name")
AttributeError: 'dict' object has no attribute 'count'

#duplicate values
a={"name":"krishna","year":2026,"name":"kanth"}
print(a)
{'name': 'kanth', 'year': 2026}
a={"name":"krishna","year":2026,"name":"krishna"}
print(a)
{'name': 'krishna', 'year': 2026}
a={"name":"krishna","year":2026,"name1":"kanth"}
print(a)
{'name': 'krishna', 'year': 2026, 'name1': 'kanth'}

#multiples values
a={"idnos":[20,30,40],"names":["krishna","gopi","kartheek"],"places":["tnl","vij","vzg"]}
print(a)
{'idnos': [20, 30, 40], 'names': ['krishna', 'gopi', 'kartheek'], 'places': ['tnl', 'vij', 'vzg']}
type(a)
<class 'dict'>
a.keys()
dict_keys(['idnos', 'names', 'places'])
a.values()
dict_values([[20, 30, 40], ['krishna', 'gopi', 'kartheek'], ['tnl', 'vij', 'vzg']])
a.items()
dict_items([('idnos', [20, 30, 40]), ('names', ['krishna', 'gopi', 'kartheek']), ('places', ['tnl', 'vij', 'vzg'])])
