from math import pi, cos, tan

g = 9.81
v0 = 44
theta = 80 * pi/180
x = 0.5
y0 = 1

y = y0 + (x * tan(theta)) - ((g * x**2)/(2*(v0 * cos(theta))**2))

print(y)
