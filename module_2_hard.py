n = int(input('Введите число из первого поля '))
dividers_list = []
divider = 2
while divider <= n:
    if n % divider == 0:
        dividers_list.append(divider)
        divider += 1
    else:
        divider += 1
result = []
for i in range(1, int(dividers_list[-1])//2+1):
    for j in dividers_list:
        if i < j-i:
            result.append(i)
            result.append(j - i)
print('Ваш пароль:')
print(*result)
