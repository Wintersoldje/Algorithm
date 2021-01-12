def solution(n, lost, reserve):
    #두벌 가져온 사람중에 잃어버린 사람은 뺀다
    reserve_set = set(reserve) - set(lost)
    #잃어 버린 사람중에 두벌 가져온 사람은 뺀다
    lost_set = set(lost) - set(reserve)
    #왼쪽사람 먼저 확인
    for i in reserve_set:
        if i-1 in lost_set:
            lost_set.remove(i-1)
        elif i+1 in lost_set:
            lost_set.remove(i+1)

    return n-len(lost_set)
