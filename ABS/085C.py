N, Y = map(int, input().split())

for x in range(N + 1):
    for y in range(N - x + 1):
        z = N - x - y
        if 10000 * x + 5000 * y + 1000 * z == Y:
            print('{} {} {}'.format(x, y, z))
            break
    else:
        continue
    break
else:
    print('{} {} {}'.format(-1, -1, -1))
