# import sys
# input = sys.stdin.readline
INF = int(1e9) #무한 수 설정 10억

v, e = map(int, input().split())
start = int(input()) # 시작점
graph = [[] for i in range(v+1)]
visited = [False] * (v+1)

distance = [INF] * (v+1)#최단 거리 테이블 생성

for _ in range(e): # 모든 노드와 간선 입력
    a, b, c = map(int, input().split()) #a: 출발 b:도착 c: 간선
    graph[a].append((b,c))

def get_smallest_node(): #distance 테이블에서 최단 경로를 찾는 함수
    min_value = INF
    index = 0 #가장 거리가 짧은 노드의 인덱스
    for i in range(1, v+1):
        if not visited[i] and distance[i] < min_value: # 방문하지 않은 노드 중에서(방문한 노드는 이미 최소 노드임)
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0 #시작 노드는 거리 0
    visited[start] = True # 시작 노드 방문 표시
    for j in graph[start]: # 시작 노드에서 뻗어 나오는 간선들 거리 테이블에 등록
        distance[j[0]] = j[1]
    for i in range(v-1): # 모든 노드의 수만큼 돌면서 갱신
        smallest = get_smallest_node() # 방문하지 않은 노드 중 거리가 가장 짧은 노드
        visited[smallest] = True
        for j in graph[smallest]:
            weight = distance[smallest] + j[1]
            if weight < distance[j[0]]: #cost 값이 기존의 거리 보다 작으면 갱신
                distance[j[0]] = weight

dijkstra(start)

for i in range(1, v+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])


