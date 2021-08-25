# 문제

[코딩테스트 연습 - [1차] 추석 트래픽](https://programmers.co.kr/learn/courses/30/lessons/17676)

# 풀이

처음에 시간이 나와 있어서 당황했다. 시간을 한개의 단위로 표현하면 계산하기 편하다. 따라서 시간을 ms단위로 맞춰 준다.

그리고 시작 시간과 종료 시간을 list에 넣어준다.

그 후 log의 시작 시간을 기준으로 1초 동안 다른 log와 겹치는 지 확인해 주어 가장 큰 값을 출력해준다.

1. split()을 이용해 date, s, t로 나눠준다.
2. s는 :를 기준으로 ms으로 계산해준다.
3. t은 replace를 이용해 s를 제거하고 초를 구한다
4. log에 담긴 시작과 끝 시간을 기준으로 시작 시간 기준 1초 간격 , 종료 시간 기준 1초 간격으로 겹쳐 져 있는 log를 sol함수를 이용해 찾아준다.
    1. 어떤 요청의 x 시작 시간이 end보다 작고, 끝 시간이 start보다 크면 해당 시점에 요청이 진행 중이므로 처리량에 1을 더한다.

```python
def solution(lines):
    answer = 0
    log = []
    for line in lines:
        date, s, t = line.split()
        s = s.split(":")
        t = t.replace("s","")
        
        end = (int(s[0])*3600 + int(s[1]) * 60 + float(s[2])) * 1000
        start = end - float(t)*1000 + 1
        log.append([start, end])
        
    for x in log:
        answer = max(answer, sol(log, x[0],x[0] + 1000), sol(log, x[1],x[1] + 1000))
        
    return answer
def sol(log, start, end):
    cnt = 0
    for x in log:
        if x[0] < end or x[1] >= start:
            cnt += 1
    return cnt
```

https://jewin.notion.site/871eed54cf9f4474b0e6ae60710b5ab2
