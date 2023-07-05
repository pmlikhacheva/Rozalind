#not ready
n = 5 #месяцы
k = 3 #сколько пар кроликов воспроизводит одна пара
sum = 0
def Rabbits(n, k):
    if n <= 1:
        return n
    else:
        x = Rabbits(n-1)
        y = Rabbits(n-2)
        return x + y

print(*Rabbits(n, k))

