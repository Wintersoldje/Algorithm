def sum_list(l):
    count = 0
    for i in range(len(l)):
        tmp = int(l[i][0])
        count = count + tmp
    return count

def solution(bridge_length, weight, truck_weights):
    max_len = bridge_length
    pass_bridge = []
    passing_bridge = []
    num = len(truck_weights)
    count = 0
    while num != len(pass_bridge):
        count += 1
        if len(passing_bridge) > 0:
            if count - passing_bridge[0][1] == max_len:
                tmp, cnt = passing_bridge.pop(0)
                pass_bridge.append(tmp)
        if len(truck_weights) == 0:
            continue
        if len(passing_bridge) <= max_len and sum_list(passing_bridge) + truck_weights[0] <= weight:
            tmp = truck_weights.pop(0)
            passing_bridge.append([tmp,count])

    answer = count
    return answer

print(solution(100, 100,[10,10,10,10,10,10,10,10,10,10]))