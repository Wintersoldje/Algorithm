def solution1(m, k, list_num):
    answer = 0
    count = 0
    list_num.sort()
    first = list_num[len(list_num)-1]
    second = list_num[len(list_num)-2]

    print(list_num)
    for i in range(m):
        if count == k:
            answer += second
            count = 0
        else:
            answer += first
            count += 1
    return answer

def solution2(m, k, list_num):
    answer = 0
    list_num.sort()
    first = list_num[len(list_num)-1]
    second = list_num[len(list_num)-2]

    count = m // (k+1) * k +(m % (k+1))

    answer += count * first
    answer += (m - count) * second

    return answer

print(solution2(8,3,[2,4,5,4,6]))
