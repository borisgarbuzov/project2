from src.diagonal_sample_tvar1 import diagonal_sample_tvar1
from timeit import default_timer as timer
import numpy as np
import unittest


class Test_diagonal_sample_tvar1(unittest.TestCase):
    def test_diagonal_sample_tvar1(self, sample_size=3, mean=0, sigma=1,
                                   noise_type=["bernoulli", "gaussian"]):

        print('\n\n===============================================================================')
        print('Testing "diagonal_sample_tvar1"')
        start_time = timer()

        for each in noise_type:
            returned = diagonal_sample_tvar1(sample_size=sample_size, mean=mean, sigma=sigma, noise_type=each)
            print('Test parameters:')
            print('sample_size = ', sample_size)
            print('mean = ', mean)
            print('sigma = ', sigma)
            print('noise_type = ', each)

            print('\nreturned = ', type(returned))
            if isinstance(returned, list):
                print('returned shape = ', len(returned))
            elif isinstance(returned, np.ndarray):
                print('returned shape = ', returned.shape)
            print('returned = ', returned)

            print("\nDuration: {:g} secs".format(timer() - start_time))
            print('End of test {}'.format('diagonal_sample_tvar1'))
            print('===============================================================================\n')


if __name__ == '__main__':
    unittest.main()
