# 문제

[코딩테스트 연습 - 섬 연결하기](https://programmers.co.kr/learn/courses/30/lessons/42861)

# 풀이

[Union-Find 알고리즘](https://www.notion.so/Kruskal-Algorithm-9ad2417d4d98422db332bd62650ed50b)을 사용하면 쉽게 구할 수 있다. 

1. Find함수를 정의한다.
    1. 이 함수는 Parents  배열에서 부모를 찾는 함수이다.
2. Union함수를 정의한다.
    1. 이 함수는 매개변수로 들어온 a,b의 부모를 연결해주는 함수이다.
3. costs 리스트를 2번째 인덱스인 거리를 기준으로 정렬해준다.
4. 정렬된 costs 리스트를 가지고 반복문을 돌면서 부모를 연결시켜준다.

```python
def find(target):
    global parents
    if target == parents[target]:
        return target
    return find(parents[target])

def union(a, b):
    global parents
    parent_a = find(a)
    parent_b = find(b)

    if parent_a > parent_b:
        parents[parent_a] = parent_b
    else:
        parents[parent_b] = parent_a

def solution(n, costs):
    global parents
    answer = 0
    parents = [i for i in range(n)]
    costs = sorted(costs, key=lambda x:x[2])
    for a, b, c in costs:
        if find(a) != find(b):
            union(a, b)
            answer += c
        print(parents)
        print(answer)
    return answer

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))
```

https://jewin.notion.site/90028c04e12c40499e1fa24f33cb729c
