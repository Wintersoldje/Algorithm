def divid_list(l, n):
    for i in range(0,len(l), n):
        yield l[i:i + n]

def count(list_n):
    count = 1
    tmp = []
    for i in range(len(list_n)-1):
        if list_n[i] == list_n[i+1]:
            count += 1
        else:
            if count != 1:
                tmp.append(str(str(count) + list_n[i]))
                count = 1
            else:
                tmp.append(list_n[i])

        if i == len(list_n)-2:
            if count != 1:
                tmp.append(str(str(count) + list_n[i]))
                count = 1
            else:
                tmp.append(list_n[i+1])

    return tmp

def solution(s):
    answer = 0
    len_s = len(s) // 2
    list_n = []
    if len(s) == 1:
        return 1
    for i in range(1, len_s+1):
        result = count(list(divid_list(s, i)))
        list_n.append(len(''.join(result)))
    answer = min(list_n)
    return answer

print(solution("abcabcdede"))