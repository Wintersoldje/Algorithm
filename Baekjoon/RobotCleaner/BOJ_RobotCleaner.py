a, b = map(int, input().split())
c_x, c_y , direction = map(int, input().split())

result = 0

array = [list(map(int, input().split())) for _ in range(b)]
print(array)
while True:
    bp = 0
    if array[c_y][c_x] == 0:
        array[c_y][c_x] = 1
        result += 1
    else:
        print("aaa")
        for i in range(4):
            if direction == 0: # 북쪽
                direction = 3
                dx = c_x - 1
                dy = c_y
                if dx <= 0 or dy <= 0 or dx >= a-1 or dy >= b-1:
                    bp += 1
                    continue

                if array[dy][dx] == 0:
                    c_x = dx
                    c_y = dy
                    break
                else:
                    bp += 1
                    continue
            if direction == 1: # 동쪽
                direction = 0
                dx = c_x
                dy = c_y - 1
                if dx <= 0 or dy <= 0 or dx >= a-1 or dy >= b-1:
                    bp += 1
                    continue
                if array[dy][dx] == 0:
                    c_x = dx
                    c_y = dy
                    break
                else:
                    bp += 1
                    continue
            if direction == 2: #남
                direction = 1
                dx = c_x + 1
                dy = c_y
                if dx <= 0 or dy <= 0 or dx >= a-1 or dy >= b-1:
                    bp += 1
                    continue
                if array[dy][dx] == 0:
                    c_x = dx
                    c_y = dy
                    break
                else:
                    bp += 1
                    continue
            if direction == 3: # 서
                direction = 2
                dx = c_x
                dy = c_y + 1
                if dx <= 0 or dy <= 0 or dx >= a-1 or dy >= b-1:
                    bp += 1
                    continue
                if array[dy][dx] == 0:
                    c_x = dx
                    c_y = dy
                    break
                else:
                    bp += 1
                    continue
        print(result)

        if bp == 4:
            if direction == 0:
                direction = 1
                c_x = c_x - 1
                if c_x <= 0 or c_y <= 0 or c_x >= a-1 or c_y >= b-1:
                    break
            if direction == 1:
                direction = 2
                c_y = c_y - 1
                if c_x <= 0 or c_y <= 0 or c_x >= a-1 or c_y >= b-1:
                    break
            if direction == 2:
                direction = 3
                c_x = c_x + 1
                if c_x <= 0 or c_y <= 0 or c_x >= a-1 or c_y >= b-1:
                    break
            if direction == 3:
                direction = 0
                c_y = c_y + 1
                if c_x <= 0 or c_y <= 0 or c_x >= a-1 or c_y >= b-1:
                    break
print(c_x)
print(c_y)
print(result)