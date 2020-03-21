#Лінійний пошук
#Курдупов Олексій 122-Г
import numpy as np                  
import random
masiv1=np.array(range(1,15)) #создаєм масив для провірки правельності нашого пошуку
print(masiv1)                  
x=int(input('Введіть елемент який будемо шукати'))#якщо корстувач веде більше 14,елемент не буде найдений
l=len(masiv1)
count=0   #Введемо щотчик для підрахунку кількості ітерацій і перебору нашого масиву
while count<l and masiv1[count]!=x:  #Вводим лінійний пошук
    count+=1
print('Кількість порівнянь',count)  #кількість порівнянь починається 0 в крок 1 значення в програмі потрібне  х-1 кроків
if count==l:
    print('Елемента немає')
else:
    print(f'На позициції {count} знайдений {x}')

#Робота з рандомними числами
masiv2=np.zeros(20,dtype=int)
for i in range(20):
    masiv2[i]=random.randint(-10,10)
print(masiv2)
l1=len(masiv2)
count2=0
while count2<l and masiv2[count2]!=x:  #Вводим лінійнй пошук
    count2+=1
print('Кількість порівнянь',count2)  #кількість порівнянь
if count2==l1:
    print('Елемента немає')
else:
    print(f'На позициції {count2} знайдений {x}')
