from src.diagonal_sample_tvma1 import diagonal_sample_tvma1
from src.horizontal_sample_tvma1 import horizontal_sample_tvma1
from src.diagonal_sample_scaled_noise import diagonal_sample_scaled_noise
from src.horizontal_sample_scaled_noise import horizontal_sample_scaled_noise
from src.create_t_par_array import create_t_par_array
from src.true_cov import true_cov_ma1
from src.cov_hat import cov_hat
from src.plot_double_array import plot_double_array
import numpy as np
import time
import matplotlib.pyplot as plt


def benchmarking():
    
    sample_sizes = np.arange(1000,10000,1000)
    measured_dict = {}
    time_per_operation_big_array = []
    time_per_operation_mean_dict = {}
    for sample_size in sample_sizes:
        start = time.time()
        time_per_operation_array = compute_and_save_cov_and_cov_hats(sample_size=sample_size,
                                          t_par_count=11,
                                          gamma_count=5,
                                          mean=0,
                                          sigma=2,
                                          lag=2,
                                          type_process='MA1',
                                          noise_type='bernoulli',
                                          diag_or_horiz='diag')
        time_dif = time.time() - start
        measured_dict[sample_size] = time_dif
        time_per_operation_big_array.extend(time_per_operation_array)
        time_per_operation_mean_dict[sample_size] = np.mean(time_per_operation_array)
        
    print('\nlist of times per operation ',time_per_operation_big_array)
    print('\ndict of mean times per operation for each sample ',time_per_operation_mean_dict)
    print('\noperation mean ',np.mean(time_per_operation_big_array))
    print('\ndictionary with measures per sample_size ',measured_dict)
    
    plt.plot(list(measured_dict.keys()), list(measured_dict.values()), 'o', color='black')
    plt.xlabel('sample_size')
    plt.ylabel('time')
    plt.savefig('measure1.png')
    
        


def compute_and_save_cov_and_cov_hats(sample_size,
                                      t_par_count,
                                      gamma_count,
                                      mean,
                                      sigma,
                                      lag,
                                      type_process,
                                      noise_type,
                                      diag_or_horiz):
    par_list = {"sample_size": sample_size,
                "t_par_count": t_par_count,
                "gamma_count": gamma_count,
                "mean": mean,
                "sigma": sigma,
                "lag": lag, "type_process": type_process,
                "noise_type": noise_type,
                "diag_or_horiz": diag_or_horiz}

    t_par_array = create_t_par_array(t_par_count=t_par_count)

    true_gamma_array = np.full(shape=t_par_count, fill_value=np.nan)

    gamma_hat_double_array = np.full(shape=(t_par_count, gamma_count),
                                     fill_value=np.nan)

    for t_index in range(t_par_count):
        true_gamma_array[t_index] = true_cov_ma1(t_par=t_par_array[t_index],
                                                 sigma=sigma,
                                                 lag=lag)
                                                 
    time_per_operation_array = []
    for index in range(gamma_count):
        start = time.time()
        if type_process == "MA1":
            if diag_or_horiz == "diag":
                sample = diagonal_sample_tvma1(
                    sample_size=sample_size,
                    mean=mean,
                    sigma=sigma,
                    noise_type=noise_type)
            elif diag_or_horiz == "horiz":
                horizontal = horizontal_sample_tvma1(
                    sample_size=sample_size,
                    t_par_count=t_par_count,
                    mean=mean,
                    sigma=sigma,
                    noise_type=noise_type)
        elif type_process == "scaled_noise":
            if diag_or_horiz == "diag":
                sample = diagonal_sample_scaled_noise(
                    sample_size=sample_size,
                    mean=mean,
                    sigma=sigma,
                    noise_type=noise_type)
            elif diag_or_horiz == "horiz":
                horizontal = horizontal_sample_scaled_noise(
                    sample_size=sample_size,
                    t_par_count=t_par_count,
                    mean=mean,
                    sigma=sigma,
                    noise_type=noise_type)
        for t_index in range(t_par_count):
            if diag_or_horiz == "horiz":
                sample = horizontal[t_index]
            gamma_hat_double_array[t_index, index] = cov_hat(
                sample=sample,
                t_par=t_par_array[t_index],
                lag=lag)
                
        time_dif = time.time() - start
        time_per_operation_array.append(time_dif)

        print("There are", gamma_count - (index + 1), "replications left")

    plot_double_array(x_array=t_par_array,
                      hat_double_array=gamma_hat_double_array,
                      true_array=true_gamma_array,
                      title='Autocovariance',
                      axis='column',
                      x_label='t par',
                      par_list=par_list)
                      
    return time_per_operation_array


if __name__ == '__main__':
    # compute_and_save_cov_and_cov_hats(sample_size=100,
    #                                   t_par_count=11,
    #                                   gamma_count=5,
    #                                   mean=0,
    #                                   sigma=2,
    #                                   lag=2,
    #                                   type_process='MA1',
    #                                   noise_type='bernoulli',
    #                                   diag_or_horiz='diag')
    benchmarking()
