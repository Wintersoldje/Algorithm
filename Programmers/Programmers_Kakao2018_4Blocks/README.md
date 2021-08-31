# 문제

[코딩테스트 연습 - [1차] 프렌즈4블록](https://programmers.co.kr/learn/courses/30/lessons/17679)

# 풀이

단순 구현 문제이다.  2x2 모양이 같으면 지워주면서 지워지면 위에 있는 블럭이 내려오는 형식이다. 그래서 나는 일단 제거되는 블럭을 먼저 찾았다. 근데 입력이 string으로 들어오기 때문에 list형식으로 바꿔 주고 문제를 풀었다.

1. string배열을 list로 바꿔줌
2. 4블럭이 같으면 list_check에 넣어주고 set으로 중복을 제거해줌
3. 없어지는 블럭을 "0"처리 해주고 
4. map에서 빈 공간을 채워준다.
    1. 빈 공간은 세로를 기준으로 내려준다.
5. 그 과정을 반복하면서 지워지는게 없을 때 까지 반복한다.

```python
def solution(m, n, board):
    answer = 0
    list_check = []
    list_map = list(map(list, board))
    print(list_map)
    while True:
        for i in range(m-1):
            for j in range(n-1):
                if list_map[i][j] == list_map[i][j+1] == list_map[i+1][j] == list_map[i+1][j+1] and list_map[i][j] != "0":
                    list_check.append((i, j))
                    list_check.append((i+1, j))
                    list_check.append((i, j+1))
                    list_check.append((i+1, j+1))

        list_check = list(set(list_check))
        if len(list_check) == 0:
            return answer
        else:
            answer += len(list_check)

        for i in range(len(list_check)):
            a, b = list_check[i]
            list_map[a][b] = "0"
        for x in range(n):
            tmp = []
            for y in range(m):
                tmp.append(list_map[y][x])
            for i in range(tmp.count("0")):
                tmp.remove("0")
            for j in range(m-1, -1,-1):
                if len(tmp) == 0:
                    list_map[j][x] = "0"
                    continue
                list_map[j][x] = tmp.pop(-1)
        list_check.clear()

    return answer
```

[https://jewin.notion.site/4-2018Kakao-7e12340870c54196972825b813e73cd7](https://www.notion.so/4-2018Kakao-7e12340870c54196972825b813e73cd7)
