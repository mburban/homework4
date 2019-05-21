# Написать программу, которая отвечает на вопрос, пересекаются ли две заданные окружности на плоскости.
# Каждая окружность задается координатами центра и радиусом.

import math

x1 = int(input('Enter the X coordinate of the first circle: '))
y1 = int(input('Enter the Y coordinate of the first circle: '))
r1 = int(input('Enter the radius of the first circle: '))
x2 = int(input('Enter the X coordinate of the second circle: '))
y2 = int(input('Enter the Y coordinate of the second circle: '))
r2 = int(input('Enter the radius of the second circle: '))
distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
radius_sum = r1 + r2
radius_difference = r1 - r2
if distance <= radius_sum and distance >= radius_difference:
    print('Circles are intersect')
else:
    print('Circles are not intersect')
