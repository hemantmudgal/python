p=input('Enter name: ').split(' ')
a=[]
for i in p:
    a.append(i[0])
for i in a:
    print('{}.'.format(i),end="")
