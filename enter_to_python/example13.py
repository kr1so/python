# Управляющие конструкции: while

original_number = 1445
inverted_number = 0
while original_number != 0:
    inverted_number = inverted_number * 10 + (original_number%10)
    original_number //= 10
    print(original_number)
else:
    print('вот что получилось!')

print(inverted_number)

