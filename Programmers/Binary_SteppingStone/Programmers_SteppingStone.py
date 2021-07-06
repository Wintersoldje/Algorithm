def solution(distance, rocks, n):
    min = 0 #거리의 최소값
    max = distance #거리의 최대값
    answer = 0
    rocks.sort() # 거리 순으로 정렬
    while max >= min:
        count = 0
        tmp = 0
        for i in range(len(rocks)):
            mid = (min + max) // 2 #거리의 중간값을 잡고
            if mid > rocks[i] - tmp: #중간값이 답이라고 생각하고 돌을 뺴준다.
                count += 1
            else:
                tmp = rocks[i]
        if count <= n: #빼준 돌의 개수가 n보다 작거나 같으면 answer와 비교하여 mid가 더 크면 answer에 mid를 넣어줌
            if answer < mid:
                answer = mid
            min = mid + 1 #min을 mid+1로 갱신하고 다시 탐색
        else: #아니면 max를 mid-1로 갱신
            max = mid - 1

    return answer

print(solution(25, [2, 14, 11, 21, 17], 2))