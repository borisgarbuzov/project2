import unittest
import numpy as np
from src.cov_hat import cov_hat  
from src.diagonal_sample_tvma1 import *
from timeit import default_timer as timer


class Test_cov_hat(unittest.TestCase):
    def test_cov_hat(self, t_par=0, lag=0):

        print('\n\n===============================================================================')
        print('Testing "cov_hat"')
        diagonal_sample = diagonal_sample_tvma1(sample_size=20,
                                            mean=0,
                                            sigma=2,
                                            noise_type='bernoulli') 
        start_time = timer()
        returned = cov_hat(sample = diagonal_sample, t_par=t_par, lag=lag)
        print('Test parameters:')
        print('sample = ', diagonal_sample)
        print('t_par = ', t_par)
        print('lag = ', lag)

        
        print('\nreturned = ', type(returned))
        if isinstance(returned, list):
            print('returned shape = ', len(returned))
        elif isinstance(returned, np.ndarray):
            print('returned shape = ', returned.shape)
        print('returned = ', returned)
        
            
        print("\nDuration: {:g} secs".format(timer() - start_time))
        print('End of test {}'.format('cov_hat'))
        print('===============================================================================\n')


if __name__ == '__main__':
    unittest.main()
