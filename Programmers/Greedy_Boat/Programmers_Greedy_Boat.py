def solution(people, limit):
    count = 0
    people.sort()
    light = 0
    heavy = len(people)-1
    while light < heavy:
        if people[light] + people[heavy] <= limit:
            count += 1
            light += 1
            heavy -= 1
        else:
            heavy -= 1
    return len(people) - count

print(solution([70, 50, 80, 50], 100))


