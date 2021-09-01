def solution(N, stages):
    answer = []
    stages.sort()
    n = len(stages)
    list_tmp = []
    for i in range(1, N+1):
        count = 0
        while True:
            if len(stages) == 0:
                break
            if stages[0] <= i:
                stages.pop(0)
                count += 1
            else:
                break
        list_tmp.append(count)
    num = 0
    list_rank = []
    for i in range(N):
        if list_tmp[i] == 0:
            list_rank.append((i+1, 0.0))
            continue
        else:
            tmp = n - num
            list_rank.append((i+1, list_tmp[i]/tmp))
            num += list_tmp[i]
    list_rank = sorted(list_rank, key=lambda x:x[1], reverse=True)
    for a,b in list_rank:
        answer.append(a)
    return answer

print(solution(4,[4,4,4,4,4]))