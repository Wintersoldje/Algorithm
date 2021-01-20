n = input()

list_num = ''.join(n)
result = 1
i = 0
while len(list_num) != i:
    if int(list_num[i]) == 0:
        tmp = int(list_num[i]) + int(list_num[i+1])
        if i == 0:
            result = tmp
        else:
            result *= tmp
        i += 2

    else:
        result *= int(list_num[i])
        i += 1

print(result)