import numpy as np
import matplotlib.pyplot as plt
import time


def benchmarking():
    
    noise_sizes = np.arange(10,1000,10)
    measured_dict = {}
    for noise_size in noise_sizes:
        start = time.time()
        create_noise(noise_size=noise_size, mean=5, sigma=2, noise_type="bernoulli")
        time_dif = time.time() - start
        measured_dict[noise_size] = time_dif

        
    print('\ndictionary with measures per noise_size ',measured_dict)
    del measured_dict[10] # eliminate firt time outlier
    plt.plot(list(measured_dict.keys()), list(measured_dict.values()), 'o', color='black')
    plt.xlabel('noise_size')
    plt.ylabel('time (sec)')
    plt.title('create_noise (Python)')
    

    plt.savefig('measure_create_noise_Pyhton.png')


def create_noise(noise_size: int, mean: float, sigma: float,
                 noise_type: str) -> float:
    """
    create "gaussian" or "bernoulli" noise.

    :param noise_size: size of noise
    :param mean: mean
    :param sigma: sigma
    :param noise_type: type
    :return: float noise
    """
    if noise_type == "gaussian":
        return np.random.normal(mean, sigma, noise_size)
    elif noise_type == "bernoulli":
        classic_bernoulli = np.random.binomial(1, 1 / 2, noise_size)
        return sigma * ((2 * classic_bernoulli) - 1)
    else:
        raise ValueError("noise_type should be 'gaussian' or 'bernoulli'.")
        
        
        
if __name__ == '__main__':
    benchmarking()
