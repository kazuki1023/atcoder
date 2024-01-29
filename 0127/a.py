s = input()
if (len(s) == 1 and s.isupper()):
    print("Yes")
    exit()
if (s[0].isupper() and s[1:].islower()):
    print("Yes")
else:
    print("No")

