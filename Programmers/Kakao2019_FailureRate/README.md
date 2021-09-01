# 문제

[코딩테스트 연습 - 실패율](https://programmers.co.kr/learn/courses/30/lessons/42889)

# 풀이

문제를 보자마자 우선 stage를 보고 해당 스테이지 레벨이 어디에 속해져야하는지 구해야 겠다는 생각을 하였다. 그럼 stage리스트를 정렬해서 가장 작은 stage부터 보면서 실패율을 구해야겠다는 생각을 하였다. 

1. stages를 오름차순 정렬한다.
2. stages를 앞에서 부터 보면서 해당 스테이지 보다 낮거나 같으면 뽑아서 카운트 해준다.
3. while문의 종료조건은 해당 스테이지보다 낮을때 혹은 stage 길이가 0일때
4. list_tmp에 실패율 계산해서 넣어준다.
5. 정렬해서 인덱스 출력해준다.

```python
def solution(N, stages):
    answer = []
    stages.sort()
    n = len(stages)
    list_tmp = []
    for i in range(1, N+1): #
        count = 0
        # if len(stages) == 0:
        #     break
        while True:
            if len(stages) == 0:
                break
            if stages[0] <= i:
                stages.pop(0)
                count += 1
            else:
                break
        list_tmp.append(count)
    num = 0
    list_rank = []
    for i in range(N):
        if list_tmp[i] == 0:
            list_rank.append((i+1, 0.0))
            continue
        else:
            tmp = n - num
            list_rank.append((i+1, list_tmp[i]/tmp))
            num += list_tmp[i]
    list_rank = sorted(list_rank, key=lambda x:x[1], reverse=True)
    for a,b in list_rank:
        answer.append(a)
    return answer

# print(solution(4,[4,4,4,4,4]))
```
https://jewin.notion.site/2019Kakao-e2a700b374904315bd8379f9a9234e8a
