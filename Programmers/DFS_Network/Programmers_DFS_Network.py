def dfs(computers, visit, start):
    record = [start]
    while record:
        tmp = record.pop()
        if visit[tmp] == 0:
            visit[tmp] = 1
        for i in range(len(computers)):
            if computers[tmp][i] == 1 and visit[i] == 0:
                record.append(i)

def solution(n, computers):
    answer = 0
    visit = [0] * n
    start = 0
    while 0 in visit:
        if visit[start] == 0:
            dfs(computers, visit, start)
            answer += 1
        start += 1

    return answer
