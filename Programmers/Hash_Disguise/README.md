# 문제

[코딩테스트 연습 - 위장](https://programmers.co.kr/learn/courses/30/lessons/42578)

# 풀이

문제는 우선 옷의 종류를 key값으로 두고 value는 옷의 이름을 적으면 된다고 생각했다. 

dictionary를 만들어주고, 이제 경우의 수를 구하는게 문제인데, 모든 종류의 옷의 수 에서 +1을 해주고 모두 곱해주면 모든 경우의 수가 나온다. 하지만 옷을 최소 하나는 입는다고 했기 때문에 마지막에 -1을 해준다.

1. Dictionary에 의상의 종류를 key로 이름을 value로 넣어준다. 
2. 경우의 수를 구하기 위해 (종류별 옷의 갯수 + 1) 를 모든 종류별로 곱해준다.
3. 마지막에 result에서 -1을 해준다.

```python
def solution(clothes):
    dict = {}
    result = 1
    for i in range(len(clothes)):
        clothe, kinds = clothes[i]
        dict[kinds] = dict.get(kinds, []) + [clothe]
    for key in dict.keys():
        result = result * (len(dict[key])+1)
    return result - 1
```
