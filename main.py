def a(x, y):
    if x > 8 and y > 8:
        print(x * y)
    elif x < 8 or y < 8:
        print(x + y)
    else:
        print("Error")


a(10, 15)

print('///////////////////////')


def b(z, x, c):
    if z > 0 and x > 0 and c > 0:
        print(z + x + c)
    elif z == 0 and c == 0 or z == 0 and x == 0 or c == 0 and x == 0:
        print(0)
    elif z < 0 and c < 0 or z < 0 and x < 0 or c < 0 and x < 0:
        print(z * x * c)
    else:
        print("Error")


b(4, 6, 2)

print('///////////////////////')


def c(ap):
    if 4 < ap <= 10:
        print(2 * ap)
    else:
        print(ap - 55)


c(6)

print('///////////////////////')


def d(d1, d2, d3):
    if d1 < d2:
        z = d1
    else:
        z = d2
    if d3 < z:
        z = d3
    x = d1 + d2 + d3 - z
    print(x)


d(3, 4, 8)
print('///////////////////////')

for Loading in range(8):
    print("Loading...")

print('///////////////////////')


def zxc(count):
    while count != 160:
        print(count)
        count = count + 10


zxc(0)

print('///////////////////////')
l1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
intersection = []
for x in l1:
    if x in l2:
        intersection.append(x)
print(intersection)

print('///////////////////////')

l3 = [1, 51, 22, 9, 5, 0]
l3.sort()
print(l3)

print('///////////////////////')

dict1 = {1: 10, 2: 20}
dict2 = {3: 30, 4: 40}
result = {}
for d in (dict1, dict2):
    result.update(d)
print(result)

print('///////////////////////')

values = input('Введите числа через запятую: ')
ints_as_strings = values.split(',')
ints = map(int, ints_as_strings)
lst = list(ints)
tup = tuple(lst)
print('Список:', lst)
print('Кортеж:', tup)

print('///////////////////////')

sp1 = [1, 2, 3, 4, 5]
print(sp1[0], sp1[-1])

print('///////////////////////')


def count(n):
    n1 = n
    n2 = int(str(n) * 2)
    n3 = int(str(n) * 3)
    print(n1 + n2 + n3)


count(5)
