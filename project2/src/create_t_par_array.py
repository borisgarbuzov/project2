import numpy as np
import matplotlib.pyplot as plt
import time

def benchmarking():
    
    t_par_counts = np.arange(10,1000,10)
    measured_dict = {}
    for t_par_count in t_par_counts:
        start = time.time()
        create_t_par_array(t_par_count=t_par_count)
        time_dif = time.time() - start
        measured_dict[t_par_count] = time_dif
        
    print('\ndictionary with measures per t_par_count ',measured_dict)
    del measured_dict[10] # eliminate firt time outlier
    plt.plot(list(measured_dict.keys()), list(measured_dict.values()), 'o', color='black')
    plt.xlabel('t_par_count')
    plt.ylabel('time (sec)')
    plt.title('create_t_par_array (Python)')
    

    plt.savefig('measure_create_t_par_array_Python.png')

def create_t_par_array(t_par_count):
    if t_par_count <= 1:
        raise ValueError(
            "t_par_count is 1 or smaller, whereas it should be 2 or greater")
    t_par_count_inner = t_par_count - 1
    t_par_array = np.arange(0, 1, 1 / t_par_count_inner)
    return np.append(t_par_array, 1)
    
    
if __name__ == '__main__':
    benchmarking()
