# 문제

[코딩테스트 연습 - [1차] 캐시](https://programmers.co.kr/learn/courses/30/lessons/17680)

# 풀이

처음에는 우선순위를 정해주려고 heapq를 사용하려고 하였는데, 무조건 우선 순위가 hit이 되지 않는 경우도 있기 때문에 heapq를 쓰면 안된다.

그래서 리스트를 이용해서 간단하게 구현할 수 있었다.

1. cache사이즈가 0이면 cities의 길이 곱하기 5를 해 주었다.
2. list_cache 사이즈가 cacheSize보다 작으면 
    1. 캐시가 아직 다 안차있다는 거니까 새로 들어오는 도시는 answer에 +5만 해주고 list에 append 해 주었다.
    2. 근데 만약 안에 중복되는 도시가 있으면 그 도시를 찾아서 리무브 해주고 다시 뒤로 넣어준다.
3. list_cache 사이즈가 cacheSize보다 크면
    1.  캐시 안에 들어있으면 지우고 뒤로 넣어줌
    2. 캐시 안에 안 들어있으면 우선순위 빼고 해당 도시 넣음

```python
def solution(cacheSize, cities):
    answer = 0
    list_cache = []
    if cacheSize == 0:
        return 5 * len(cities)
    for i in range(len(cities)):
        if len(list_cache) < cacheSize:
            if cities[i].upper() in list_cache:
                answer += 1
                list_cache.remove(cities[i].upper())
                list_cache.append(cities[i].upper())
            else:
                answer += 5
                list_cache.append(cities[i].upper())
        else:
            if cities[i].upper() in list_cache:
                answer += 1
                list_cache.remove(cities[i].upper())
                list_cache.append(cities[i].upper())
            else:
                answer += 5
                list_cache.pop(0)
                list_cache.append(cities[i].upper())
    return answer

print(solution(2,["Jeju", "Seoul", "Jeju"]))
```

[https://jewin.notion.site/2018-96b56fe7bacd4f948a3a9a2533208c55](https://www.notion.so/2018-96b56fe7bacd4f948a3a9a2533208c55)
