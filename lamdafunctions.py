###
write the programs for using lambda function filter,map,res for biggestno,evenodd,filtering and mappin?
###
def f1(fun,x):
    print('welcome')
    fun(x)
    print('bye')
def f2(x):
    print(x*2)
#res =lambda x:x*2
f1(f2,10)
def f1(sum,x,y):
    print(sum(x,y))
sum = lambda x,y:x+y
f1(sum,10,20)
def f1(biggest,x,y):
    print(biggest(x,y))
biggest=lambda x,y:x if x>y else y
f1(biggest,20,27)
def f1(num,z):
    print(num(z))
x = 'even'
y = 'odd'
num = lambda z:x if z%2==0 else y
f1(num,22)
x = int(input("enter the number"))
y = int(input("enter the number"))
z = int(input("enter the number"))
def f1(x,y,z,res,even_odd):
    print(res(x,y),'is biggest')
    print(even_odd(z))
res = lambda x,y: x if x>y else y
even_odd = lambda z:'even' if z%2==0 else 'odd'
f1(x,y,z,res,even_odd)
x = [10,11,12,13,14,15]
for i in x:
    if i%2==1:
        print(i)
x = [10,12,9,8,19]
y = [(x[i]**2)for i in range(len(x)) if i%2==1]
li = list(filter(lambda i:i,y))
print(li)
x = [10,5,6,8]
for i in x:
    print(i*2)
x = [10,5,6,8]
li = list(map(lambda i:i**2,x))
print(li)
x = [10,5,6,8]
y = [(x[i]**2)for i in range(len(x)) if i%2==1]
li = list(map(lambda i:i,y))
print(li)
x = [10,5,6,8]
y = [(x[i]**2)for i in range(len(x)) if i%2==0]
li = list(map(lambda i:i,y))
print(li)
x = [10,5,6,8]
y = [(x[i]+10)for i in range(len(x)) if i%2==1]
li = list(map(lambda i:i,y))
print(li)
###
welcome
20
bye
30
27
even
enter the number43
enter the number22
enter the number86
43 is biggest
even
11
13
15
[144, 64]
20
10
12
16
[100, 25, 36, 64]
[25, 64]
[100, 36]
[15, 18]


