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


a=int(input())
x=0
for i in range(a):
    x+=1
    for z in range(a-x):
        print("*", end="")
    for j in range (i):
        print(' ', end="")
    print(' ')


