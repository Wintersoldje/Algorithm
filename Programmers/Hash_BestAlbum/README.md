# 문제

[코딩테스트 연습 - 베스트앨범](https://programmers.co.kr/learn/courses/30/lessons/42579)

# 풀이

해시 문제를 많이 풀어보지 않아서 key-value 사용법을 찾아보고 문제를 풀었다. 

문제의 알고리즘은 간단했다. 기본적으로 처음에 장르별로 play 횟수를 저장한다. 그래서 플레이 횟수가 가장 많은 장르를 보기 위해 정렬을 해주었다. 그리고 모든 play 횟수를 정렬해주어 가장 많은 플레이 횟수 순으로 최대 2개 출력해 주었다.

1. playList에 장르의 play 횟수의 총 합을 장르별로 저장해준다.
2. playTimeList에는 play횟수와 인덱스를 저장해준다.
3. playList와 playTimeList를 정렬해주는데, playTimeList는 play수에 대한 정렬 및 같은 횟수이면 index 적은대로 정렬해준다.
4. 마지막으로 정렬된 리스트를 가장 많은 장르의 인덱스 번호를 최대 2개 출력해준다.

```python
def solution(genres, plays):
    answer = []
    playList = {}
    playTimeList = {}
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        playList[genre] = playList.get(genre, 0) + play #장르에 해당하는 play시간 합쳐주기
        playTimeList[genre] = playTimeList.get(genre, []) + [(play, i)] #해당하는 장르에 play시간과 인덱스 입력
    sorted_genre = sorted(playList.items(), key=lambda x:x[1], reverse=True) #재생 횟수에 따른 장르 정렬
    for playtime in playTimeList.keys(): #play수에 대한 정렬 및 같은 횟수이면 index 적은대로 정렬
        tmp = sorted(playTimeList[playtime], key=lambda x:(x[0],-x[1]), reverse=True)
        playTimeList[playtime] = tmp

    for i in range(len(sorted_genre)):
        for tmp_key in playTimeList.keys():
            if sorted_genre[i][0] == tmp_key:
                for j in range(len(playTimeList[tmp_key])):
                    if j == 2:
                        break
                    answer.append(playTimeList[tmp_key][j][1])
    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500]))
```
