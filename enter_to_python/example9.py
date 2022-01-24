# Логические операции

# and, not, or - не путать с &, |, ^
# is, is not, in, not in

import numbers


a = -11<2 and 7 > 2
print(a)


b = -11<25 and 7 > 22
print(b)


c = 11 !=12
print(c)

d = 'ert'
e = 'rte'
print(d == e)

d = 'ert'
e = 'rte'
print(d == e)

f = [1,2,3]
g = [1,2,3]
print(f == g)

# Пример четверного неравенства. 
# Особенность Пайтона
h = 1<3<5<6
print(h)

number =  1
y = 2
x = 4
print(x<y>number)

f = 1 < 2 or 5 > 3
print(f)

# Поиск одного числа в массиве
f = [1,2,3,4]
print(2 in f)

# Поиск одного числа в массиве с отрицанием 
f = [1,2,3,4]
print(not 5 in f)

# Проверка четности числа

number = not f[0]%2 == 0
print(number == 0)






