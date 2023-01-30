import matplotlib.pyplot as plt

x = 1
num = int(input('Enter Start Number: '))
axis_x = [x]
axis_y = [num]

def toUp(n):
    return 3*n+1

def toDown(n):
    return n // 2

while num != 1:
    x += 1
    if num%2 == 0:
        num = toDown(num)
    else:
        num = toUp(num)
    axis_x.append(x)
    axis_y.append(num)

plt.plot(axis_x, axis_y)
plt.show()




