def move_left(cnt_list, idx):
    i = 1
    while cnt_list[idx - i] == 0:
        i += 1
    return i

def move_right(cnt_list, idx):
    i = 1
    while cnt_list[idx + i] == 0:
        i += 1
    return i

def solution(name):
    answer = 0
    count_list = []

    for i in range(len(name)):
        if ord(name[i]) <= 77 and ord(name[i]) > 65: #중간인 M기준 으로 count
            count_list.append(ord(name[i]) - ord("A"))
        elif ord(name[i]) >= 78:
            count_list.append(ord("Z") - ord(name[i])+1)
        elif ord(name[i]) == 65: #A일때는 0
            count_list.append(0)

    idx = 0
    while True:
        answer += count_list[idx]
        count_list[idx] = 0
        if sum(count_list) == 0: #전부 A가 되면 종료
            break

        left = move_left(count_list, idx)
        right = move_right(count_list, idx)
        if left < right:
            answer += left
            idx += -left
        else:
            answer += right
            idx += right

    return answer

