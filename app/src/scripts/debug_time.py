import time


start = time.time()
time.sleep(2)
end = time.time()
diff = round(end - start, 4)

print(f"\nTotal time - {diff} seconds.\n")
