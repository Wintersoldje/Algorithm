def solution(m, n, board):
    answer = 0
    list_map = list(map(list,board))
    # print(list_map)
    while True:
        list_remove = set()
        for i in range(m-1):
            for j in range(n-1):
                if list_map[i][j] == list_map[i+1][j] == list_map[i][j+1] == list_map[i+1][j+1] and list_map[i][j] != "0":
                    list_remove.add((i,j))
                    list_remove.add((i+1, j))
                    list_remove.add((i, j+1))
                    list_remove.add((i + 1, j+1))
        list_remove = list(set(list_remove))

        if len(list_remove) == 0:
            return answer
        else:
            answer += len(list_remove)
        list_remove.sort()
        for i in range(len(list_remove)):
            a, b = list_remove[i]
            list_map[a][b] = "0"
        for x in range(n):
            tmp = []
            for y in range(m):
                tmp.append(list_map[y][x])
            for i in range(tmp.count("0")):
                tmp.remove("0")
            for k in range(m-1,-1,-1):
                if len(tmp) == 0:
                    list_map[k][x] = "0"
                    continue
                list_map[k][x] = tmp.pop(-1)
        list_remove.clear()
        # print(list_map)
    return answer

print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))