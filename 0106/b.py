s = int(input())
for x in range(22):
  for  y in range(22):
    for  z in range(22):
      if (x + y + z <= s):
        print(x, y, z)
