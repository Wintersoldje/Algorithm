# 문제

[코딩테스트 연습 - 여행경로](https://programmers.co.kr/learn/courses/30/lessons/43164)

# 풀이

처음에 문제를 접근할때 heapq만을 이용해서 풀으려 했지만 heap을 pop할때 문제가 생기는걸 알고 포기했다.. (시간 버림)

다시 처음으로 돌아가서 heapq를 사용하되 dfs를 사용해서 풀면 될 것이라고 생각했다.

우선 첫 출발이 "ICN"이기 때문에 ICN이 출발인 티켓을 먼저 heap에 넣는다. heap은 우선순위를 알파벳 순으로 설정해 두었다. 

그래서 heap을 보면서 heap의 도착지점을 다시 dfs의 인자로 넣어주면서 재귀를 돈다. 그러면서 dfs를 시작하는데, 종료조건 때문에 조금 해맸다. 

종료 조건이 맞으면 그 즉시 들어있는 list를 반환해 주어야 하는데, 그때는 flag값을 변경 시켜주어 dfs를 종료시키게 코드를 짰다. 

1. dfs에 ICN을 시작으로 넣고, tickets 리스트를 넣어준다.
2. dfs에서 티켓의 출발점과 dfs의 시작점이 일치하면 heap에 넣어준다.
3. 사용한 티켓은 티켓 리스트에서 지워주고 티켓의 도착지점을 dfs의 출발지점으로 넣어주어 재귀를 돈다.
4. 종료 조건이 충족되면 재귀를 멈추고 return한다.

```python
import heapq
flag = 0
a = ["ICN"]
def dfs(depart, tickets):
    global flag
    global a

    heap = []
    if flag == 1:
        return
    if len(tickets) == 0:
        flag = 1
        return

    for start, end in tickets:
        if start == depart:
            heapq.heappush(heap, (end))
    while heap:
        end = heapq.heappop(heap)
        tickets.remove([depart, end])
        a.append(end)
        dfs(end, tickets)
        if flag == 1:
            break
        a.pop()
        tickets.append([depart, end])
    return

def solution(tickets):
    dfs("ICN", tickets)
    return a

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
```
