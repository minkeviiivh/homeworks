fibonacci1 = 1
fibonacci2 = 1
n = input("Пользователь ввёл индекс ")
n = int(n)
i = 0
while i < n - 2:
    fib_sum = fibonacci1 + fibonacci2
    fibonacci1 = fibonacci2
    fibonacci2 = fib_sum
    i = i + 1
print("Результат: число Фибоначчи =", fibonacci2)
