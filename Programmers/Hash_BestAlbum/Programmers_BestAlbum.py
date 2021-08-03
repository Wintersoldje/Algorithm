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