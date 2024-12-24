###
decorator functions for regular expressions 
###
def decorator_function(fun):
    def wrapper_fun():
        print('this add before original code')
        fun()
        print('this added after original function')
    return wrapper_fun()
@decorator_function
def fun():
    print('this is the original code')
def decorator_function(fun):
    def wrapper_fun():
        print('hello')
        fun()
        print(' hi')
    return wrapper_fun()
@decorator_function
def fun():
    print('my name is deepika')
import re
x = 'mother theresa institute'
y = re.split('',x)
print(len(y))
import re
x = input("enter the string:")
y = re.split(' ',x)
print(len(y))
print(len(y)-1)
print(y)
x = ['palle','python','java','ml']
y = ' '.join(x)
print(y)
import re
x = 'palle technologies banglore'
y = re.match('alle',x)
if y:
    print('it  starts with alle')
else:
    print('it does not start with alle')
import re
x = 'palle technologies bangalore india palye abc'
y = re.findall('^palle',x)
print(y)
y = re.findall('^palle/Palle',x)
print(y)
y = re.findall('pal',x)
print(y)
x ='python lab bangalore lb is a laab'
y = re.findall('la*b',x)
print(y)
###
this add before original code
this is the original code
this added after original function
hello
my name is deepika
 hi
26
enter the string: hello
2
1
['', 'hello']
palle python java ml
it does not start with alle
['palle']
[]
['pal', 'pal']
['lab', 'lb', 'laab']
