n = int(input())
m = list(map(int, input().split()))
#오름차순 정렬
m.sort()
#비교할 타겟 설정
target = 1


for i in m:
    #타겟보다 크면 target이 결과
    if target < i:
        break
    target += i

print(target)


