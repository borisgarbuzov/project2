import unittest
import numpy as np
from timeit import default_timer as timer
import src.precision


class Test_precision(unittest.TestCase):
    def test_mse_value_by_value_and_array(self, true_value=3, est_array=[1,2,3,4,5]):
        print('\n\n===============================================================================')
        print('Testing "mse_value_by_value_and_array"')
        start_time = timer()
        returned = src.precision.mse_value_by_value_and_array(true_value=true_value, est_array=est_array)
        print('Test parameters:')
        print('true_value = ', true_value)
        print('est_array = ', est_array)
        
        print('\nreturned = ', type(returned))
        # if isinstance(returned, list):
        #     print('returned shape = ', len(returned))
        # elif isinstance(returned, np.ndarray):
        #     print('returned shape = ', returned.shape)
        print('returned = ', returned)
            
        print("\nDuration: {:g} secs".format(timer() - start_time))
        print('End of test {}'.format('mse_value_by_value_and_array'))
        print('===============================================================================\n')
        
    def test_mse_value_by_array_and_array(self, true_array=[1,2,3,4,5], est_array=[6,7,8,9,10]):
        print('\n\n===============================================================================')
        print('Testing "mse_value_by_array_and_array"')
        start_time = timer()
        returned = src.precision.mse_value_by_array_and_array(true_array=true_array, est_array=est_array)
        print('Test parameters:')
        print('true_array = ', true_array)
        print('est_array = ', est_array)
        
        print('\nreturned = ', type(returned))
        # if isinstance(returned, list):
        #     print('returned shape = ', len(returned))
        # elif isinstance(returned, np.ndarray):
        #     print('returned shape = ', returned.shape)
        print('returned = ', returned)
            
        print("\nDuration: {:g} secs".format(timer() - start_time))
        print('End of test {}'.format('mse_value_by_array_and_array'))
        print('===============================================================================\n')
    
    def test_mse_array_by_array_and_double_array(self, true_array=[1,2,3], est_double_array=[[1,2,3],[4,5,6],[7,8,9]]):
        print('\n\n===============================================================================')
        print('Testing "mse_array_by_array_and_double_array"')
        start_time = timer()
        returned = src.precision.mse_array_by_array_and_double_array(true_array=true_array, est_double_array=est_double_array)
        print('Test parameters:')
        print('true_array = ', true_array)
        print('est_double_array = ', est_double_array)
        
        print('\nreturned = ', type(returned))
        if isinstance(returned, list):
            print('returned shape = ', len(returned))
        elif isinstance(returned, np.ndarray):
            print('returned shape = ', returned.shape)
        print('returned = ', returned)
            
        print("\nDuration: {:g} secs".format(timer() - start_time))
        print('End of test {}'.format('mse_array_by_array_and_double_array'))
        print('===============================================================================\n')

    def test_mean_array_by_double_array(self, double_array=[[1,2,3],[4,5,6],[7,8,9]]):
        print('\n\n===============================================================================')
        print('Testing "mean_array_by_double_array"')
        start_time = timer()
        returned = src.precision.mean_array_by_double_array(double_array=double_array)
        print('Test parameters:')
        print('double_array = ', double_array)
        
        print('\nreturned = ', type(returned))
        if isinstance(returned, list):
            print('returned shape = ', len(returned))
        elif isinstance(returned, np.ndarray):
            print('returned shape = ', returned.shape)
        print('returned = ', returned)
            
        print("\nDuration: {:g} secs".format(timer() - start_time))
        print('End of test {}'.format('mean_array_by_double_array'))
        print('===============================================================================\n')

    def test_variance_array_by_double_array(self, double_array=[[1,2,3],[4,5,6],[7,8,9]]):
        print('\n\n===============================================================================')
        print('Testing "variance_array_by_double_array"')
        start_time = timer()
        returned = src.precision.variance_array_by_double_array(double_array=double_array)
        print('Test parameters:')
        print('double_array = ', double_array)
    
        print('\nreturned = ', type(returned))
        if isinstance(returned, list):
            print('returned shape = ', len(returned))
        elif isinstance(returned, np.ndarray):
            print('returned shape = ', returned.shape)
        print('returned = ', returned)
            
        print("\nDuration: {:g} secs".format(timer() - start_time))
        print('End of test {}'.format('variance_array_by_double_array'))
        print('===============================================================================\n')

    def test_bias_array_by_array(self, true_array=[1,2,3], est_array=[4,5,6]):
        print('\n\n===============================================================================')
        print('Testing "bias_array_by_array"')
        start_time = timer()
        returned = src.precision.bias_array_by_array(true_array=true_array, est_array=est_array)
        print('Test parameters:')
        print('true_array = ', true_array)
        print('est_array = ', est_array)
        
        print('\nreturned = ', type(returned))
        if isinstance(returned, list):
            print('returned shape = ', len(returned))
        elif isinstance(returned, np.ndarray):
            print('returned shape = ', returned.shape)
        print('returned = ', returned)
            
        print("\nDuration: {:g} secs".format(timer() - start_time))
        print('End of test {}'.format('bias_array_by_array'))
        print('===============================================================================\n')

    def test_bias_array_by_double_array(self, true_array=[1,2,3], double_array=[[1,2,3],[4,5,6],[7,8,9]]):
        print('\n\n===============================================================================')
        print('Testing "bias_array_by_double_array"')
        start_time = timer()
        returned = src.precision.bias_array_by_double_array(true_array=true_array, double_array=double_array)
        print('Test parameters:')
        print('true_array = ', true_array)
        print('double_array = ', double_array)
        
        print('\nreturned = ', type(returned))
        if isinstance(returned, list):
            print('returned shape = ', len(returned))
        elif isinstance(returned, np.ndarray):
            print('returned shape = ', returned.shape)
        print('returned = ', returned)
            
        print("\nDuration: {:g} secs".format(timer() - start_time))
        print('End of test {}'.format('bias_array_by_double_array'))
        print('===============================================================================\n')

if __name__ == '__main__':
    unittest.main()
