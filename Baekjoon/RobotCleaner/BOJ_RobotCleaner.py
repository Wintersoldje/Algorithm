a, b = map(int, input().split())
cx, cy, direction = map(int, input().split())

array = [list(map(int, input().split())) for _ in range(a)]

# 북동남서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def cleaner(x, y, d):
    global result

    if array[x][y] == 0:
        # 청소하면 2로 reset
        array[x][y] = 2
        result += 1
    for i in range(4):
        #왼쪽으로 돌기 때문에 +3 %4 가 방향
        nd = (d + 3) % 4
        nx = x + dx[nd]
        ny = y + dy[nd]
        if array[nx][ny] == 0:
            # 0이면 청소가 안되어 있기 때문에 이동해서 다시 재귀
            cleaner(nx, ny, nd)
            return
        d = nd
    # 뒤로 가기
    nd = (d + 2) % 4
    nx = x + dx[nd]
    ny = y + dy[nd]
    if array[nx][ny] == 1:
        return
    cleaner(nx, ny, d)

result = 0
cleaner(cx, cy, direction)
print(result)






# print(array)
# while True:
#     bp = 0
#     if array[c_y][c_x] == 0:
#         array[c_y][c_x] = 1
#         result += 1
#     else:
#         print("aaa")
#         for i in range(4):
#             if direction == 0: # 북쪽
#                 direction = 3
#                 dx = c_x - 1
#                 dy = c_y
#                 if dx <= 0 or dy <= 0 or dx >= a-1 or dy >= b-1:
#                     bp += 1
#                     continue
#
#                 if array[dy][dx] == 0:
#                     c_x = dx
#                     c_y = dy
#                     break
#                 else:
#                     bp += 1
#                     continue
#             if direction == 1: # 동쪽
#                 direction = 0
#                 dx = c_x
#                 dy = c_y - 1
#                 if dx <= 0 or dy <= 0 or dx >= a-1 or dy >= b-1:
#                     bp += 1
#                     continue
#                 if array[dy][dx] == 0:
#                     c_x = dx
#                     c_y = dy
#                     break
#                 else:
#                     bp += 1
#                     continue
#             if direction == 2: #남
#                 direction = 1
#                 dx = c_x + 1
#                 dy = c_y
#                 if dx <= 0 or dy <= 0 or dx >= a-1 or dy >= b-1:
#                     bp += 1
#                     continue
#                 if array[dy][dx] == 0:
#                     c_x = dx
#                     c_y = dy
#                     break
#                 else:
#                     bp += 1
#                     continue
#             if direction == 3: # 서
#                 direction = 2
#                 dx = c_x
#                 dy = c_y + 1
#                 if dx <= 0 or dy <= 0 or dx >= a-1 or dy >= b-1:
#                     bp += 1
#                     continue
#                 if array[dy][dx] == 0:
#                     c_x = dx
#                     c_y = dy
#                     break
#                 else:
#                     bp += 1
#                     continue
#         print(result)
#
#         if bp == 4:
#             if direction == 0:
#                 direction = 1
#                 c_x = c_x - 1
#                 if c_x <= 0 or c_y <= 0 or c_x >= a-1 or c_y >= b-1:
#                     break
#             if direction == 1:
#                 direction = 2
#                 c_y = c_y - 1
#                 if c_x <= 0 or c_y <= 0 or c_x >= a-1 or c_y >= b-1:
#                     break
#             if direction == 2:
#                 direction = 3
#                 c_x = c_x + 1
#                 if c_x <= 0 or c_y <= 0 or c_x >= a-1 or c_y >= b-1:
#                     break
#             if direction == 3:
#                 direction = 0
#                 c_y = c_y + 1
#                 if c_x <= 0 or c_y <= 0 or c_x >= a-1 or c_y >= b-1:
#                     break
# print(c_x)
# print(c_y)
# print(result)