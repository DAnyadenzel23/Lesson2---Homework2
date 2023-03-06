"""На входе список из чисел, каждое число повторяется два раза,
и только одно число повторяется 1 раз. Найти число, которое повторяется 1 раз.
пример:
1 6 2 5 2 9 6 1 5
вывести 9"""

a = int(input('Введите 1 число: '))
b = int(input('Введите 2 число: '))
c = int(input('Введите 3 число: '))
d = int(input('Введите 4 число: '))
e = int(input('Введите 5 число: '))
f = int(input('Введите 6 число: '))
g = int(input('Введите 7 число: '))

#Проверка первого числа:
if a!=b and a!=c and a!=d and a!=e and a!=f and a!=g:
    print(a)

#Проверка первого числа:
elif b!=a and b!=c and b!=d and b!=e and b!=f and b!=g:
    print(b)

#Проверка первого числа:
elif c!=a and c!=b and c!=d and c!=e and c!=f and c!=g:
    print(c)

#Проверка первого числа:
elif d!=a and d!=b and d!=c and d!=e and d!=f and d!=g:
    print(d)

#Проверка первого числа:
elif e!=a and e!=b and e!=c and e!=d and e!=f and e!=g:
    print(e)

#Проверка первого числа:
elif f!=a and f!=b and f!=c and f!=d and f!=e and f!=g:
    print(f)

#Проверка первого числа:
elif g!=b and g!=c and g!=d and g!=e and g!=f and g!=a:
    print(g)

else:
    print('Неправильно задали числа, не как в условии')