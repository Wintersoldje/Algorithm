def solution(progresses, speeds):
    answer = []
    stack = []
    for i in range(len(progresses)):
        if (100 - progresses[i]) % speeds[i] > 0:
            tmp = (100 - progresses[i]) // speeds[i] + 1
        else:
            tmp = (100 - progresses[i]) // speeds[i]
        stack.append(tmp)
    count = 1
    # print(stack)
    entry = stack.pop(0)
    # print(entry)
    while len(stack) != 0:
        if entry >= stack[0]:
            tmp = stack.pop(0)
            print(tmp)
            count += 1
            if len(stack) == 0:
                answer.append(count)
            continue
        answer.append(count)
        count = 1
        entry = stack.pop(0)
        if len(stack) == 0:
            answer.append(count)
    return answer

print(solution([100, 100, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))