def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    min = 0
    max = distance
    while min <= max:
        mid = (min+max) // 2
        tmp = 0
        tmp_max = distance
        count = 0
        for i in range(len(rocks)):
            if mid > rocks[i] - tmp:
                count += 1
            else:
                tmp = rocks[i]
            if i == len(rocks)-1:
                if tmp_max - tmp < mid:
                    count += 1
        if count <= n:
            # answer = mid
            min = mid+1
        else:
            max = mid-1
    return mid

print(solution(16, [4,8,11], 2))