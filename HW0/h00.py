def f(n):
    while n < 10:
        if n < 3:
            n = n + 2
        elif n < 6:
            return n
        if n < 10:
            n = n + 5
            return n
    return n
def countOdds(x):
    n = 0
    for i in x:
        if i % 2 == 0:
            n = n
        elif i % 2 == 1:
            n = n +1
    return n
countOdds([1,2,3])
countOdds([]) 
countOdds([3,3,5]) 
