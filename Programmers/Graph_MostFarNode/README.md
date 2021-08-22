# 문제

[코딩테스트 연습 - 가장 먼 노드](https://programmers.co.kr/learn/courses/30/lessons/49189)

# 풀이

한 지점에서 모든 노드까지의 최단 거리를 본 후 가장 먼 노드를 구해야한다. 따라서 다익스트라 알고리즘을 사용하면 된다.

1. 그래프의 방향성이 없기 때문에 연결되어 있는 모든 노드를 넣어준다.
2. 다익스트라 알고리즘을 사용하여 가장 먼 노드를 구해준다.
    1. 시작 노드를 지정해서 distance를 0으로 만들어준다.
    2. 연결 되어 있는 노드의 거리를 구하고 해당 거리가 distance 와 비교했을때 더 작으면 갱신해준다.
    3. 한 번 방문한 노드는 더 방문 안해도 최소 거리이다.
3. distance의 0번째 인덱스는 무시해도 되므로 0으로 바꿔주고 그 distance의 max값을 찾는다.
4. 리스트에서 max값의 개수를 세어준다.

```python
import heapq
INF = int(1e9)
def solution(n, edge):
    distance = [INF] * (n+1)
    heap = []
    graph = [[] for _ in range(n+1)]
    for s, e in edge:
        graph[s].append(e)
        graph[e].append(s)
    def dijikstra(start):
        distance[start] = 0
        heapq.heappush(heap, (distance[start], 1))
        while heap:
            dist, start = heapq.heappop(heap)
            for tmp in graph[start]:
                if distance[tmp] > dist + 1:
                    distance[tmp] = dist + 1
                    heapq.heappush(heap, (distance[tmp], tmp))
    dijikstra(1)
    distance[0] = 0
    max_num = max(distance)
    answer = distance.count(max_num)

    # print(distance)
    return answer

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
```
