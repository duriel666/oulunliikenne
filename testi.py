import time

run = True
i = 1000000
while run:
    start_time = time.time()
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i, time.time() - start_time)
    i += 1
