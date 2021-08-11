def find(l):
    start, end = l.pop(0)
    count = 1
    for s, e in l:
        # print(start, end)
        # print(s,e)
        if end < s :
            count += 1
            start = s
            end = e
            continue
        if start <= s or end >= e:
            if start <= s:
                start = max(start, s)
            if end >= e:
                end = min(end, e)
        # print("final", start, end)

    return count


def solution(routes):
    routes = sorted(routes,key=lambda x:x[0])
    # print(routes)
    answer = find(routes)
    return answer

print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]))