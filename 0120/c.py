n = int(input())
l = list(map(int, input().split()))
# print(l)
# print(l.index(-1) + 1)
result = [0 for i in range(n)]
index_dict = {index + 1: value for index, value in enumerate(l)}

def inverse_dic(dictionary):
  return {v:k for k,v in dictionary.items()}
reverse = inverse_dic(index_dict)
# print(reverse)


for i in range(n):
  if i == 0:
    result[i] = l.index(-1) + 1
  else:
    result[i] = reverse[result[i - 1]]

r = " ".join(map(str, result))
print(r)
