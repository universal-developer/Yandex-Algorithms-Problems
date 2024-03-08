def main(a, b, c):
    if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
        return 'YES'
    else:
        return 'NO'


# Вводим три натуральных числа и выводим результат работы функции на экран
a = int(input())
b = int(input())
c = int(input())
print(main(a, b, c))
