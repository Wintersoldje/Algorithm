## 문제

[코딩테스트 연습 - 자물쇠와 열쇠](https://programmers.co.kr/learn/courses/30/lessons/60059)

## 풀이

키의 좌표와 자물쇠의 빈 공간의 좌표를 따로 저장해서 해당 좌표와 키의 좌표가 일치하는지 비교해준다.

1. 좌물쇠의 빈 공간 좌표를 list_lock에 set으로 저장해준다.
2. 키의 튀어나온 부분을 list_key에 저장해준다.
3. 자물쇠의 첫 빈칸을 베이스로 잡는다.
4. 베이스로 잡은 자물쇠의 빈 공간과 list_key 안에 있는 부분을 차례대로 기준을 잡아주고, 해당 기준의 키를 평행이동 시켜 칸에 알맞게 들어가는지 확인해준다.
5. 만약 맞지 않으면 키를 90도 회전 시켜서 다시 해준다.

```python
def rotate(tmp_list): #키를 회전시키는 함수
    tmp = []
    for i in range(len(tmp_list)):
        tmp.append([tmp_list[i][1], -tmp_list[i][0]])
    return tmp

def solution(key, lock):
    answer = False
    n = len(lock)
    m = len(key)
    list_lock = set() # lock은 변하지 않음으로 set으로 고정
    for i in range(n):
        for j in range(n):
            if lock[i][j] == 0:
                list_lock.add((i, j))
    list_key = []
    #키 넣어주기
    for i in range(m):
        for j in range(m):
            if key[i][j] == 1:
                list_key.append([i, j])
    #자물쇠의 첫 부분을 베이스로 잡기
    for i in list_lock:
        base_x, base_y = i
        break

    if len(list_lock) == 0:
        return True
    if len(list_key) == 0:
        return False
    #키를 돌리면서 확인
    for _ in range(4):
        list_key = rotate(list_key)
        # 베이스와의 거리 차를 이용해 다른 key도 평행이동 시키기 위한 평행이동좌표 구하기
        for k_x, k_y in list_key:
            flag = True
            cx = base_x - k_x
            cy = base_y - k_y
            count = 0
            for diff_x, diff_y in list_key:
                x, y = diff_x + cx, diff_y + cy
                if 0 <= x < n and 0 <= y < n:
                    if (x, y) in list_lock:
                        count += 1
                        continue
                    else:
                        flag = False
                        break
            if flag and count == len(list_lock):
                return True

    return answer

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
```
https://jewin.notion.site/50ee9911befc471f8a4e016225efaebc
