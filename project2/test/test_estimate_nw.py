from src.lrv_hat_of_t_nw import lrv_hat_of_t_nw
from src.cov_double_array_of_t import cov_double_array_of_t
from src.diagonal_sample_tvma1 import diagonal_sample_tvma1
from timeit import default_timer as timer
import numpy as np
import unittest


class Test_estimate_nw(unittest.TestCase):
    def test_estimate_nw(self, t_par_count=11,
                         sample_size=20,
                         mean=0,
                         sigma=2,
                         noise_type='bernoulli'):

        print('\n\n===============================================================================')
        print('Testing "estimate_nw"')
        diagonal_sample = diagonal_sample_tvma1(sample_size=sample_size,
                                                mean=mean,
                                                sigma=sigma,
                                                noise_type=noise_type)
                                      
        cov_double_aray = cov_double_array_of_t(sample=diagonal_sample,
                                                t_par_count=t_par_count)
        start_time = timer()
        returned = lrv_hat_of_t_nw(cov_double_aray=cov_double_aray)
        print('Test parameters:')
        print('cov_double_aray_size = ', cov_double_aray.shape)

        print('\nreturned = ', type(returned))
        if isinstance(returned, list):
            print('returned shape = ', len(returned))
        elif isinstance(returned, np.ndarray):
            print('returned shape = ', returned.shape)
        print('returned = ', returned)

        print("\nDuration: {:g} secs".format(timer() - start_time))
        print('End of test {}'.format('estimate_nw'))
        print('===============================================================================\n')


if __name__ == '__main__':
    unittest.main()
