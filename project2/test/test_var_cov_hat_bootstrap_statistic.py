from src.var_cov_hat_bootstrap_statistic import var_cov_hat_bootstrap_statistic
from timeit import default_timer as timer
import numpy as np
import unittest


class Test_var_cov_hat_bootstrap_statistic(unittest.TestCase):
    def test_var_cov_hat_bootstrap_statistic(self,
                                             paired_product_array = np.array([1., 4., 9., 16., 25.]),
                                             block_sum_array = np.array([5, 13, 25, 41]),
                                             sample_size = 5,
                                             g_array=np.array([0, 1, 0, -1]), #if g_array same in original var_cov...
                                             true_return = -8.854377448471462
                                             ):
        print('\n\n===============================================================================')
        print('Testing "var_cov_hat_bootstrap_statistic"')

        start_time = timer()
        s_value = var_cov_hat_bootstrap_statistic(paired_product_array, block_sum_array, sample_size, g_array)
        self.assertEqual(s_value, true_return)
        end_time = timer() - start_time

        print('Test parameters:')
        print('paired_product_array =', paired_product_array)
        print('block_sum_array =', block_sum_array)
        print('sample_size =', sample_size)
        print('g_array =', g_array)
        print('true_return =', true_return)
        print('\nreturned = ', type(s_value))
        print('s_value = ', s_value)
        
        print("\nDuration: {:g} secs".format(end_time))
        print('End of test {}'.format('var_cov_hat_bootstrap_statistic'))
        print('===============================================================================\n')


if __name__ == '__main__':
    unittest.main()