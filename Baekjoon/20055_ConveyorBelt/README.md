# 문제

[](https://www.acmicpc.net/problem/20055)

# 풀이

처음에는 문제가 제대로 이해가 되지 않았다. 로봇이 언제 올라가는 지 헷갈렸는데, 문제를 천천히 다시 읽어보고 하라는 대로 했다.

우선 컨베이어 벨트가 돌고 있기 때문에 이를 편하게 하기 위해서 deque에 rotate함수를 사용했다.

1. 컨베이어 벨트 내구도가 담긴 리스트를 deque에 넣어줬다.
2. 로봇은 N만큼의 길이에서만 있을 수 있기 때문에 N의 크기의 deque를 만들어줬다.
3. 반복문을 돌면서 문제에서 수행하라는 대로 해줬다.
    1. 벨트와 로봇의 위치를 이동시킨다. (이때 로봇의 마지막 위치는 떨어져야 하므로 0으로 표시)
    2. 앞으로 갈 수 있는 로봇을 들어온 순서대로 확인해준다.
        
        (조건 : 로봇이 있는지 확인, 가려고 하는 컨베이어 벨트의 내구도가 1이상인지, 가려고 하는 위치에 로봇이 없는지)
        
        1. 조건에 부합하다면 로봇을 옮겨 준다.
        2. 여기서도 마지막 로봇은 떨어져야 하므로 0으로 바꿔준다.
    3. 올리는 위치의 내구도가 1이상이면 로봇을 올려준다.
    4. count 함수를 이용해 0의 갯수를 확인하고 k 이상이면 반복문에서 빠져나온다.

```python
from collections import deque

n, k = map(int, input().split())
list_map = deque(list(map(int, input().split())))
list_robot = deque([0] * n)
cnt = 1

while True:
    list_map.rotate(1)
    list_robot.rotate(1)
    list_robot[n-1] = 0

    for i in range(len(list_robot)-2, -1, -1):
        if list_robot[i] == 1 and list_map[i+1] > 0 and list_robot[i+1] == 0:
            list_robot[i+1] = 1
            list_map[i+1] -= 1
            list_robot[i] = 0
    list_robot[n - 1] = 0

    if list_map[0] != 0:
        list_map[0] -= 1
        list_robot[0] = 1

    if list_map.count(0) >= k:
        break

    cnt += 1

print(cnt)
```

https://jewin.notion.site/90fab6494b94417bbde151f99985b861
