import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())
k = int(input())

distance = [INF] * (v+1)
graph = [[] for _ in range(v+1)]
heap = []

for i in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    distance[start] = 0
    heapq.heappush(heap, (0, start)) # (우선순위(가중치), 가야할 정점)
    while heap:
        weight, where = heapq.heappop(heap)
        # if distance[where] < weight:
        #     continue

        for next, n_weight in graph[where]:
            next_weight = weight + n_weight
            if next_weight < distance[next]:
                distance[next] = next_weight
                heapq.heappush(heap, (next_weight, next))
dijkstra(k)
for i in range(1, v+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])

