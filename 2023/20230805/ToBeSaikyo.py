n = int(input())
p = list(map(int, input().split()))
if(p[1:] == [] ):
    print(0)
else:
    if p[0] > max(p[1:]):
      print(0)
    else:
      print(max(p[1:])-p[0] + 1)