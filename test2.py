import os
print(os.getcwd())

x=open("TXT.txt",'r')
z=x.readline()
z1=z.replace('\n','')
z2=z1.split(',')
print(z2)
print()

while z1!='':
    z1=x.readline()
    a=z1.replace('\n','')
    a2=a.split(',')
    print(a2)
x.close()