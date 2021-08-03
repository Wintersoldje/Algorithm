def merge_sort(start, end):
    global cnt
    if start < end:
        mid = (start + end) // 2
        merge_sort(start, mid)
        merge_sort(mid + 1 , end)

        a = start
        b = mid + 1

        tmp = []

        while a <= mid and b <= end :
            if array[a] <= array[b]:
                tmp.append(array[a])
                a += 1
            else:
                tmp.append(array[b])
                b += 1
                cnt += mid - a + 1
        if a <= mid:
            tmp = tmp + array[a:mid+1]
        if b <= end:
            tmp = tmp + array[b:end+1]
        for i in range(len(tmp)):
            array[start + i] = tmp[i]


n = int(input())
array = list(map(int, input().split()))
cnt = 0
merge_sort(0, n-1)
print(cnt)

