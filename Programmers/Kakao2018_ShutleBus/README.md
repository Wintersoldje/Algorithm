# 문제

[코딩테스트 연습 - [1차] 셔틀버스](https://programmers.co.kr/learn/courses/30/lessons/17678)

# 풀이

우선 처음 시간을 분 단위로 바꿔준다.

그리고 버스 시간 테이블을 리스트로 만들어준다. 그 후 첫 버스 부터 마지막 버스까지 돌면서 해당 버스에 정원이 다 찰때까지 돌아주는데 만약 다 차 있으면 마지막에 있는 사람을 빼주고 그 버스 시간에 맞춰서 탄다.

1. 타임테이블을 분으로 바꿔준다.
2. 버스 시간표를 리스트로 만들어준다.
3. 모든 버스를 보면서 조건에 맞으면 버스에 태워준다.
4. 꽉 차있으면 마지막 사람을 빼고 태운다
5. 아니면 최대한 늦게 탑승한다.
6. 최종 적으로 시간을 맞춰 적어준다.

```python
def solution(n, t, m, timetable):
    answer = ''
    list_time = []
    for i in timetable:
        list_time.append(int(i[:2]) * 60 + int(i[3:]))
    list_time.sort(reverse=True)
    #버스 시간 테이블
    bus = [540 + t*i for i in range(n)]
    bus_idx = 0
    tmp_answer = 0
    #첫 버스부터 마지막 버스까지
    while bus_idx < len(bus):
        #현재의 버스
        stack = []
        bus_onboard = 0
        #해당 버스에 정원이 다 찰때까지
        while bus_onboard != m:
            # 조건에 안 맞으면 버스에 태워준다
            if len(list_time) >= 1 and list_time[-1] <= bus[bus_idx]:
                bus_onboard += 1
                stack.append(list_time.pop())
            else:
                break
        #마지막 버스에서
        if bus_idx == len(bus)-1:
            #꽉 차있으면
            if bus_onboard == m:
                #무조건 이 앞에 타야함
                tmp_answer = stack.pop() - 1
            else:
                #최대한 늦게 탑승
                tmp_answer = bus[bus_idx]
        bus_idx += 1
    #분단위 변환
    if tmp_answer // 60 < 10:
        answer += '0' + str(tmp_answer//60)
    else:
        answer += str(tmp_answer//60)
    answer += ":"
    if tmp_answer%60 < 10:
        answer += '0' + str(tmp_answer%60)
    else:
        answer += str(tmp_answer%60)
    return answer

print(solution(1,1,5,["08:00", "08:01", "08:02", "08:03"]))
```
https://jewin.notion.site/2018Kakao-022b111e0d224d5baf386ff397e82321
