import heapq
INF = int(1e9)

def solution(n, edge):
    distance = [INF] * (n + 1)
    heap = []
    graph = [[] for i in range(n+1)]
    for i, j in edge:
        graph[i].append(j)
        graph[j].append(i)
    def dijikstra(start):
        distance[start] = 0
        heapq.heappush(heap, (0, start))
        while heap:
            dis, st = heapq.heappop(heap)
            for i in graph[st]:
                if distance[i] > distance[st] + 1:
                    distance[i] = distance[st] + 1
                    heapq.heappush(heap, (distance[i], i))
    dijikstra(1)
    distance.pop(0)
    max_num = max(distance)
    answer = distance.count(max_num)
    return answer

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))