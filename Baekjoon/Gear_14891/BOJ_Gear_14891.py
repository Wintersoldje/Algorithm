from collections import deque

circle = [deque(map(int,input())) for _ in range(4)]
opers = deque(list(map(int,input().split())) for _ in range(int(input())))

while opers:
    num, direction = opers.popleft()
    num -= 1
    tmp_right = circle[num][2]
    tmp_left = circle[num][6]
    circle[num].rotate(direction)
    tmp_direct = direction

    direction = tmp_direct
    for i in range(num-1, -1, -1):
        if circle[i][2] != tmp_left:
            tmp_left = circle[i][6]
            circle[i].rotate(direction*-1)
            direction *= -1
        else:
            break

    direction = tmp_direct
    for i in range(num+1, 4):
        if circle[i][6] != tmp_right:
            tmp_right = circle[i][2]
            circle[i].rotate(direction*-1)
            direction *= -1
        else:
            break
ans  = 0
for i in range(4):
    if circle[i][0] == 1:
        ans += (2**i)
print(ans)