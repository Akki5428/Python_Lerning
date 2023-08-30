"""
def fibo(n):
    if n == 1 or n == 2:
        return 1
    else :
        return fibo(n-1) + fibo(n-2)

n = int(input())
print(fibo(n))
"""
cache_memory = {}

def fibo(n):
    if n in cache_memory:
        return cache_memory[n]
    if n == 1 or n == 2:
        cache_memory[n]=1
        return 1
    else :
        term = fibo(n-1) + fibo(n-2)
        cache_memory[n] = term
        return term

a = int(input())

print("Fibo Series:")
for i in range(1,a+1):
    print(i,":",fibo(i))