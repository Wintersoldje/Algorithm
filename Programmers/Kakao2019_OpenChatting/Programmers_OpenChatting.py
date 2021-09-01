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

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))