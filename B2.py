from turtle import *

n = 3

for i in range(4):
    for i in range(n):
        forward(100)
        left(360/n)
    n = n + 1

mainloop()