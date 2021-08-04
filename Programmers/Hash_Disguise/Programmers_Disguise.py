def solution(clothes):
    dict = {}
    result = 1
    for i in range(len(clothes)):
        clothe, kinds = clothes[i]
        dict[kinds] = dict.get(kinds, []) + [clothe]
    for key in dict.keys():
        result = result * (len(dict[key])+1)
    return result - 1

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
