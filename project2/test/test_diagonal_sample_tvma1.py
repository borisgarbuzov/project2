from src.diagonal_sample_tvma1 import diagonal_sample_tvma1
from timeit import default_timer as timer
import numpy as np
import unittest


class Test_diagonal_sample_tvma1(unittest.TestCase):
    def test_diagonal_sample_tvma1(self, sample_size=8, mean=5, sigma=0.12,
                                   noise_type="gaussian"):

        print('\n\n===============================================================================')
        print('Testing "diagonal_sample_tvma1"')
        start_time = timer()
        

        returned = diagonal_sample_tvma1(sample_size=sample_size, mean=mean, sigma=sigma, noise_type=noise_type)
        print('Test parameters:')
        print('sample_size = ', sample_size)
        print('mean = ', mean)
        print('sigma = ', sigma)
        print('noise_type = ', noise_type)

        print('\nreturned = ', type(returned))
        if isinstance(returned, list):
            print('returned shape = ', len(returned))
        elif isinstance(returned, np.ndarray):
            print('returned shape = ', returned.shape)
        print('returned = ', returned)
            
        print("\nDuration: {:g} secs".format(timer() - start_time))
        print('End of test {}'.format('diagonal_sample_tvma1'))
        print('===============================================================================\n')


if __name__ == '__main__':
    unittest.main()
