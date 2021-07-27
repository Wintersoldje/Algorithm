# 문제

[코딩테스트 연습 - 단어 변환](https://programmers.co.kr/learn/courses/30/lessons/43163)

# 풀이

문제를 보고 처음에는 BFS로 풀면 될것 같다고 생각하였는데, BFS로 돌면 자식노드에 중복으로 들어가야 하는 부분이 따로 처리를 해줘야 한다. 그래서 조금 복잡해질 것 같아서 DFS로 풀었다.

DFS의 인자로는 시작, 타겟, 단어배열, 방문 배열, 그리고 count값이 들어간다.

그리고 문자 하나만 달라야 단어를 변환할 수 있기 때문에 변환 가능 여부를 확인해 주는 Check함수를 따로 만들었다. 

그래서 DFS의 종료조건은 시작과 타겟이 같을때 이고, 단어 리스트에서 방문하지 않은 노드들을 보고, check의 리턴값이 true이면 dfs를 돌게 해주었다. 근데 여기서 count값을 1증가 시켜줘야한다. 그래서 비교한 모든 count의 최소값을 answer로 넣어주고, 그 answer가 답이 된다.

1. target이 단어 리스트 안에 없으면 0을 리턴한다.
2. 시작, 타겟, 단어리스트, 방문한 노드를 넣어두는 리스트, count값을 인자로하는 dfs를 만들어준다.
3. 단어에서 문자 하나만 달라야 변환 할 수 있기 때문에 문자 하나만 다른지 확인하는 check함수를 만들어준다.
4. dfs에서 종료조건은, target과 begin이 같을때 종료해줘야한다.
5. 방문한 노드는 방문 리스트에 넣어주고, dfs를 도는데 dfs의 리턴값인 count의 최소값이 답이 되도록 해준다.

```python
def dfs(b, t, w, v, c):
    answer = int(1e9)
    if b == t:
        return c
    for i in w:
        if i not in v:
            if check(i, b):
                v.append(b)
                answer = min(answer, dfs(i, t, w, v, c+1))
                v.pop()
    return answer

def check(a, b):
    count = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            count += 1
    if len(a) - count == 1:
        return True
    return False

def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    visited = []
    answer = dfs(begin, target, words, visited, 0)
    return answer

# print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]	))
# print(solution("hit", "cog",["hot", "dot", "dog", "lot", "log"]))
```
