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

print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))
