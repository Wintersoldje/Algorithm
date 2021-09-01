# 문제

[코딩테스트 연습 - 오픈채팅방](https://programmers.co.kr/learn/courses/30/lessons/42888)

# 풀이

문제를 처음에 조금 잘못 이해해서 해맸다. 하지만 정말 간단한 문제였다.

dictionary를 이용하면 바로 해결 가능한 문제이다.

key를 아이디로 잡고 value를 닉네임으로 잡으면 쉽게 풀린다.

1. 모든 명령을 구분하기 쉽게 띄어쓰기 단위로  string list로 변환해준다.
2. 해당 아이디 정보는 "Enter"일때와 "Change"일때 변하므로
    1. "Enter"일때는 추가
    2. "Change"일때는 해당 key를 찾아서 변경해주면 된다.
3. 그리고 마지막으로 list_order를 순회하면서 해당 아이디에 해당하는 닉네임으로 출력해준다.

```python
def solution(record):
    answer = []
    name = {}
    list_order = [list(map(str, record[i].split())) for i in range(len(record))]
    for i in range(len(list_order)):
        if list_order[i][0] == "Enter":
            name[list_order[i][1]] = list_order[i][2]
        elif list_order[i][0] == "Change":
            name[list_order[i][1]] = list_order[i][2]
    for i in range(len(list_order)):
        if list_order[i][0] == "Enter":
            answer.append(name[list_order[i][1]] + "님이 들어왔습니다.")
        elif list_order[i][0] == "Leave":
            answer.append(str(name[list_order[i][1]] + "님이 나갔습니다."))
    return answer
```
https://jewin.notion.site/2019Kakao-1f07cf6e594a49d7938044bf04eca8c3
