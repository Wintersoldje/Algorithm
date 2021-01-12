def solution(numbers):
    num = list(map(str, numbers))
    num.sort(key= lambda x : x*3, reverse=True)
    print(num)
    return str(int(''.join(num)))

print(solution([6,10,2]))
