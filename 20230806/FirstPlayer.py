N = int(input())
names = []
ages = []
for _ in range(N):
    name, age = input().split()
    names.append(name)
    ages.append(int(age))
min_age_index = ages.index(min(ages))
 
for i in range(N):
    index = (min_age_index + i) % N
    print(names[index])