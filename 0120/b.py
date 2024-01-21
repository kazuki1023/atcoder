s = input()
aIndex = s.find("A")
bIndex = s.find("B")
aCount = s.count("A")
bCount = s.count("B")
cIndex = s.find("C")
cCount = s.count("C")
l = len(s)
if aCount == l and aCount == 1:
  print("Yes")
elif aCount == bIndex and bCount == cIndex - bIndex and cCount == l - cIndex:
  print("Yes")
else:
  print("No")
