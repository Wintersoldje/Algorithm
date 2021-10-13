# 문제

[코딩테스트 연습 - 후보키](https://programmers.co.kr/learn/courses/30/lessons/42890)

# 풀이

1. 인덱스로 조합을 구해준다.
2. 유일성이 만족하는지 확인해준다.
    1. 조합만큼 돌면서 해당 조합으로 릴레이션을 만들어준다.
    2. 추가적으로 해당 조합을 튜플로 추가해준다.
3. 튜플을 따로 list_answer에 넣어준다. 이때 들어간 튜플은 유일성을 만족시키는 튜플들이다.
4. 최소성을 만족시키기 위해 앞 뒤 set & 연산을 이용해 비교해준다. 
    1. discard는 remove대신 인덱스 애러를 방지하기 위해 사용함

```python
from itertools import combinations

def solution(relation):
    answer = 0
    len_row = len(relation)
    len_col = len(relation[0])
    list_answer = []
    
    # 테이블 릴레에션 인덱스로 조합 구하기
    comb_list = []
    list_relation = [i for i in range(len(relation[0]))]
        
    # 해당 릴레이션이 유일성을 만족하는지 확인
    for j in range(1, len_col+1):
        tmp_s = []
        for comb in combinations(list_relation, j):
            tmp = []
            for rel in relation:
                cur = [rel[c] for c in comb]
                if cur in tmp:
                    break
                else:
                    tmp.append(cur)
            tmp.append(comb)
            if len(tmp) == len_row + 1:
                list_answer.append(tmp[-1])

    #최소성 만족하는지 확인
    temp = set(list_answer)
    for i in range(0, len(list_answer) - 1):
        for j in range(i + 1, len(list_answer)):
            # 최소성을 만족하지 못한 경우
            if set(list_answer[i]) == set(list_answer[i]) & set(list_answer[j]):
                temp.discard(list_answer[j])
                
    answer = len(temp)
     
    # 유일성을 만족하는 애들 중에 최소성을 만족하는지 확인
    return answer
```
