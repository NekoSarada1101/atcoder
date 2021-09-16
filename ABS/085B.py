N = int(input())
d = []
for i in range(N):
    d.append(int(input()))

d.sort()
before = 0
result = 0
for i in range(N):
    if d[i] > before:
        result += 1
        before = d[i]
print(result)
