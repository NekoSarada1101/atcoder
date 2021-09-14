n = int(input())
list = list(map(int, input().split()))

cnt = 0
while(True):
    is_even = True
    for i in list:
        if i % 2 != 0:
            is_even = False

    if is_even:
        cnt += 1
        for i in range(n):
            list[i] = list[i] / 2
    else:
        break
print(cnt)
