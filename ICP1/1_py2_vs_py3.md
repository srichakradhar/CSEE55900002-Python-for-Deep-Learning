1. Print Statement:
py2: `print "Hello Python"`
py3: `print("Hello Python")`

2. No more `raw_input()`
```py
>>> my_input = input('enter a number: ')

enter a number: 123

>>> type(my_input)
<type 'int'>

>>> my_input = raw_input('enter a number: ')

enter a number: 123

>>> type(my_input)
<type 'str'>
```
```py
>>> my_input = input('enter a number: ')

enter a number: 123

>>> type(my_input)
<class 'str'>
```

3. The __future__ module:
py2: from __future__ import division
py3: import division

breaking changes introduced in python3 were packaged into the in-built __future__ module in python2

4. Integer division:

Python 2
```py
print '3 / 2 =', 3 / 2
print '3 // 2 =', 3 // 2
print '3 / 2.0 =', 3 / 2.0
print '3 // 2.0 =', 3 // 2.0
```
```py
3 / 2 = 1
3 // 2 = 1
3 / 2.0 = 1.5
3 // 2.0 = 1.0
```

Python 3
```py
print('Python', python_version())
print('3 / 2 =', 3 / 2)
print('3 // 2 =', 3 // 2)
print('3 / 2.0 =', 3 / 2.0)
print('3 // 2.0 =', 3 // 2.0)
```
```py
Python 3.4.1
3 / 2 = 1.5
3 // 2 = 1
3 / 2.0 = 1.5
3 // 2.0 = 1.0
```

5. __next__() in python 2 vs the .next() method in python 3
Python 2:
```py
next(my_generator)
my_generator.next()
```
Python 3:
```py
next(my_generator)
```

6. Inheritance in Simpler
`super() -> same as super(__class__, self)`


In summary, Python 3 makes it easier to develop software which is,

* Less prone to hidden or tricky bugs - i.e., robust and reliable;
* More straightforward to change over time - in other words, maintainable; and
* Simpler to troubleshoot and fix when things do go wrong.

than Python 2.

Ref:
* https://powerfulpython.com/blog/main-difference-python-3/
* https://sebastianraschka.com/Articles/2014_python_2_3_key_diff.html#parsing-user-inputs-via-input