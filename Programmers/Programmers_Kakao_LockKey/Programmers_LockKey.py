def turnninety(key_list):#90degree rotation
    len_list = len(key_list)
    turn_key = [[0]*len_list for i in range(len_list)]
    for i in range(len_list):
        for j in range(len_list):
            turn_key[j][len(key_list)-i-1] = key_list[i][j]
    return turn_key


def check_lock(lock_list):
    start_point = len(lock_list) // 3
    for i in range(start_point, 2*start_point):
        for j in range(start_point, 2*start_point):
            if lock_list[i][j] != 1:
                return False
    return True

def solution(key, lock):
    len_lock = len(lock)
    check_box = [[0] * (len_lock * 3) for _ in range(len_lock*3)]

    for i in range(len_lock):
        for j in range(len_lock):
            check_box[i+len_lock][j+len_lock] = lock[i][j]

    for i in range(4):
        turned_key = turnninety(key)
        for k in range(1,len(key)*2):
            for l in range(1,len(key)*2):
                for a in range(len(key)):
                    for b in range(len(key)):
                        check_box[k+a][l+b] += turned_key[a][b]

                print(check_box)
                if check_lock(check_box) == True:
                    return True
                else:
                    for a in range(len(key)):
                        for b in range(len(key)):
                            check_box[k + a][l + b] -= turned_key[a][b]


    return False

print(solution([[0,0,0],[1,0,0],[0,1,1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))