###
write aprogram for file input output create a file name details.txt write something about u more than 5 sentences read the content in console?
###
f = open('details.txt','w')
f.write(' hello\n')
f.write('i am deepika\n')
f.write('i am from chowdepalli\n')
f.write('i am learning python\n')
f.write('i am from cse ds department\n')
f.close()
f =open('details.txt','a')
f.write('welcome to python programming\n')
f.write('this is my file\n')
f.write('i am studying btech')
f.close()
f = open('details.txt','r')
lines = f.read()
print(lines)
f.close()
f = open('details.txt','r')
list1 = f.readlines()
print(list1[0])
f.close()
f = open('details.txt','r')
for i in f:
    print(i)
f.close()
f = open('sample.txt','w')
f.write('python\n')
f.write('welcome to python\n')
f.close()
f = open('sample.txt','a')
f.write('start learning python\n')
f.write('this is my file\n')
f.write('we are learning python')
f.close()
f = open('sample.txt','r')
lines = f.read()
print(lines)
f.close()
f = open('sample.txt','r')
list1 = f.readlines()
print(list1[1])
f.close()
f = open('sample.txt','r')
for i in f:
    print(i)
f.close()
###
i am deepika
i am from chowdepalli
i am learning python
i am from cse ds department
welcome to python programming
this is my file
i am studying btech
 hello

 hello

i am deepika

i am from chowdepalli

i am learning python

i am from cse ds department

welcome to python programming

this is my file

i am studying btech
python
welcome to python
start learning python
this is my file
we are learning python
welcome to python

python

welcome to python

start learning python

this is my file

we are learning python

