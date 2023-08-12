n = int(input())
q ,r = divmod(n, 5)
if r >= 3:
    print(q*5 +5)
else:
    print(q*5)