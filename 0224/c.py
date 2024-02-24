n = int(input())
s = list(input())
q = int(input())
t = [list(map(str, input().split())) for t in range(q)]
replace_map = {chr(ord('a') + i): chr(ord('a') + i) for i in range(26)}

for c_i, d_i in t:
    for key, value in list(replace_map.items()):
        if value == c_i:
            replace_map[key] = d_i

final_s = ''.join(replace_map[char] for char in s)

print(final_s)
