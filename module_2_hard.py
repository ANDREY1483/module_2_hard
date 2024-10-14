first_number = int(input('Введите число от 3 до 20: '))
result = []
for i in range(1, 21):
    for j in range(2, 21):
        sum = i + j
        if sum > 0 and first_number % sum == 0:
            if j not in result:
                result.append(i)
                result.append(j)


print(f'Подходящие пары{result}')
print("".join(result))
