import timeit
import matplotlib.pyplot as plt

def func(n):
    if n==0 or n==1:
        return n
    else:
        return func(n-1) + func(n-2)

def func_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n==0 or n==1:
        return n
    else:
        memo[n] = func_memo(n-1, memo) + func_memo(n-2, memo)
        return memo[n]

original_code =[]
new_code=[]

for n in range(36):
    original_time = timeit.timeit(lambda: func(n), number=1)
    original_code.append(original_time)

    new_time = timeit.timeit(lambda: func_memo(n))
    new_code.append(new_time)

plt.plot(original_code, label="Original")
plt.plot(new_code, label="New")
plt.xlabel("Number")
plt.ylabel("time(s)")
plt.legend()
plt.show()