###
write a python program for sum,product,evenodd,reverse,string,square,leapyear?
###
sum = lambda x,y:x+y
product =lambda x,y:x*y
x = sum(10,20)
print(x)
y = product(22,2)
print(y)
num1 = int(input("enter the number"))
num2 = int(input("enter the number"))
comp = lambda num1,num2:num1 if num1>num2 else num2
print(comp(num1,num2))
num = int(input("enter the number"))
x = 'even'
y = 'odd'
z = lambda num:x if num%2==0 else y
print(z(num))
x = input("enter the string")
reversed = lambda x:x[ : :-1]
print(reversed(x))
x = input("enter the string")
y = input("enter the string")
z = lambda x,y:x+y
print(z(x,y))
x = int(input("enter the number"))
y = int(input("enter the number"))
power = lambda x,y:x**y
print(power(x,y))
x = int(input("enter the number"))
z = lambda x:'leap year' if (x%4==0) and (x%100!=0 or x%400==0) else 'not a leap year'
print(z(x))
###
30
44
enter the number 32
enter the number34
34
enter the number23
odd
enter the stringhello
olleh
enter the stringhello
enter the stringhi
hellohi
enter the number6
enter the number7
279936
enter the number23
not a leap year
