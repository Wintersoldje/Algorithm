# 문제

[14890번: 경사로](https://www.acmicpc.net/problem/14890)

# 풀이

차이가 1 이 나야하고 오르막과 내리막이 있을 수 있기 때문에 조금 까다로웠다.

k라는 변수를 활용해 k를 초기에 1로 두고 만약 경사로를 올라가야할 때 k값이 l보다 크다면 경사로를 만들 수 있기 때문에 k를 0으로 초기화 하고 반복문을 돈다.

만약 내리막일 경우는 k≥0 이면 k 를 -l로 초기화 해주고 내리막이 완성 되려면 반복문을 돌면서 k+=1을 해주기때문에 문제 없이 진행 될 수 있다.

이 부분이 어려웠다.

```python
n, l = map(int,input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

def solution(x, y, dx, dy):
    k = 1
    for _ in range(n-1):
        nx = x + dx
        ny = y + dy
        diff = maps[nx][ny] - maps[x][y]
        if abs(diff) > 1:
            return 0
        if diff == 1:
            if k >= l:
                k = 0
            else:
                return 0
        if diff == -1:
            if k >= 0:
                k = -l
            else:
                return 0
        k += 1
        x, y = nx, ny
    if k >= 0:
        return 1
    else:
        return 0

result = 0
for i in range(n):
    result += solution(0, i, 1, 0)
    result += solution(i, 0, 0, 1)

print(result)
```
https://jewin.notion.site/8e7fd8888ab64053b045e5fb3d77d1bb
