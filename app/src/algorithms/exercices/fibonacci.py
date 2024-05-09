import time

fib = [0, 1]


def fibonacci(x: int):
    for i in range(len(fib), x + 1):
        fib.append(fib[i - 2] + fib[i - 1])

    return fib[x]


start = time.time()

for i in range(1, 15):
    print(i, "-", fibonacci(i))

# 1 - 1
# 2 - 1
# 3 - 2
# 4 - 3
# 5 - 5
# 6 - 8
# 7 - 13
# 8 - 21
# 9 - 34
# 10 - 55
# 11 - 89
# 12 - 144
# 13 - 233
# 14 - 377

end = time.time()
diff = round(end - start, 4)
print(f"\nTime - {diff} secs.\n")
