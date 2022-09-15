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
with open ("dataset_3363_2.txt") as file :
    stroka = file.readline()

import re
#stroka = 'a1b1c1e0b1'
letter=[]
numbs=[]
stroka=stroka.strip()
letter+=re.split('\d+' , stroka)
numbs+=re.split('\D+', stroka)
letter.pop()                                                    #Напишите программу, которая считывает из файла строку, соответствующую тексту, сжатому с помощью кодирования повторов, и производит обратную операцию, получая исходный текст.
numbs.pop(0)
stroka=""
for i in range(len(numbs)):
    numbs[i]=int(numbs[i])
    letter[i]*=numbs[i]
    stroka+=letter[i]
print(stroka)
with open ('data_clear.txt',"w") as file:
    file.write(stroka)
''''''
import re
stroka_low=[]

sorted_dictionary={}
with open ("3.txt") as file : #открыть файл
    for i in file:
        i=i.strip().lower().split(' ')  # удалить пробелы вначале и конце(убрать \n), разделить строку и вернуть подстроки в виде списка
        stroka_low+=i    #добавляет элементы к списку stroka для последущей обработки

stroka_size=len(stroka_low) #размер строки
dictionary={}
for i in range(stroka_size):  
    if stroka_low[i] not in dictionary:
        dictionary[stroka_low[i]]=stroka_low.count(stroka_low[i]) #в созданный словарь записываем: key=слово, value=кол-во этих слов в файла
max_value= max(dictionary.values()) #находим максимальное кол-во слов в value словаря
max_dictionary = {key: value for key, value in dictionary.items() if value == max_value} #создаём словарь со словами имеющими одинаково максимальное значение
if len(max_dictionary)>1: #если в словаре максимальных значений больше одного значения
    #выбираем лексикографически первое имя ключа
    sorted_dictionary=dict(sorted(max_dictionary.items())) #сортируем словарь по лексикографическому значению ключа
    itemss = list(sorted_dictionary.items())#переводим словарь в список для вытаскивания первого (максимального) отсортированного значения по индексу. !!! происходит так что получаем список а внутри него кортежи с ключом и значением из словаря
    del itemss[1:] #удаляем всё кроме первого из списка
    itemss=dict(itemss)#переводим список в словарь
    x=''.join('{}'.format(key) for key in itemss.keys())
    y=''.join('{}'.format(key) for key in itemss.values())
    z=x+' '+y
else:
    x=''.join('{}'.format(key) for key in max_dictionary.keys())
    y=''.join('{}'.format(key) for key in max_dictionary.values())
    z=x+' '+y
with open ('data_clear2.txt',"w") as file:
    file.write(z)
'''

'''
numb=int(input())
print("Следующее за числом",numb,"число:",numb+1)
print("Для числа",numb, "предыдущее число:",numb-1)

'''
'''import re
marks_osn=[]
only_names=[]

sr=0
with open ("4.txt",encoding='utf-8') as file : #открыть файл
    for i in file:
        i=i.strip().lower().split(';')  # удалить пробелы вначале и конце(убрать \n), разделить строку и вернуть подстроки в виде списка
        marks_osn+=i    #добавляет элементы к списку stroka для последущей обработки
stroka_size=len(marks_osn) #размер строки
marks_numbs=[]
for i in range(0,stroka_size,4):
    marks_osn[i+1]=int(marks_osn[i+1])
    marks_osn[i+2]=int(marks_osn[i+2])
    marks_osn[i+3]=int(marks_osn[i+3])
    only_names.append(marks_osn[i]) #имена учеников по порядку
    marks_numbs.append(marks_osn[i+1:i+4]) #изначальные оценки по порядку only_names
marks_sr=[]  #список для среднего показателя оценок каждого по очереди организуемой: only_names                       #средняя оценка по каждому ученику
for i in marks_numbs:
    sr=0
    for j in i:
        sr+=j
    marks_sr.append(sr/3)  
    marks_sr.append("\n")  
#ср баллы по придметам:
def schitalka(n):    #считает среднее значение по предметам (n индекс предмета из marks_numbs:  0=математика, 1=физика, 2=русс яз)
    cnt=0
    sr=0
    for i in marks_numbs:
        for j in i[n:n+1]:
            sr+=j
        cnt+=1
    return sr/cnt
math=schitalka(0)
fizika=schitalka(1)
russki=schitalka(2)

with open ('data_clear2.txt',"w") as file:
    for i in marks_sr:
        file.write(str(i))
    file.write(str(math))
    file.write(str(" "))
    file.write(str(fizika))
    file.write(str(" "))
    file.write(str(russki))'''

'''import math
print(2*float(input())*math.pi)'''
import sys
s = ''
s2 = ''
for i in range(1,len(sys.argv)):
    s = s + sys.argv[i]+' '
s2 = s
print(s2,end=' ')














