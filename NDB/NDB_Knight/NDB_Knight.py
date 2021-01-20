n =input()
row = int(n[1])
#앞 문자를 0~7로 바꿈
column = int(ord(n[0])) - int(ord('a')) + 1

steps = [(-2,1),(-2,-1),(-1,2), (-1, -2), (1, 2), (1,-2), (2,1), (2,-1)]

answer = 0
for step in steps:
    next_row = step[0] + row
    next_col = step[1] + column

    # 이동한 값이 범위 내에 있으면 +1
    if next_row >= 1 and next_row <=8 and next_col >= 1 and next_col <=8:
        answer += 1

print(answer)