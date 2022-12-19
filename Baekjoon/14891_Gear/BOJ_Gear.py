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
