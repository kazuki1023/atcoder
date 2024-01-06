import re
n = int(input())
s = input()

a = re.split('(.)', s)[1::2]
result =[0] * len(a)
for d in range(len(a)):
    result[d] = a[d] + a[d]

answer = ''.join(result)
print(answer)