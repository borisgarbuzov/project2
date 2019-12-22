import numpy as np
import math
from sklearn.metrics import mean_squared_error

def find_bar(x):
    sum = 0
    for elem in x:
        sum += elem
    return sum / len(x)

def var_lower_than_mse(x=[2, 3, 4], c=1):
    print('Var is lower than MSE. Parametrs:')
    print('x =', x)
    print('c =', c)
    xbar = find_bar(x) 
    bias = xbar - c
    variance = np.var(x)
    mse = variance + bias ** 2
    print('xbar =', xbar)
    print('bias =', bias)
    print('var =', variance)
    print('mse =', mse)
    print('Now we check pythagorean_theorem...')
    if mse == variance + bias ** 2:
        print('True that mse = var + bias * bias')
    else:
        print('Its not true')
    
def xbar_equal_c(x=[2, 3, 4], c=3):
    print('\nNow xbar is equal center')
    print('x =', x)
    print('c =', c)
    xbar = find_bar(x) 
    bias = xbar - c
    variance = np.var(x)
    mse = variance + bias ** 2
    print('xbar =', xbar)
    print('bias =', bias)
    print('var =', variance)
    print('mse =', mse)
    
if __name__ == '__main__':
    var_lower_than_mse()
    xbar_equal_c()