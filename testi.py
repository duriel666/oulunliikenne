import time

run = True
i = 1
while run:
    start_time = time.time()
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(f'{i} - {time.time() - start_time:.4f} s since last prime')
    i += 1
