# 문제

[1922번: 네트워크 연결](https://www.acmicpc.net/problem/1922)

# 풀이

모든 노드가 연결되어있다는 문제 조건이 있고 모든 컴퓨터를 연결하는 최소 비용을 구하는 문제이다. 

따라서 처음에는 다익스트라 알고리즘을 사용하여 구하려고 했지만 다익스트라 알고리즘은 시작 노드와 종료 노드를 줘서 최소비용의 최단 거리를 구하는 문제이기 때문에 모든 노드를 거쳐가지 않아서 불가능하다.

따라서 다른 알고리즘을 찾아보다가 크루스칼 알고리즘이 있다는 것을 알았다. 크루스칼 알고리즘이란, **가장 적은 비용으로 모든 노드를 연결하기 위해 사용하는 알고리즘**이다. 따라서 문제 조건에 부합하므로 크루스칼 알고리즘을 이용해서 풀어야 한다. 

1. Union-Find 알고리즘을 적용시켜 각 노드의 부모 노드를 자기 자신으로 처음에 지정해준다.
2. find가 불리면 재귀함수를 돌면서 부모 노드를 찾아준다.
3. 부모 노드가 다를때는 합집합(Union)을 해주고, 해당 cost 즉 비용을 더해준다.

```python

n = int(input())
m = int(input())
parent = [i for i in range(n+1)]
list = [list(map(int, input().split())) for _ in range(m)]
result = 0

list.sort(key=lambda x:x[2])# 간선의 크기를 기준으로 오름차순 정렬 해준다. 
# print(list)

def find(target): #find로 부모 노드를 찾아준다.
    if target == parent[target]:
        return target
    return find(parent[target])

def union(a, b): #부모 노드가 다를때 부모 노드를 같게 해줌으로서 그룹을 연결시켜준다.
    a = find(a)
    b = find(b)
    if a < b:
        parent[a] = parent[b]
    else:
        parent[b] = parent[a]

for i in range(m):
    a, b, c = list[i]
    if find(a) != find(b): #부모 노드가 다를때 union을 불러주고 result에 비용을 더해준다.
        union(a,b)
        result += c

print(result)
```

notion: https://www.notion.so/jewin/f43c07977f39436fa07742558e23cd96
