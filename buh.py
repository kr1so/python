print("Код-рассчет")
print("Введите свой оклад. Пример: 24000")
oklad = int(input())
print("Введите количество дней по производственному календарю")
mounth_day = int(input())
print("Введите количество отработанных дней с 1 по 15 число")
work_day = int(input())
payment = (oklad/mounth_day)*work_day
print(payment)

