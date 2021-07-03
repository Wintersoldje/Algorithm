def solution(n, times):
    left = 1 #대기 하는 시간의 최소시간
    right = max(times) * n #대기하는 시간의 최대시간
    answer = 0
    while right >= left:
        mid = (right + left) // 2 #최대시간과 최소시간의 중간값 (한 심사위원에게 주어진 시간)
        tmp = 0
        for time in times:#각자 심사위원이 mid라는 시간동안 모두 수행해서 할 수 있는 시간
            tmp += mid // time
            if tmp >= n:
                break
        if tmp >= n:
            answer = mid
            right -= 1
        else:
            left += 1

    return answer
