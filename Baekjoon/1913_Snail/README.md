# 문제

[1913번: 달팽이](https://www.acmicpc.net/problem/1913)

# 풀이

처음에 문제에서 1부터 시작해서 n^2까지 가는 방법으로 풀려고 했는데 그렇게 하면 일정 규칙(1칸씩 2번, 2칸씩 2번,, 이런 규칙)이 있긴 하지만 어디가 벽인지, 그리고 마지막에는 몇칸씩 두번이 아니라 세번이 되기 때문에 구현하는데 어려움이 있을거라고 생각했다. 

그래서 고민을 해보다가 차라리 마지막 숫자인 n^2부터 세어 나가면 괜찮을 것 같다는 생각을 하게 되었다. 그렇게 하면 방향을 바꾸는 조건과 종료 조건이 명확해진다. 방향을 바꾸는 조건은 벽에 부딪히거나 0이 아닌 다른 숫자를 만났을때 방향을 바꿔주면서 숫자를 채워나간다. 그렇게 되면 마지막 종료조건은 가장 가운데 있는 숫자가 1이 되면, 즉 array[n//2][n//2]가 1이 되면 조건에 해당하여 모든 숫자를 채울 수 있게 된다. 

# 코드

[JewinJeong/Algorithm](https://github.com/JewinJeong/Algorithm/tree/master/Baekjoon/Snail_1913)