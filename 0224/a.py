s = list(input())  
n = len(s)


if s[0] != s[1]:
    if s[0] != s[2]:  
        print(1) 
    else:
        print(2) 
else:
    for i in range(2, n):
        if s[i] != s[0]:
            print(i + 1)
            break
