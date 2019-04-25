import random
n = random.uniform(1,4)
m = int(input('Введите загаданное число от 1 до 4: '))
if m > n:
    print('Победа!')
elif m < n:
    print ('Загаданное число больше')
elif m > n:
    print ('Загаданное число меньше')