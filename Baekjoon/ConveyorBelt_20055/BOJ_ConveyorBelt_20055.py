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

