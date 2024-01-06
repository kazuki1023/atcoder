a,b = map(int,input().split())

q, r = divmod(a, b)
if r == 0:
    print(q)
else:
    print(q + 1)