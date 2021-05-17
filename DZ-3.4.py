"""Возводит положительное число х в степень равную отрицательному числу у"""
#def my_func(x, y):
#    c = round(x ** y, 2)
#    return(c)

#print(my_func(3, -3))


"""Второй вариант функции выше"""
def my_func(x, y):
    n = abs(y)
    c = x
    i = 1
    while i < n:
        x *= c
        i += 1
    return(round(1 / x, 2))

print(my_func(3, -3))
      