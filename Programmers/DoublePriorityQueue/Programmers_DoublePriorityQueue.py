import heapq
def solution(operations):
    answer = []
    heap1 = []
    heap2 = []
    len = 0
    for i in operations:
        a, b = i.split(" ")
        b = int(b)
        if a == "I":
            len += 1
            heapq.heappush(heap1, b)
            heapq.heappush(heap2, -b)
        elif a == "D":
            if len <= 0:
                continue
            len -= 1
            if b == 1:
                heapq.heappop(heap2)
            elif b == -1:
                heapq.heappop(heap1)
    if len == 0:
        answer.append(0)
        answer.append(0)
    else:
        answer.append(heap1[0])
        answer.append(-heap2[0])
    answer.sort(reverse=True)
    return answer

print(solution(["I -1","I -1","I 1","D 1"]))