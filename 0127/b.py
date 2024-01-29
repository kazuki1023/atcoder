from collections import Counter
s= list(input())
counter = Counter(s)
most_common = counter.most_common()
max_count = most_common[0][1]
result = min([char for char, count in most_common if count == max_count])

print(result)
