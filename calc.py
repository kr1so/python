# Недокалькулятор

# print('Введите 1 число')
# a = int(input())
# print('Введите 2 число')
# b = int(input())
# c = a*b
# d = a/b
# e = a+b
# f = a-b
# print(f'Первое число = {a}\nВторое число = {b}')
# print(f'Результат умножения = {c}')
# print(f'Результат деления = {d}')
# print(f'Результат сложения = {e}')
# print(f'Результат вычитания = {f}')

# Ещё результат можно представить так:
# print(f'{a}+{b}={c}')
# print(f'{a}+{b}={d}')
# print(f'{a}+{b}={e}')
# print(f'{a}-{b}={f}')
print('Введите 1 число')
a = int(input())
print('Введите операцию, которую нужно произвести')
c = input()
print('Введите 2 число')
b = int(input())
if c == "+":
    d = a+b
    print(d)
elif c == "-":
    d = a-b
    print(d)
elif c == "/":
    d = a/b
    print(d)
elif c == "*":
    d = a*b
    print(d)
else:
    print("Неверные данные. Попробуйте ещё раз")
