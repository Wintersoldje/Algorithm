def solution(n, results):
    answer = 0
    list_map = [[-1] * n for i in range(n)]
    for i,j in results:
        list_map[i-1][j-1] = 0
    # print(list_map)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if list_map[i][k] == 0 and list_map[k][j] == 0:
                    list_map[i][j] = 0
                    # list_map[j][i] = 0
    # print(list_map)
    for i in range(n):
        count = 0
        for j in range(n):
            if list_map[i][j] != -1 or list_map[j][i] != -1:
                count += 1
        if count == n-1:
            answer += 1
    return answer

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))