def solution(s):
    answer = []
    tmp = 0
    str = []
    t = []
    # 숫자 구분 ( "{" , "," , "}" 제외 시키기)
    for i in range(1, len(s)-1):
        if s[i] == "{":
            tmp = i+1
            continue
        elif s[i] == ',':
            continue
        elif s[i] == "}":
            str.append(s[tmp:i].split(","))
            t.clear()
            tmp += 1
        else:
            t.append(s[i])
    # 길이로 구분
    str.sort(key=lambda x:len(x))
    len_num = len(str)

    # 구분된 부분에서 순서대로 위치 맞춰주기
    for i in range(len_num-1):
        for j in range(i+1):
            index = str[i + 1].index(str[j][j])
            if index == j:
                continue
            else:
                temp = str[i + 1][j]
                str[i + 1][j] = str[i + 1][index]
                str[i + 1][index] = temp
    # 가장 앞 부분만 따서 오기 
    for i in range(len_num):
        answer.append(int(str[i][i]))


    return answer

# from collections import Counter
# def solution(s):
#     new_s = [sss.replace('{','').replace('}','') for sss in s.split(',')]
#     print(Counter(new_s).items())
#     return [int(c[0]) for c in sorted(Counter(new_s).items(), key = lambda x: x[1],reverse=True )]

print(solution("{{1,2,3},{1,2},{4,1,2,3},{2}}"))
