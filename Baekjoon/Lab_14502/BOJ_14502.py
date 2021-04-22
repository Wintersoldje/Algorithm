# from copy import deepcopy
# import sys
#
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
# list_map = [list(map(int, input().split())) for _ in range(m)]
# max_value = 0
# list_virus = []
# #바이러스 리스트 만들기
# for i in range(n):
#     for j in range(m):
#         if list_map[i][j] == 2:
#             list_virus.append([i, j])
# #위 우 아래 좌
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
#
#
# #벽 선택하기
# def select_wall(start, count):
#     global max_value
#     #벽 다 설치했으면 바이러스 퍼트리기
#     if count == 3:
#         cp_map = deepcopy(list_map)
#         for i in range(len(list_virus)):
#             x, y = list_virus[i]
#             spread_virus(x, y, cp_map)
#         safe_count = sum(i.count(0) for i in cp_map)
#         max_value = max(max_value, safe_count)
#         return True
#     else:
#         for i in range(start, n*m):
#             x = i // m
#             y = i % m
#             if list_map[x][y] == 0:
#                 list_map[x][y] = 1
#                 select_wall(i, count+1)
#                 list_map[x][y] = 0
#
# def spread_virus(x, y, map):
#     if map[x][y] == 2:
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < n and 0 <= ny < m:
#                 if map[nx][ny] == 0:
#                     map[nx][ny] = 2
#                     spread_virus(nx, ny, map)
#
# select_wall(0, 0)
# print(max_value)

import copy
from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

max_result = 0
q = deque()

def bfs():
    global max_result
    tmp_list = copy.deepcopy(graph)
    for i in range(n): #  바이러스 퍼트리기
        for j in range(m):
            if tmp_list[i][j] == 2:
                q.append([i,j])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and ny >= 0 and nx < n and ny < m:
                if tmp_list[nx][ny] == 0:
                    tmp_list[nx][ny] = 2
                    q.append([nx, ny])
    ans = 0
    for i in tmp_list:
        ans += i.count(0)
    max_result = max(ans, max_result)

def wall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                wall(cnt + 1)
                graph[i][j] = 0

wall(0)
print(max_result)