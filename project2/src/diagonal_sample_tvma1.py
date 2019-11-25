from src.create_noise import create_noise
from src.coef import coef
import numpy as np
import matplotlib.pyplot as plt
import time


def benchmarking():
    
    sample_sizes = np.arange(10,1000,10)
    measured_dict = {}
    for sample_size in sample_sizes:
        start = time.time()
        diagonal_sample_tvma1(sample_size=sample_size, mean=5, sigma=2, noise_type="gaussian")
        time_dif = time.time() - start
        measured_dict[sample_size] = time_dif

        
    print('\ndictionary with measures per sample_size ',measured_dict)
    del measured_dict[10] # eliminate firt time outlier
    plt.plot(list(measured_dict.keys()), list(measured_dict.values()), 'o', color='black')
    plt.xlabel('sample_size')
    plt.ylabel('time (sec)')
    plt.title('diagonal_sample_tvma1 (Python)')
    plt.savefig('measure_diagonal_sample_tvma1_(Python).png')


def diagonal_sample_tvma1(sample_size: int, mean: float, sigma: float,
                          noise_type: str) -> np.array:
    """
    Create diagonal sample tvma1.

    :param sample_size: len of sample
    :param mean: mean
    :param sigma: sigma
    :param noise_type: type
    :return: diagonal sample tvma1
    """
    noise = create_noise(noise_size=sample_size + 1, mean=mean, sigma=sigma,
                         noise_type=noise_type)
    diagonal_sample_tvma1 = np.full(shape=sample_size, fill_value=np.nan)
    for i in range(1, sample_size + 1):
        diagonal_sample_tvma1[i - 1] = coef(t_par=i / sample_size) * noise[
            i - 1] + noise[i]
    return diagonal_sample_tvma1
    
    
if __name__ == '__main__':
    benchmarking()
