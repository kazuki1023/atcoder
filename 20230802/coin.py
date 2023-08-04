A = int(input())
B = int(input())
C = int(input())
X = int(input())
# xを500で割った余りをｘｒとする
AR = 0
X , AR = divmod(X, 500)
if(AR != 0):
    X = X + 1