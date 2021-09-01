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