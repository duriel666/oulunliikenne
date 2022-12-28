run = True
i = 2
while run:
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)
    i += 1
