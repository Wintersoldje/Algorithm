# 문제

[코딩테스트 연습 - 순위](https://programmers.co.kr/learn/courses/30/lessons/49191)

# 풀이

1. **[플로이드 와샬 알고리즘](https://www.notion.so/6ff0081f881e4feaadc0310f3a4568bd)**을 사용한다.
    1. 예를 들면 A가 B를 이기고 B가 C를 이긴다면 A가 C를 이긴다. 라는 알고리즘
    2. k가 거쳐가는 노드 i 가 시작 노드 j가 끝 노드
2. 행열 위치 바꾼 부분(A vs B or B vs A)하나라도 성립하면 count 해준다.
3. count가 자신과의 대결을 제외한 n-1이라면 answer += 1

```python
def solution(n, results):
    answer = 0
    vs = [[-1] * n for _ in range(n)]
    for a,b in results:
        vs[a-1][b-1] = 0
    #플로이드와샬 알고리즘을 사용하여 거쳐가는 노드를 계산
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if vs[i][k] == 0 and vs[k][j] == 0:
                    vs[i][j] = 0
		# 행열의 위치를 바꾼 대상과 둘중 하나라도 대결이 되어 있으면 참
    for i in range(n):
        count = 0
        for j in range(n):
            if vs[i][j] == 0 or vs[j][i] == 0:
                count += 1
        if count == n-1:
            answer += 1
    return answer
```
https://jewin.notion.site/d85a0ceafb834598a8156ec8d02a9bb5
