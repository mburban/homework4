# Пользователь вводит 4-х значное, целое число. Необходимо его перевернуть. Например: вводите 1234 ==> получаем 4321.
# Примечание:
# использовать строки, срезы, сторонние функции и выводить число по одной цифре не разрешено. Можно имполььзовать только
# арифметические операторы.

number = int(input('Input the number: '))
x = 0
x = x * 10 + number % 10
number = number // 10
x = x * 10 + number % 10
number = number // 10
x = x * 10 + number % 10
number = number // 10
x = x * 10 + number % 10
number = number // 10
print('Inverted number is:', x)
