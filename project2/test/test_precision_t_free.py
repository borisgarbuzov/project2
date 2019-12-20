import unittest
import numpy as np
from timeit import default_timer as timer
import src.precision_t_free

class Test_run_precision_t_free(unittest.TestCase):
    def test_run_mean_t_free(self, est_array=np.array([1,2,3])):
        print('\n\n===============================================================================')
        print('RUN testing "mean_t_free"')
        start_time = timer()
        returned = src.precision_t_free.mean_t_free(est_array)
        duration = timer() - start_time
        print('Test parameters:')
        print('est_array = ', est_array)
        
        print('\nreturned = ', type(returned))
        print('returned = ', returned)
            
        print("\nDuration: {:g} secs".format(duration))
        print('End of RUN test {}'.format('mean_t_free'))
        print('===============================================================================\n')
    
    def test_run_variance_t_free(self, est_array=np.array([1,2,3])):
        print('\n\n===============================================================================')
        print('RUN testing "variance_t_free"')
        start_time = timer()
        returned = src.precision_t_free.variance_t_free(est_array)
        duration = timer() - start_time
        print('Test parameters:')
        print('est_array = ', est_array)

        print('\nreturned = ', type(returned))
        print('returned = ', returned)
            
        print("\nDuration: {:g} secs".format(duration))
        print('End of RUN test {}'.format('variance_t_free'))
        print('===============================================================================\n')
        
    def test_run_mse_t_free(self, est_array=np.array([1,2,3]), true_array=np.array([3,4,5])):
        print('\n\n===============================================================================')
        print('RUN testing "mse_t_free"')
        start_time = timer()
        returned = src.precision_t_free.mse_t_free(true_array, est_array)
        duration = timer() - start_time
        print('Test parameters:')
        print('est_array = ', est_array)
        print('true_array = ', true_array)

        print('\nreturned = ', type(returned))
        print('returned = ', returned)
            
        print("\nDuration: {:g} secs".format(duration))
        print('End of RUN test {}'.format('mse_t_free'))
        print('===============================================================================\n')

    def test_bias_t_free(self, est_array=np.array([1,2,3]), true_value=5.0):
        print('\n\n===============================================================================')
        print('RUN testing "bias_t_free"')
        start_time = timer()
        returned = src.precision_t_free.bias_t_free(true_value, est_array)
        duration = timer() - start_time
        print('Test parameters:')
        print('est_array = ', est_array)
        print('true_value = ', true_value)

        print('\nreturned = ', type(returned))
        print('returned = ', returned)
            
        print("\nDuration: {:g} secs".format(duration))
        print('End of RUN test {}'.format('bias_t_free'))
        print('===============================================================================\n')
    
if __name__ == '__main__':
    unittest.main()
