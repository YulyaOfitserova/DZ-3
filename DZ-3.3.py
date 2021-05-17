"""Складывает два наибольших числа из трех"""
#def sum_max(num1, num2, num3):
#    a = min(num1, num2, num3)
#    res = num1 + num2 + num3 - a
#    return res

#print(sum_max(3, 4, 5))

"""Складывает два наибольших числа из трех через lambda"""
sum_max = lambda num1, num2, num3: num1 + num2 + num3 - min(num1, num2, num3)
print(sum_max(2, 3, 6))
