# 문제

[코딩테스트 연습 - 메뉴 리뉴얼](https://programmers.co.kr/learn/courses/30/lessons/72411)

# 풀이

1. 해당 course 즉 메뉴 갯수별로 모든 조합을 구해주고 딕셔너리에 저장해준다. 
2. 다음 주문자에서도 중복된게 나오면 딕셔너리에 추가해준다.
3. 가장 많이 나오는 값을 정해주고, 중복되는게 있으면 같이 출력해준다.

```python
from itertools import combinations

def solution(orders, course):
    answer = []
    tmp_answer = []
    tmp = []
    dict = {}
    for i in course:
        tmp.clear()
        for order in orders:
            if len(order) < i:
                continue
            tmp = list(combinations(sorted(order), i))
            for j in tmp:
                if j not in dict.keys():
                    dict[j] = 1
                else:
                    dict[j] += 1
        if len(dict) == 0:
            continue
        if not(max(dict.values()) < 2):
            tmp_list = [k for k, v in dict.items() if max(dict.values()) == v]
            for s in tmp_list:
                str = ""
                for k in range(len(s)):
                    str += s[k]
                answer.append(str)

        tmp_list.clear()
        dict.clear()
    answer.sort()
    return answer

# print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))
#
```

[https://jewin.notion.site/e3f4e65eac914f59b594578179c0f125](https://www.notion.so/e3f4e65eac914f59b594578179c0f125)
