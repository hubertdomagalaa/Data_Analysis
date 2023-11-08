


import pandas as pd
import matplotlib as plt


def nww(a, b):
    x = list(range(1, 1000000000000000000000000000))
    for y in x:
        while (a % y == 1) and (b % y == 1):
            return y
        



nww(140, 66)




    