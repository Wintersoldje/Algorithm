def dfs(b, t, w, v, c):
    answer = int(1e9)
    if b == t:
        return c
    for i in w:
        if i not in v:
            if check(i, b):
                v.append(b)
                answer = min(answer, dfs(i, t, w, v, c+1))
                v.pop()
    return answer


def check(a, b):
    count = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            count += 1
    if len(a) - count == 1:
        return True
    return False

def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    visited = []
    answer = dfs(begin, target, words, visited, 0)
    return answer

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]	))
print(solution("hit", "cog",["hot", "dot", "dog", "lot", "log"]))
