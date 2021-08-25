def solution(lines):
    answer = 0
    log = []
    for line in lines:
        date, s, t = line.split()
        s = s.split(":")
        t = t.replace("s", "")

        end = (int(s[0]) * 3600 + int(s[1]) * 60 + float(s[2])) * 1000
        start = end - float(t) * 1000 + 1
        log.append([start, end])

    for x in log:
        answer = max(answer, sol(log, x[0], x[0] + 1000), sol(log, x[1], x[1] + 1000))

    return answer


def sol(log, start, end):
    cnt = 0
    for x in log:
        if x[0] < end or x[1] >= start:
            cnt += 1
    return cnt