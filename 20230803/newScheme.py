s = list(map(int, input().split()))

min_s = min(s)
max_s = max(s)
div_list = all(num % 25 == 0 for num in s)

if min_s >= 100 and max_s <= 675 and s == sorted(s) and div_list: 
    print("Yes")
else:
    print("No")