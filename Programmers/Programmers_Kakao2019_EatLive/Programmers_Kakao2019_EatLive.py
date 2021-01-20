def solution(food_times, k):
    pair_list = []
    total_time = 0
    # pair_list에 [음식번호, 음식 시간]으로 넣음
    for i in range(len(food_times)):
        pair_list.append([i, food_times[i]])
        total_time += food_times[i]

    # total_time 보다 k가 작으면 -1 return
    if total_time <= k:
        return -1

    # 음식 시간으로 정렬
    pair_list.sort(key=lambda x: x[1])

    # 지울 시간 저장
    delTime = pair_list[0][1] * len(food_times)

    # 지울 시간이 k보다 작으면 delTime 리셋
    i = 1
    while delTime < k:
        k -= delTime
        delTime = (pair_list[i][1] - pair_list[i - 1][1]) * (len(pair_list) - i)
        i += 1

    # 마지막 번호로 정렬해준 후 나머지 연산으로 음식 번호 return
    pair_list = sorted(pair_list[i - 1:], key=lambda x: x[0])
    return pair_list[k % len(pair_list)][0] + 1


import heapq
def solution(food_times, k):
    if sum(food_times) <=k:
        return -1

    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))

    sum_value = 0 #먹기 위해 사용한 시간
    previous = 0 #직전에 다 먹은 음식 시간

    length = len(food_times)

    #sumvalue + (현재 음식 시간 - 이전 음식 시간) * 현재 음식 개수와 K 비교
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1
        previous = now

    #남은 음식 중에서 몇 번째 음식인지 확인하여 출력
    result = sorted(q, key=lambda x:x[1]) #음식 번호 기준으로 정렬
    return result[(k-sum_value) % length][1]