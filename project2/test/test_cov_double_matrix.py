import unittest
import numpy as np
from src.cov_double_matrix import cov_double_matrix  
from src.diagonal_sample_tvma1 import diagonal_sample_tvma1
from timeit import default_timer as timer


class Test_cov_double_array(unittest.TestCase):
    def test_cov_double_matrix(self, t_par_count=11, 
                                      sample_size=20,
                                      mean=0,
                                      sigma=2,
                                      noise_type='bernoulli'):

        print('\n\n===============================================================================')
        print('Testing "cov_double_array"')
        diagonal_sample = diagonal_sample_tvma1(sample_size=sample_size,
                                      mean=mean,
                                      sigma=sigma,
                                      noise_type=noise_type)
        start_time = timer()
        returned = cov_double_matrix(sample=diagonal_sample,
                                            t_par_count=t_par_count)
        print('Test parameters:')
        print('sample_size = ', diagonal_sample.shape)
        print('t_par_count = ', t_par_count)


        print('\nreturned = ', type(returned))
        if isinstance(returned, list):
            print('returned shape = ', len(returned))
        elif isinstance(returned, np.ndarray):
            print('returned shape = ', returned.shape)
        print('returned = ', returned)

        print("\nDuration: {:g} secs".format(timer() - start_time))
        print('End of test {}'.format('cov_double_array'))
        print('===============================================================================\n')


if __name__ == '__main__':
    unittest.main()
