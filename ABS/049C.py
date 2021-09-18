S = input()[::-1]
T = ''
word = ['dream', 'dreamer', 'erase', 'eraser']
for i in range(len(word)):
    word[i] = word[i][::-1]

flg = True
i = 0
while i < len(S):
    flg2 = False
    for w in word:
        if S[i:i + len(w)] == w:
            flg2 = True
            i += len(w)
    if flg2 is False:
        flg = False
        break

if flg is False:
    print('NO')
else:
    print('YES')
