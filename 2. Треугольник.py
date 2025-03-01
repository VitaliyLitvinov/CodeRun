# Даны три натуральных числа. Возможно ли построить треугольник с такими
# сторонами? Если это возможно, выведите строку YES, иначе выведите строку NO.
#
# Треугольник — это три точки, не лежащие на одной прямой.
#
# Формат ввода
# Вводятся три натуральных числа.
#
# Формат вывода
# Выведите ответ на задачу.

    a, b, c = int(input()), int(input()), int(input())
    median = (a + b + c) - max(a, b, c) - min(a, b, c)
    print("YES" if max(a, b, c) < min(a, b, c) + median else 'NO')