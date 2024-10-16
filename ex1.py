def caching_fibonacci():
    chace = {}
    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in chace:
            return chace[n]
        chace[n] = fibonacci(n -1 ) + fibonacci(n - 2)
        return chace[n]        
    return  fibonacci
fib = caching_fibonacci()
print(fib(10)) 