N, A, B = map(int, input().split())

total = 0
for i in range(1, N + 1):
    s = sum(list(map(int, list(str(i)))))

    if A <= s <= B:
        total += i
print(total)
