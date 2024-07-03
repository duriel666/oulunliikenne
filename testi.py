# Description: This is a test file to test random code snippets.

import time

run = True
i = 1
total = 0
total_time = time.time()
while run:
    start_time = time.time()
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        total += 1
        print(
            f"{i} - {time.time() - start_time:.4f} s since last prime - {total} primes found - {time.time() - total_time:.2f} s total time"
        )
    i += 1
