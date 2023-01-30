value = int(input('Введите до какого числа искать совершенное:'))
def perfect_numbers(n):
    sum = 0
    for x in range(1,n):
        if n%x == 0:
            sum += x
    return sum == n

print('Ваши совершенные числа:')
for i in range(1,value):
    if perfect_numbers(i):
        print(i)








