import heapq

def solution(scoville, K):
    heap = []
    count = 0
    for i in scoville:
        heapq.heappush(heap, (i))

    while heap:
        print(heap)
        num1 = heapq.heappop(heap)
        if num1 >= K:
            return count
        if len(heap) == 0:
            return -1
        num2 = heapq.heappop(heap)
        heapq.heappush(heap, num1+(num2*2))
        count += 1

    return count

print(solution([1, 2, 3, 9, 10, 12]	, 7))