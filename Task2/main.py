# Найдите сумму цифр трехзначного числа.

a = int(input('Введите трехзначное число: '))
sum = 0

while a // 1000 > 0 :   
     print('Число не трехзначное')
     a = int(input('Введите трехзначное число: '))

x=0
while a > 0:
    x = a % 10
    sum += x
    a //= 10

print(f'Сумма цифр трехзначного числа равна: {sum}')
