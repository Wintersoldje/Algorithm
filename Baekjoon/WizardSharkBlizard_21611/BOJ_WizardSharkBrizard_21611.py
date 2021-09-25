from collections import deque

n, m = map(int, input().split())
list_map = [list(map(int, input().split())) for _ in range(n)]
list_magic = [list(map(int, input().split())) for _ in range(m)]
score = [0, 0, 0, 0]
list_marble = []

def marble():
    x = n // 2
    y = n // 2

    count = 0
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    step = 0
    list_marble.append([x, y])
    flag = True
    while True:
        if count % 2 == 0:
            step += 1
        for i in range(step):
            x += dx[count]
            y += dy[count]
            list_marble.append([x,y])
            if x == 0 and y == 0:
                flag = False
                break
        if not flag:
            break
        count = (count + 1) % 4

def solve(board):
    dx = [0, -1, 1, 0, 0]
    dy = [0, 0, 0, -1, 1]

    for d, s in list_magic:
        x = n // 2
        y = n // 2
        # 마법 사용
        for i in range(s):
            x += dx[d]
            y += dy[d]
            if 0 <= x < n and 0 <= y < n:
                board[x][y] = 0
            else:
                break
        # 빈칸 채우기
        empty_fill(board)
        # 중복 제거
        while remove_overlap(board):
            empty_fill(board)

        #그룹화
        group_marble(board)

        # print(board)

def empty_fill(board):
    empty_pos = deque()
    for x, y in list_marble:
        if x == n // 2 and y == n // 2:
            continue
        if board[x][y] == 0:
            empty_pos.append([x, y])
        elif board[x][y] > 0 and empty_pos:
            nx, ny = empty_pos.popleft()
            board[nx][ny], board[x][y] = board[x][y], 0
            empty_pos.append([x, y])

def remove_overlap(board):
    cnt = 0
    visited = deque()
    num = -1
    flag1 = False

    for x, y in list_marble:
        if x == n//2 and y == n//2:
            continue
        if num == board[x][y]:
            cnt += 1
            visited.append([x,y])
        else:
            if cnt >= 4:
                flag1 = True
                score[num] += cnt
            while visited:
                nx, ny = visited.popleft()
                if cnt >= 4:
                    board[nx][ny] = 0
            cnt = 1
            num = board[x][y]
            visited.append([x,y])
    return flag1

def group_marble(board):
    num = -1
    count = 0
    numbers = [0]
    for x, y in list_marble:
        if x == n//2 and y == n//2:
            continue
        if num == -1:
            num = board[x][y]
            count = 1
        else:
            if num == board[x][y]:
                count += 1
            else:
                numbers.append(count)
                numbers.append(num)
                num = board[x][y]
                count = 1
    idx = 0
    for x, y in list_marble:
        board[x][y] = numbers[idx]
        idx += 1
        if idx >= len(numbers):
            break

marble()
solve(list_map)
ans = 0
for i in range(1, 4):
    ans += score[i] * i

print(ans)