def solution(numbers, target):
    answer = [0]
    for num in numbers:
        node_list = []
        for answer_node in answer:
            node_list.append(answer_node + num)
            node_list.append(answer_node - num)
        answer = node_list

    return answer.count(target)

print(solution([1,1,1,1,1], 3))