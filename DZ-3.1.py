def div_num():
    num1 = int(input('Введите первое число: '))
    num2 = int(input('Введите второе число: '))
    if num2 == 0:
        num2 = int(input('На ноль делить нельзя! Введите другое число: '))
        res = round(num1 / num2, 2)
    else:
        res = round(num1 / num2, 2)
    return res

print(div_num())
