# 문제

[코딩테스트 연습 - 네트워크](https://programmers.co.kr/learn/courses/30/lessons/43162)

# 풀이

union-Find로 풀이하면 쉽게 풀린다.

연결된 노드들의 그래프 list를 만들어주고 연결 되어 있으면 union으로 parent를 맞춰준다.

최종적으로 부모가 다른 애들이 다른 네트워크기 때문에 그 개수를 세어준다.

```python
def find(target):
    global parent
    if target == parent[target]:
        return target
    return find(parent[target])

def union(a, b):
    global parent
    parent_a = find(a)
    parent_b = find(b)
    
    if parent_a < parent_b:
        parent[parent_b] = parent_a
    else:
        parent[parent_a] = parent_b

def solution(n, computers):
    global parent
    answer = 0
    parent = [i for i in range(n)]
    graph = [[] for _ in range(n)]
    #그래프로 연결된 노드들 찾기
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and i != j:
                graph[i].append(j)
                graph[j].append(i)
                
    #부모가 다른 노드들 연결
    for i in range(len(graph)):
        for j in graph[i]:
            if find(i) != find(j):
                union(i, j)
                
    #개수 새기
    list_answer = set()
    for i in range(n):
        list_answer.add(find(parent[i]))
    answer = len(list_answer)
        
    return answer
```

https://jewin.notion.site/8f07655e6aef4ebb9d6f43b06c4333ec
