
N = int(input())
Q = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))


min_servings_A = min(Q[i] // A[i] if A[i] != 0 else float('inf') for i in range(N))
min_servings_B = min(Q[i] // B[i] if B[i] != 0 else float('inf') for i in range(N))

max_total_servings = 0
for a_servings in range(min_servings_A + 1):
    b_servings = min((Q[i] - a_servings * A[i]) // B[i] if B[i] != 0 else float('inf') for i in range(N))
    max_total_servings = max(max_total_servings, a_servings + b_servings)

print(max_total_servings) 
