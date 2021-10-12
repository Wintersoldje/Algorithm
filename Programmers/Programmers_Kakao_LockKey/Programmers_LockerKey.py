def rotate(tmp_list): #키를 회전시키는 함수
    tmp = []
    for i in range(len(tmp_list)):
        tmp.append([tmp_list[i][1], -tmp_list[i][0]])
    return tmp

def solution(key, lock):
    answer = False
    n = len(lock)
    m = len(key)
    list_lock = set() # lock은 변하지 않음으로 set으로 고정
    for i in range(n):
        for j in range(n):
            if lock[i][j] == 0:
                list_lock.add((i, j))
    list_key = []
    #키 넣어주기
    for i in range(m):
        for j in range(m):
            if key[i][j] == 1:
                list_key.append([i, j])
    #자물쇠의 첫 부분을 베이스로 잡기
    for i in list_lock:
        base_x, base_y = i
        break

    if len(list_lock) == 0:
        return True
    if len(list_key) == 0:
        return False
    #키를 돌리면서 확인
    for _ in range(4):
        list_key = rotate(list_key)
        # 베이스와의 거리 차를 이용해 다른 key도 평행이동 시키기 위한 평행이동좌표 구하기
        for k_x, k_y in list_key:
            flag = True
            cx = base_x - k_x
            cy = base_y - k_y
            count = 0
            for diff_x, diff_y in list_key:
                x, y = diff_x + cx, diff_y + cy
                if 0 <= x < n and 0 <= y < n:
                    if (x, y) in list_lock:
                        count += 1
                        continue
                    else:
                        flag = False
                        break
            if flag and count == len(list_lock):
                return True

    return answer

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))