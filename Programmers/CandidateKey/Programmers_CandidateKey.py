from itertools import combinations

def solution(relation):
    len_row = len(relation)
    len_col = len(relation[0])
    list_answer = []

    # 테이블 릴레에션 인덱스로 조합 구하기
    list_relation = [i for i in range(len(relation[0]))]

    # 해당 릴레이션이 유일성을 만족하는지 확인

    for j in range(1, len_col + 1):
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

    temp = set(list_answer)
    for i in range(0, len(list_answer) - 1):
        for j in range(i + 1, len(list_answer)):
            # 최소성을 만족하지 못한 경우
            if set(list_answer[i]) == set(list_answer[i]) & set(list_answer[j]):
                temp.discard(list_answer[j])

    answer = len(temp)

    # 유일성을 만족하는 애들 중에 최소성을 만족하는지 확인
    return answer