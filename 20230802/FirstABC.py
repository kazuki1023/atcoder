N = int(input())
S = input()
size = [0, 0, 0]
size[0] = S.find("A")
size[1] = S.find("B")
size[2] = S.find("C")
print(max(size) + 1)