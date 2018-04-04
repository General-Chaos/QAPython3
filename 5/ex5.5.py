from math import pi, cos, tan
import matplotlib.pyplot as pyplot

g = 9.81
v0 = 44
theta = 80 * pi/180
x = 0.0
y0 = 1
y = 1
x_axis = []
y_axis = []


while y > 0:
    y = y0 + (x * tan(theta)) - ((g * x**2)/(2*(v0 * cos(theta))**2))
    x_axis.append(x)
    y_axis.append(y)
    x += 0.1

pyplot.ylabel('Height m')
pyplot.xlabel('Distance m')
pyplot.ylim(-1, max(max(x_axis), max(y_axis)))
pyplot.plot(x_axis, y_axis)
pyplot.show()
