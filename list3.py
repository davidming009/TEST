list1=list(input("輸入1："))
list2=list(input("輸入2："))
m=0
n=0

for a in range(len(list1)):
    if list2[a] == list1[a]:
        m=m+1
    elif list1[a] in list2:
        n=n+1
print(m,'a',n,"b")


