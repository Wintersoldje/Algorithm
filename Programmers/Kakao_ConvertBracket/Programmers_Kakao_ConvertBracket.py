def solution(p):
    answer = ''
    u = []
    v = []
    len_a = 0
    len_b = 0
    # 비어있으면 빈거 출력
    if len(p) == 0:
        return ""
    # u, v 나눔
    for i in range(len(p)):
        if p[i] == '(':
            len_a += 1
        else:
            len_b += 1
        if len_a == len_b :
            for j in range(i+1):
                u.append(p[j])
            for k in range(i+1, len(p)):
                v.append(p[k])
            break

    print(u)
    print(v)
    if u[0] == "(" and u[-1] == ")":
        answer += "".join(u)
        if len(v) != 0:
            answer += solution(v)
    else:
        u.pop(0)
        u.pop()
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "("
        answer += solution(v)
        answer += ")"
        answer += "".join(u)


    return answer

print(solution("(()())()"))

