n = int(input())
a = list(map(int, input().split()))

first = 0
minpa = 0

for change in a:
    first += change
    minpa = max(minpa, -first)

print(minpa + sum(a))

