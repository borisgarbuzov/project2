from src.lrv_hat_threshold_t_free import lrv_hat_threshold_t_free
from timeit import default_timer as timer
import numpy as np
import unittest


class Test_lrv_hat_threshold_t_free(unittest.TestCase):
    def test_lrv_hat_threshold_t_free(self):
        print('\n\n===============================================================================')
        print('RUN testing "lrv_hat_threshold_t_free"')

        start_time = timer()
        small = 0.1
        big = 1000
        sample_size = 10
        cov_hat_column = np.array([small, big])
        returned = lrv_hat_threshold_t_free(cov_hat_column = cov_hat_column,
                                            sample_size = sample_size)
        duration = timer() - start_time
        expected = 2*big
        print('Test parameters:')
        print('cov_hat_column = ', cov_hat_column)
        print('sample_size = ', sample_size)
        print('expected = ', expected)
        print('returned = ', returned)
        print("\nDuration: {:g} secs".format(duration))
        print('End of RUN test {}'.format('lrv_hat_threshold_t_free'))
        print('===============================================================================\n')


if __name__ == '__main__':
    unittest.main()
