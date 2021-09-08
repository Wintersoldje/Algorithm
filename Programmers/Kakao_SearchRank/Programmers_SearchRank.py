from itertools import combinations

def solution(info, query):
    answer = []
    order = []
    db = {}
    for i in info:
        tmp = i.split()
        condition = tmp[:-1]
        score = int(tmp[-1])
        for n in range(5):
            combi = list(combinations(range(4), n))
            for c in combi:
                t_c = condition.copy()
                for v in c:
                    t_c[v] = '-'
                change_tc = '/'.join(t_c)
                if change_tc in db:
                    db[change_tc].append(score)
                else:
                    db[change_tc] = [score]
    print(db)
    for value in db.values():
        value.sort()
    for q in query:  # query의 모든 조건에 대해서
        qry = [i for i in q.split() if i != 'and']
        qry_cnd = '/'.join(qry[:-1])
        qry_score = int(qry[-1])
        if qry_cnd in db:  # 딕셔너리 내에 값이 존재한다면,
            data = db[qry_cnd]
            if len(data) > 0:
                start, end = 0, len(data)  # lower bound 알고리즘 통해 인덱스 찾고,
                while start != end and start != len(data):
                    if data[(start + end) // 2] >= qry_score:
                        end = (start + end) // 2
                    else:
                        start = (start + end) // 2 + 1
                answer.append(len(data) - start)  # 해당 인덱스부터 끝까지의 갯수가 정답
        else:
            answer.append(0)
    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))