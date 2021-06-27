def a(x, y):
    if x > 8 and y > 8:
        print(x * y)
    elif x < 8 or y < 8:
        print(x + y)
    else:
        print("Error")


a(10, 15)


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


def c(ap):
    if 4 < ap <= 10:
        print(2 * ap)
    else:
        print(ap - 55)


c(6)


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

for Loading in range(8):
    print("Loading...")


def zxc(count):
    while count != 160:
        print(count)
        count = count + 10


zxc(0)

