
"""
cevap : 137846528820
"""


from math import *

grid = 2
while grid <= 20:
    a = factorial(grid)
    b = factorial(grid*2)
    answer = int(b / (a**2))
    print("{} x {} karede toplam {} yol var.".format(grid, grid, answer))
    grid += 1
    
print(answer)