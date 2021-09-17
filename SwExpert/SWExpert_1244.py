from collections import deque
import copy

def ss(l): #list 숫자로 변경하는 함수
    tmp = 0
    cnt = 0
    for i in range(len(l)-1, -1, -1):
        tmp += l[i] * (10 ** cnt)
        cnt += 1
    return tmp

T = int(input())
for test_case in range(1, T + 1):
    num, b = map(str, input().split())
    b = int(b)
    num_list = [int(num[i]) for i in range(len(num))]
    max_list = sorted(num_list, reverse=True)

    max1 = -100001
    q = deque()
    cnt = 0
    q.append([num_list, cnt])
    while q:
        qu, cnt = q.popleft()
        print(qu, cnt)
        if cnt == b:
            a = ss(qu)
            max1 = max(max1, a)
            continue
        if (b-cnt) % 2 == 0 and ss(qu) == ss(max_list):
            max1 = ss(qu)
            break
        if (b-cnt) % 2 == 1 and ss(qu) == ss(max_list):
            flag = 0
            for tt in qu:
                if qu.count(tt) > 1:
                    max1 = ss(qu)
                    flag = 1
                    break
            if flag != 1:
                tmp = qu[-1]
                qu[-1] = qu[-2]
                qu[-2] = tmp
                print(qu)
                max1 = ss(qu)
            break

        for i in range(len(qu)-1):
            if qu[i] <= max(qu[i+1:]):
                m = max(qu[i+1:])
                m_list = [j for j, v in enumerate(qu) if v == m]
                for tmp in m_list:
                    c_list = copy.deepcopy(qu)
                    c_list[tmp], c_list[i] = c_list[i], c_list[tmp]
                    q.append([c_list, cnt+1])
    print("#" + str(test_case) + " " + str(max1))
