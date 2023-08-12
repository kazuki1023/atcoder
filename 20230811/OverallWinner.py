n = int(input())
s = input()
tCount = s.count('T')
acount = n - tCount
if tCount > acount:
    print('T')
elif tCount < acount:
    print('A')
elif tCount == acount:
    if s.rfind('T') > s.rfind('A'):
        print('A')
    else:
        print('T')
