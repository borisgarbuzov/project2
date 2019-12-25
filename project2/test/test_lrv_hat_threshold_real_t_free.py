from src.lrv_hat_threshold_t_free import lrv_hat_threshold_t_free
from src.diagonal_sample_tvma1 import diagonal_sample_tvma1
from src.cov_column_t_free import cov_column_t_free
from src.threshold_max_lag import threshold_max_lag
from timeit import default_timer as timer
import numpy as np
import unittest


class Test_lrv_hat_threshold_real_t_free(unittest.TestCase):
    def test_lrv_hat_threshold_real_t_free(self,
                                           sample_size=100):
        print('\n\n===============================================================================')
        print('RUN testing "lrv_hat_threshold_real_t_free"')

        start_time = timer()
        sample = diagonal_sample_tvma1(sample_size=sample_size,
                                       mean=0,
                                       sigma=2,
                                       noise_type="gaussian")
        max_lag = threshold_max_lag(sample_size=sample_size)
        cov_hat_column = cov_column_t_free(sample=sample, max_lag=max_lag)
        
        returned = lrv_hat_threshold_t_free(cov_hat_column=cov_hat_column,
                                            sample_size=sample_size)
        duration = timer() - start_time
        print('Test parameters:')
        print('returned = ', returned)
        print("\nDuration: {:g} secs".format(duration))
        print('End of RUN test {}'.format('lrv_hat_threshold_real_t_free'))
        print('===============================================================================\n')


if __name__ == '__main__':
    unittest.main()
