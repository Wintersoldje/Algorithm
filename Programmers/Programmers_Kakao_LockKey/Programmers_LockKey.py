#90도 회전
def turnninety(key_list):
    len_list = len(key_list)
    len_col = len(key_list[0])
    turn_key = [[0]*len_list for _ in range(len_col)]
    for i in range(len_list):
        for j in range(len_col):
            turn_key[j][len(key_list)-i-1] = key_list[i][j]
    return turn_key
#자물쇠 확인
def check_lock(lock_list):
    start_point = len(lock_list) // 3
    for i in range(start_point, 2*start_point):
        for j in range(start_point, 2*start_point):
            if lock_list[i][j] != 1:
                return False
    return True

def solution(key, lock):
    len_lock = len(lock)
    len_key = len(key)
    #자물쇠 크기 3배
    check_box = [[0] * (len_lock * 3) for _ in range(len_lock*3)]
    # check_box라는 배열가운데 자물쇠 저장
    for i in range(len_lock):
        for j in range(len_lock):
            check_box[i+len_lock][j+len_lock] = lock[i][j]

    for i in range(4):
        turnkey = turnninety(key)
        for k in range(len_lock*2):
            for l in range(len_lock*2):
                #자물쇠 넣기
                for a in range(len_key):
                    for b in range(len_key):
                        check_box[k+a][l+b] += turnkey[a][b]
                #맞는지 체크
                if check_lock(check_box) == True:
                    return True
                #다시 빼기
                for a in range(len_key):
                    for b in range(len_key):
                        check_box[k + a][l + b] -= turnkey[a][b]


    return False

