# 문제

[1753번: 최단경로](https://www.acmicpc.net/problem/1753)

# 풀이

문제를 보고 다익스트라 알고리즘을 적용해야 겠다고 생각을 했습니다. 

다익스트라 알고리즘을 이용하기 위해 다익스트라 함수를 만들었습니다. 

```python
def dijkstra(start):
    distance[start] = 0
    heapq.heappush(heap, (0, start))
    while heap:
        weight, now = heapq.heappop(heap)
        for next, n_weight in graph[now]:
            cost = weight + n_weight
            if distance[next] > cost:
                distance[next] = cost
                heapq.heappush(heap, (cost, next))
```

 이 함수는 heap을 이용했습니다. heapq는 우선순위 큐와 비슷한데 우선순위 숫자가 작을수록 top에 존재한다. 그래서 heap이 빌때까지 돌면서 heap에 들어있는 노드 중 비용이 가장 적은 노드에서 다음 노드의 cost를 계산해주고 기존의 비용보다 적으면 갱신을 해준다.  

### 코드 순서

1. 입력으로 받은 그래프를 비용을 포함해서 저장해준다.
2. 비용 테이블을 모두 최대 (INF)로 설정해둔다.
3. 다익스트라 알고리즘을 사용한다.
    1. 시작 지점은 비용을 0으로 갱신해주고, heap에 비용을 우선순위로 넣어준다. (비용, 노드)
    2. 그리고 heap이 빌때까지 돌면서 heap에 들어있는 노드를 뽑아준다. 
    3. 뽑힌 노드는 가장 비용이 적은 노드이기 때문에 뽑힌 노드와 연결되는 노드를 보면서 비용 테이블의 값과 cost = 현재 weight + 그 전의 weight를 계산 해주면서 cost가 더 적으면 갱신을 해주고 heap에 넣어준다.
    4. b,c를 반복해준다.
4. 최종적으로 모든 비용 테이블을 확인해서 시작지점에서 모든 노드를 가는 최소 비용을 출력해준다.

```python
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
```
