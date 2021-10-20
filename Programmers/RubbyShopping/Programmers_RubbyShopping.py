def solution(gems):
    answer = []
    shortest = len(gems) + 1

    start = 0
    end = 0
    contained = {}
    len_ruby = len(set(gems))

    while end < len(gems):
        if gems[end] not in contained:
            contained[gems[end]] = 1
        else:
            contained[gems[end]] += 1

        end += 1

        if len(contained) == len_ruby:
            while start < end:
                if contained[gems[start]] > 1:
                    contained[gems[start]] -= 1
                    start += 1
                elif shortest > end - start:
                    shortest = end - start
                    answer = [start + 1, end]
                    break
                else:
                    break

    return answer

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))