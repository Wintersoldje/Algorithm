n = input(str)
len_num = len(n)
sum1 = 0
sum2 = 0

# 절반을 나눠서 합 비교
for i in range(len_num//2):
    sum1 += int(n[i])
    sum2 += int(n[i+len_num//2])

if sum1 == sum2 :
    print("LUCKY")
else:
    print("READY")
