def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    tmp_id = ""
    for i in range(len(new_id)):
        if 'a' <= new_id[i] <= 'z' or '0' <= new_id[i] <= '9' or new_id[i] == '-' or new_id[i] == '_' or new_id[i] == '.':
            tmp_id += new_id[i]
            continue
    new_id = tmp_id
    print(new_id)
    tmp2_id = ""
    for i in range(len(new_id)):
        if new_id[i] == '.':
            if len(tmp2_id) == 0:
                tmp2_id += new_id[i]
                continue
            if tmp2_id[-1] == '.':
                continue
            else:
                tmp2_id += new_id[i]
        else:
            tmp2_id += new_id[i]
    new_id = tmp2_id
    if new_id[0] == '.':
        new_id = new_id[1:]
    if len(new_id) != 0:
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    if len(new_id) == 0:
        new_id += "a"
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    while len(new_id) <= 2:
        new_id += new_id[-1]
    answer = new_id
    return answer

print(solution("abcdefghijklmn.p"))