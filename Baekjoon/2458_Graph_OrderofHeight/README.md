# 문제

[2458번: 키 순서](https://www.acmicpc.net/problem/2458)

# 풀이

모든 노드에서 모든 노드로 가는 비용을 구해야 하는 문제입니다. 따라서 이 문제는 [플로이드 와샬 알고리즘](https://www.notion.so/6ff0081f881e4feaadc0310f3a4568bd)을 사용해야 합니다.

플로이드 와샬 알고리즘이란 거쳐가는 정점을 기준으로 알고리즘을 수행합니다.

### 풀이 방법

1. 이차원 배열을 만들어서 연결이 된 노드는 1로 표시를 해주고, 연결이 되지 않은 부분은 INF로 처리해준다.
2. 플로이드 와샬 알고리즘을 사용한다.
    1. 노드가 노드끼리 거쳐갈때와 거치지 않고 바로 갈때를 비교하여 계산을 해준다. 
    2. 즉, 거치는 점을 i라고 하고 출발점을 j, 도착점을 k라고 할때 j→i + i→k < j→k 가 성립하면 앞의 비용으로 갱신해준다.
3. 완성된 테이블에서 i→j 와 j→i 가 INF가 아니라면 카운트를 해주고, 그 카운트 값이 자신을 제외한 n-1번이 되면 answer에 +1을 해준다.

```python
n, m = map(int, input().split())
INF = int(1e9)
list = [[INF] * n for i in range(n)]
# for i in range(n):
#     list[i][i] = 0

for i in range(m):
    a, b = map(int, input().split())
    list[a-1][b-1] = 1

for i in range(n):#거쳐가는 노드
    for j in range(n): #시작 노드
        for k in range(n): #도착 노드
            if list[j][i] + list[i][k] < list[j][k]:
                list[j][k] = list[j][i] + list[i][k]
answer = 0
# print(list)
for i in range(n):
    count = 0
    for j in range(n):
        if list[i][j] != INF or list[j][i] != INF:
            count += 1
    if count == n-1:
        answer += 1

print(answer)
```
