def solution(brown, yellow):
    answer = []
    for i in range(1, 1+yellow):
        if yellow % i == 0:
            a = yellow / i
            if a >= i:
                if brown == (i+2) * 2 + 2 * a:
                    return [int(a+2), i+2]
            elif a < i:
                if brown == (a+2) * 2 + 2 * i:
                    return [i+2, int(a+2)]
    return answer

print(solution(10,2))