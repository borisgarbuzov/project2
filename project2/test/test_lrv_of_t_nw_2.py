from src.lrv_hat_of_t_nw_2 import lrv_hat_of_t_nw_2
from timeit import default_timer as timer
import unittest
import numpy as np

class Test_lrv_hat_of_t_nw_2(unittest.TestCase):
    def test_lrv_hat_of_t_nw_2(self, 
                               sample = np.array([1, 2, 3]),
                               t_par_array = np.array([1, 2, 3])):
        print('\n\n===============================================================================')
        print('Testing "lrv_hat_of_t_nw_2"')
        start_time = timer()
        returned = lrv_hat_of_t_nw_2(sample, t_par_array)
        duration = timer() - start_time
        print('Test parameters:')
        print('sample = ', sample)
        print('t_par_array = ', t_par_array)
        print('returned = ', returned)
        print("\nDuration: {:g} secs".format(duration))
        print('End of test {}'.format('lrv_hat_of_t_nw_2'))
        print('===============================================================================\n')

if __name__ == '__main__':
    unittest.main()