# 문제

[14891번: 톱니바퀴](https://www.acmicpc.net/problem/14891)

# 풀이

회전을 하기 때문에 **deque의 rotate함수를 이용**하면 쉽게 풀릴 수 있다. 

deque를 이용하여 gear 리스트를 만든다.

그리고 다른 기어와 접하는 부분인 왼쪽과 오른쪽 기어를 저장해둔다. 

그리고 operation 기준 왼쪽과 오른쪽으로 나뉘어져서 이동한다.

왼쪽은 만약 접하는 부분이 다르면 tmp_6을 리셋해주고 방향은 반대 방향으로 바꿔주고 rotate를 이용해 돌려준다.

오른쪽도 마찬가지이다.

```python
from collections import deque

gear = [deque(map(int, input())) for _ in range(4)]
opers = deque(list(map(int,input().split())) for _ in range(int(input())))

while opers:
    num, dir = opers.popleft()
    num -= 1
    tmp_2 = gear[num][2]
    tmp_6 = gear[num][6]
    gear[num].rotate(dir)
    tmp_dir = dir

    #왼쪽 방향
    for i in range(num-1, -1, -1):
        if gear[i][2] != tmp_6:
            tmp_6 = gear[i][6]
            dir = dir * -1
            gear[i].rotate(dir)
        else:
            break
    dir = tmp_dir
    for i in range(num+1, 4):
        if gear[i][6] != tmp_2:
            tmp_2 = gear[i][2]
            dir = dir * -1
            gear[i].rotate(dir)
        else:
            break

answer = 0
for i in range(4):
    if gear[i][0] == 1:
        answer += (2**i)
print(answer)
```
https://jewin.notion.site/a594074d589e42edaad197cdf967573e
