import random

num = random.randint(1, 100)
print('Добро пожаловать в числовую угадайку')
while 0 == 0:
    n = int(input())
    if n > num:
        print('Слишком много, попробуйте еще раз')
        continue
    elif n < num:
        print('Слишком мало, попробуйте еще раз')
        continue
    elif n == num:
        print('Вы угадали, поздравляем!')
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
        break