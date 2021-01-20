s = input()
c = []
n = []
for i in range(len(s)):
    if ord(s[i]) >=65 and ord(s[i]) <= 90:
        c.append(s[i])
    else:
        n.append(int(s[i]))
c.sort()
sum = sum(n)
c.append(str(sum))
str1 = ''.join(c)
print("%s" %str1)