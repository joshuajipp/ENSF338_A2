
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
        memo[n] = func_memo(n - 1, memo) + func_memo(n - 2, memo)
        return memo[n]

