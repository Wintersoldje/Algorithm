import collections
def solution(arrows):
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]
    x = 0
    y = 0
    answer = 0
    node = collections.defaultdict(int)
    vertex = collections.defaultdict(int)
    queue = collections.deque()
    queue.append((0,0))
    for arrow in arrows:
        for i in range(2): #x 모양으로 교차될때 좌표가 없을 수 있기 때문에 2배로 만들어준다.
            nx = x + dx[arrow]
            ny = y + dy[arrow]
            queue.append((nx, ny)) # queue에 이동한 모든 좌표를 넣어준다.
            x = nx
            y = ny

    now = queue.popleft()
    node[now] = 1

    while queue:
        next = queue.popleft()
        if node[next] == 1: #방문 함
            if vertex[(now,next)] == 0: # 간선이 겹치지 않는다면,  answer 1 올려줌
                answer += 1
        else:
            node[next] = 1
        print(node)
        # now, next로 움직이는 부분 즉, 간선을 1로 바꿔준다.
        vertex[(now, next)] = 1
        vertex[(next, now)] = 1
        now = next

    return answer

print(solution([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]))