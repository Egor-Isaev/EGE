import turtle
from turtle import *

turtle.tracer(0)
koef = 20
# Алгоритм рисования фигуры
for i in range(2):
    forward(10 * koef)
    right(90)
    forward(18 * koef)
    right(90)
up()
forward(5 * koef)
right(90)
forward(7 * koef)
left(90)
down()
for i in range(2):
    forward(10 * koef)
    right(90)
    forward(7 * koef)
    right(90)
# Алгоритм рисования сетки
up()
for x in range(-koef, koef):
    for y in range(-koef, koef):
        goto(x * koef, y * koef)
        dot(3)
done()
