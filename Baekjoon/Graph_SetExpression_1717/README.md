# 문제

[1717번: 집합의 표현](https://www.acmicpc.net/problem/1717)

# 풀이

처음 문제를 보고 어떻게 접근해야할지 고민을 하다가, 단순히 graph를 이용해서 간선을 그어주고 연결된 graph를 탐색하여 해당 그래프에 포함이 되어 있으면 될 것 같다는 생각을 하였다. 그래서 flag가 1이 나오면 검사를 dfs로 검사를 하면서 들어 있으면 YES를 출력 하도록 했다. 하지만.. 결과는 시간초과& 틀림..

```python
n, m = map(int, input().split())
list = [list(map(int, input().split())) for i in range(m)]
graph = [[] for _ in range(n+1)]
result = 0
def input_graph(a, b):
    graph[a].append(b)
    graph[b].append(a)

def dfs(v, find_v, visited = []): # 
    global result
    visited.append(v)
    if find_v == v:
        result += 1
    for i in graph[v]:
        if not i in visited:
            visited = dfs(i, find_v, visited)
    return visited

for i in range(m): # m만큼 돌면서 flag가 0이면 간선을 연결..
    if list[i][0] == 0:
        if list[i][1] == list[i][2]:
            continue
        input_graph(list[i][1], list[i][2])
        # print(list[i])
    elif list[i][0] == 1:# flag가 1이면 dfs로 탐색해서 있으면 yes출력
        dfs(list[i][1], list[i][2])
        if result > 0:
            print("YES")
            result = 0
        else:
            print("NO")
```

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8247ac42-885b-491d-b1bf-d4046f47dac9/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8247ac42-885b-491d-b1bf-d4046f47dac9/Untitled.png)

어디서 틀린건지는 모르겠지만 노드 연결이 잘 안된 것 같다..

그래서 어떻게 풀어야 하는지 찾아봤다.

결론은 **Union-Find 알고리즘**을 사용해야한다고 한다.

1. parent 배열을 만들어줘서 처음에는 자기 자신을 부모로 설정해준다. 
2. flag가 0일때 union함수(합집합)를 이용해서 같은 그룹으로 묶어준다. 
    1. 부모 노드를 비교하여 부모 노드가 같으면 같은 집합
    2. 부모 노드가 다르면 두 집합을 합쳐 준다.
3. find함수를 이용해서 부모 노드가 누구인지 찾아준다.
    1. 재귀함수를 이용(종료 조건: 자기 자신이 루트 노드일때 까지 재귀)
4. flag가 1일때 find함수를 이용해서 부모 노드를 비교 한다. 
    1. 부모 노드가 같으면 "YES"
    2. 부모 노드가 다르면 "NO"

```python
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int,input().split())

parent = [0] * (N+1) # 부모 테이블 생성
for i in range(N+1): # 자기 자신을 부모로 설정
    parent[i] = i

# 루트 노드 찾는 함수
def find(a):
    if a == parent[a]: # 자기 자신이 루트 노드이면 a 반환
        return a
    p = find(parent[a]) # a의 루트 노드 찾기
    parent[a] = p # 부모 테이블 갱신
    return parent[a] # a의 루트 노드 반환

# a가 속해있는 집합과 b가 속해있는 집합을 합치는 연산
def union(a,b):
    a = find(a) # a의 루트 노드 찾기
    b = find(b) # b의 루트 노드 찾기

    if a == b: # a와 b의 루트 노드가 같으면 동일한 집합
        return
    if a < b: # a와 b의 루트 노드가 다르면 두 집합을 합치기
        parent[b] = a
    else:
        parent[a] = b

for _ in range(M):
    o, a, b = map(int,input().split()) # operation, 원소, 원소
    if o == 0: # o=0은 두 원소가 포함되어 있는 집합을 합치기
        union(a,b)
    elif o == 1: # 두 원소가 동일한 집합인지 판단
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')
```

*TIP 

import sys
sys.setrecursionlimit(10**6)

만약 재귀를 사용해서 풀어야 하는 문제라면, 위 코드를 상단에 쓰는 것은 선택이 아닌 필수이다. 파이썬의 기본 재귀 깊이 제한은 1000으로 매우 얕은 편이다. 따라서 재귀로 문제를 풀 경우 드물지 않게 이 제한에 걸리게 되는데, 문제는 코딩테스트 환경에서는 에러 메시지를 볼 수 없다는 것이다. 이 함정에 걸린 사람은 원인 미상의 런타임 에러를 붙잡고 몇십 분을 각종 테스트케이스를 넣어가며 씨름하겠지만, 그런다고 문제가 잡힐 리 없다. 결국에는 문제를 풀지 못한 채 제출하게 되고 내가 뭘 잘못했지 하는 끝없는 자괴감에 빠지게 되는 것이다.

실제로 올해 여러 번 코딩테스트에 응시하면서 위 코드 없이는 풀 수 없는 문제들을 꽤 많이 봤다. 그중에는 카카오 인턴 코딩테스트 문제도 있었다. 억을하게 문제를 틀리고 싶지 않다면 위 코드를 반드시 숙지해놓아야 할 것이다.
