import time

count = 10**6
t1 = time.time()
nums = []
for i in range(count):
    nums.append(i)

nums.reverse()
print(time.time() - t1)
t2 = time.time()
nums = []
for i in range(count):
    nums.insert(0, i)

print(time.time() - t2)
# 0.012000799179077148
# 2.972169876098633