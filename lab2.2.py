#Бинарний пошук
#Курдупов Олексій 122-Г
import numpy as np                  
import random
masiv1=np.array(range(1,15))  #Создаєм масив для провірки правельності нашого пошуку
print(masiv1)                  
x=int(input('Введіть елемент який будемо шукати'))#якщо корстувач веде більше 14,елемент не буде найдений
R=len(masiv1)-1 #Кінець масиву
L,count,k=0,0,0, #Начало масива,счетчик для порівняння,і змінна для позиції числа
flag=False
while L<=R and not flag :
    k=(L+R)//2 #Якщо ввести 9,При первшій ітерації,к=6,при другій к=10 при третій к =8
    count+=1   #счетчик ітерацій
    if masiv1[k]==x:
        flag=True
    elif masiv1[k]<x:
        L=k+1
    else:
        R=k-1
if not flag:
    print('Елемента немає')
else:
    print(f'Елемент знайден на позиції {k} за {count} порівнянь')

#Робота з рандомними числами
masiv2=np.zeros(20,dtype=int)
for i in range(20):
    masiv2[i]=random.randint(-10,10)
print(masiv2)
R1=len(masiv2)-1 #Кінець масива
L1,count1,k1=0,0,0, #Начало масива,счетчик для порівняння,і змінна для позиції числа
flag1=False
while L1<=R1 and not flag1 :
    k1=(L1+R1)//2 
    count1+=1   #счетчик ітерацій
    if masiv2[k1]==x:
        flag1=True
    elif masiv2[k1]<x:
        L1=k1+1
    else:
        R1=k1-1
if not flag1:
    print('Елемента немає')
else:
    print(f'Елемент знайден на позиции {k1} за {count1} порівнянь')

