# import heapq
# #
# # def solution(tickets):
# #     answer = []
# #     heap = []
# #     tickets.sort(key=lambda x:x[1])
# #     count = 0
# #     for s, e in tickets:
# #         if s == "ICN" and count == 0:
# #             answer.append(s)
# #             answer.append(e)
# #             count += 1
# #         else:
# #             heap.append((s,e))
# #     heap.sort(key=lambda x:x[1])
# #     while heap:
# #         for i in range(len(heap)):
# #             start, end = heap[i]
# #
# #             if answer[-1] == start:
# #                 answer.append(end)
# #                 heap.remove((start,end))
# #                 break
# #     return answer
# answer = ["ICN"]
# flag = 0
# def dfs(start, tickets):
#     heap = []
#     global flag
#     if flag == 1 :
#         return
#     if len(tickets) == 0:
#         flag = 1
#         # print(answer)
#         return
#
#     for s, e in tickets:
#         if s == start:
#             heapq.heappush(heap, (e))
#
#     while heap:
#         # print(heap)
#         # print("answer", answer)
#         end = heapq.heappop(heap)
#         tickets.remove([start, end])
#         answer.append(end)
#         dfs(end, tickets)
#         if flag == 1: break
#         answer.pop()
#         #print(answer)
#         tickets.append([start, end])
#     return answer
#
# def solution(tickets):
#     a = dfs("ICN", tickets)
#     return a
import heapq
flag = 0
a = ["ICN"]
def dfs(depart, tickets):
    global flag
    global a

    heap = []
    if flag == 1:
        return
    if len(tickets) == 0:
        flag = 1
        return

    for start, end in tickets:
        if start == depart:
            heapq.heappush(heap, (end))
    while heap:
        end = heapq.heappop(heap)
        tickets.remove([depart, end])
        a.append(end)
        dfs(end, tickets)
        if flag == 1:
            break
        a.pop()
        tickets.append([depart, end])
    return

def solution(tickets):
    dfs("ICN", tickets)
    return a

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))