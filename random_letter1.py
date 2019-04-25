import random
spisok=['самовар','весна','лето']
ch=random.choice(spisok)
cho=random.choice(ch)
lst=list(ch)
lst[ch.index(cho)]='?'
stroka=''.join(lst)
print(stroka)
w = input('Введите ваш ответ: ')
if w == cho:
    print('Победа')
else:
    print('Поражение')
    





        

