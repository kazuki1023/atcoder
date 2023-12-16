s= input().split()
t= input().split()
len1 = ['AB', 'BA', 'BC', 'CB', 'DC', 'CD', 'DE', 'ED', 'AE', 'EA']

if (s[0] in len1):
  s = 1
else:
  s = 2
if (t[0] in len1):
  t = 1
else:
  t = 2

if (s == t):
  print("Yes")
else:
  print("No")

