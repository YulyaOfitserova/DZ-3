
def my_sum():
    total = 0
    qu = True
    while qu == True:
        numbers = input('Введите числа через пробел (если хотите выйти из приложения, нажмите Q): ').split()
        result = 0
        for ind in range(len(numbers)):
            if numbers[ind] == 'Q' or numbers[ind] == 'q':
                qu = False
                break
            else:
                result = result + int(numbers[ind])
        total = total + result
        print(f'Сумма введенной строки - {result}')
        print(f'Сумма всех чисел - {total}')

my_sum()
