def solution(cacheSize, cities):
    answer = 0
    cache = []
    if cacheSize == 0:
        answer = len(cities) * 5
        return answer
    for i in range(len(cities)):
        if len(cache) < cacheSize:
            if cities[i].upper() in cache:
                cache.remove(cities[i].upper())
                cache.append(cities[i].upper())
                answer += 1
            else:
                cache.append(cities[i].upper())
                answer += 5
            continue
        if cities[i].upper() not in cache:
            answer += 5
            cache.pop(0)
            cache.append(cities[i].upper())
        else:
            cache.remove(cities[i].upper())
            cache.append(cities[i].upper())
            answer += 1
        # print(cache)
    return answer
print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))