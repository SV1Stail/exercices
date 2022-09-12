""""
a = int(input())
#a=a**2
#print(a)
#a=a**3
#print(a)


if a>0 :
    print("положительное")
elif a<0:
    print("отрицательное")

"""
"""
a,b,c=input("вводить без пробелов: ")


a=int(a)
b=int(b)
c=int(c)
if (a<b) and (b<c):
    print("да")
else:
    print("нет")
"""
"""
n=int(input())
ost=n%5
print("остаток от деления",ost)

if n%5==0:
    print("остаток 0")
elif  n%5==1:
    print("остаток 1")
elif  n%5==2:
    print("остаток 2")
elif  n%5==3:
    print("остаток 3")
elif  n%5==4:
    print("остаток 4")

"""

"""
a=int(input())

for i in range(a):
    for j in range(15):
        print("*", end="")
    print(" ")
"""
"""
a="*"
for i in range(5):
        print(a*i)
x=[4,3,2,1]
for i in range(4):
    print(a*x[i])
p=" "
for i in range(4):
    print(p*i,a*x[i])
"""

"""

a=int(input())
x=0
for i in range(a):
    x+=1
    for z in range(a-x):
        print("*", end="")
    for j in range (i):
        print(' ', end="")
    print(' ')


for i in range(a):
    for j in range (i):
        print('*', end="")


    print(' ')

    """
'''
s=0
b=0
a=1
while a!=0:
    a=int(input())
    if a!=0:
        s+=a

print(s)'''
'''
a=int(input())
s=0
b=0
while    a!=0:
    s+=a
    b=int(input())
    a=b
print(s)
'''
'''
a=int(input())
b=int(input())
c=int(input())
d=int(input())
for    x    in    range(c,d+1):
    print('\t',x,end='')
print()
for    i    in    range(a,b+1):
    print(i,end='\t')
    for    j    in    range(c,d+1):
        print    (i*j,end='\t')
    print()
'''
"""
a,b= (int(i) for i in input().split())                                                                               ввод данных в строку одну строку с преобразованием в инт

print(a,b)
"""
'''
sum=0
kolvo=0
a=int(input())
b=int(input())
for i in range(a,b+1):
    if i%3==0:
        sum+=i
        kolvo+=1
print(sum/kolvo)
'''
'''
s=input()
inv=s[::-1]
if s==inv:
    print("true")
else:
    print("false")
    '''
'''
students = ['Ivan', 'Masha', 'Sasha',5]
students += ['Olga']
students += 'Olga'
for i in students:
    str(students[i])
s=sorted(students)
print(s)
'''
'''
a = [1, 2, 3]
b = a
a[1] = 10
b[0] = 20
a = [5, 6]
print(a)
'''
'''

a=[int(i)for i in input().split()]
s=0
z=[]

for x in range(len(a)):
    if len(a)==1:
        z=a
    elif x==0:
        z.insert(0,int(a[x+1])+int(a[-1]))
    elif x==(len(a)-1):
        z.append(int(a[0])+int(a[x-1]))
    else:
        z.append(int(a[x-1])+int(a[x+1]))

print(" ".join(map(str, z)))
'''
'''
a=[int(i)for i in input().split()]
z=[]

for i in range (len(a)):
    if a.count(a[i])>1 and a[i]not in z:
        z.append(a[i])
print (" ".join(map(str, z)))
'''
'''

summ=0
kvadrat=0
while True:
    a=int(input())
    summ+=a
    kvadrat+=a**2
    if summ==0:
        break
print(kvadrat)
'''
'''
s=[int(input())]
while sum(s)!=0:
    s.append(int(input()))
print(sum(i**2 for i in s))
'''
'''
a=[]
n=int(input())

for i in range(1,n+1):
    for x in range(i):
        if len(a)<n:
            a.append(i)

print(" ".join(map(str,a)))
'''
'''
lst=[int(i) for i in input().split()]
x=int(input())
new_lst=[]
flag=0
for i in range(len(lst)):
    if lst[i]==x:
        new_lst.append(i)
        flag=1
if flag==0:
    print("Отсутствует")
else:
    print(" ".join(map(str,new_lst)))
'''

'''
summa=0
mat=[]
while True:
    s=input()
    if s=="end":
        break
    mat.append([int(i) for i in s.split()])
for i in range(len(mat)):
    for j in range(len(mat[i])):
        x=int(mat[i][j-1]) + int(mat[i][j+1-len(mat[i])]) + int(mat[i-1][j]) + int(mat[i+1-len(mat)][j])
        print(x, end=' ')
    print()
'''
'''
n=int(input())
mat=[[0]*n for i in range(n)] 
for i in range(n):
    for j in range(n):
        print(n, end="")
    print(' ')
pr0int(mat)
'''
'''
n=int(input())
dx, dy = 1, 0
x, y = 0, 0
mat = [[None] * n for _ in range(n)]
for i in range(1, n**2+1):
    mat[x][y] = i
    nx, ny = x+dx, y+dy
    if 0 <= nx < n and 0 <= ny < n and not mat[nx][ny]:                                                                #улитка циклом FOR
        x, y = nx, ny
    else:
        dx, dy = -dy, dx
        x, y = x+dx, y+dy
for x in list(zip(*mat)):
    print(*x)
'''
'''
def f(n):
    return n * 10 + 5
    
print(f(f(f(10))))
'''
'''
def f(x):
    if x<=-2:
        return 1-(x+2)**2
    elif -2<x<=2:
        return (-x)/2
    elif 2<x:
        return (x-2)**2+1
print(f(4.5))
'''
'''
def modify_list(l):
    l_new=[]
    len_l=(len(l))
    for i in range(len_l):
        if l[i]%2==0:
            l[i]//=2
        else:
            l[i]="*"
    while l.count("*")!=0:
        l.remove("*")

lst = [1, 2, 3, 4, 5, 6]

print(modify_list(lst))
print(lst)
modify_list(lst)
print(lst)  
lst = [10, 5, 8, 3]
modify_list(lst)
print(lst) 
'''

'''

l=[i.lower() for i in input().split()]
dictionary={}
mn=set(l)
for i in mn:
    dictionary[i]=l.count(i)
for key, value in dictionary.items():
    print(key, value)
'''
'''
def update_dictionary(d, key, value):
    if key in d: #если key в списке
        d[key]+=[value]
    elif (key not in d ) and (key*2 in d): #если  key не в списке и key*2 в списке
        d[key*2]+=[value]
    elif (key not in d ) and (key*2 not in d ):
        d[key*2]=[value]

z = {1: ["один"],2: "два"}
d={}

print(update_dictionary(d, 1, -1))  # None
print(d)                            # {2: [-1]}
update_dictionary(d, 2, -2)
print(d)                            # {2: [-1, -2]}
update_dictionary(d, 1, -3)
print(d)   
'''
'''
dictionary={}
a=[]
for i in range (int(input())):
    a.append(int(input()))
for i in range (len(a)):
    if a[i] not in dictionary:
        dictionary[a[i]]=a[i]+1000       #f(a[i])
        print(dictionary[a[i]])
    else:
        print(dictionary[a[i]],'*')
'''
'''
with open ("") as file :
    stroka = file.readline()'''
import re
stroka = 'a1b1c1e0b'
letter=[]
numbs=[]
letter+=re.split('\d+' , stroka)
numbs+=re.split('\D+', stroka)
letter.pop()
numbs.pop(0)

for i in range(len(numbs)):
    numbs[i]=int(numbs[i])
    letter[i]*=numbs[i]
    print (letter[i],end='')



























