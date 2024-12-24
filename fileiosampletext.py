###
create a file sample.txt, write first two lines using 'w' and next three lines using 'a' .read the content from file using the three read method?
###
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

