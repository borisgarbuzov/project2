import unittest
import numpy as np
from timeit import default_timer as timer
import src.precision


class Test_precision_run(unittest.TestCase):
    def test_run_mse_value_by_value_and_array(self, true_value=3, est_array=[1,2,3,4,5]):
        print('\n\n===============================================================================')
        print('RUN testing "mse_value_by_value_and_array"')
        start_time = timer()
        returned = src.precision.mse_value_by_value_and_array(true_value=true_value, est_array=est_array)
        duration = timer() - start_time
        print('Test parameters:')
        print('true_value = ', true_value)
        print('est_array = ', est_array)
        
        print('\nreturned = ', type(returned))
        print('returned = ', returned)
            
        print("\nDuration: {:g} secs".format(duration))
        print('End of RUN test {}'.format('mse_value_by_value_and_array'))
        print('===============================================================================\n')
        
    def test_run_mse_value_by_array_and_array(self, true_array=[1,2,3,4,5], est_array=[6,7,8,9,10]):
        print('\n\n===============================================================================')
        print('RUN testing "mse_value_by_array_and_array"')
        start_time = timer()
        returned = src.precision.mse_value_by_array_and_array(true_array=true_array, est_array=est_array)
        duration = timer() - start_time
        print('Test parameters:')
        print('true_array = ', true_array)
        print('est_array = ', est_array)
        
        print('\nreturned = ', type(returned))
        print('returned = ', returned)
            
        print("\nDuration: {:g} secs".format(duration))
        print('End of RUN test {}'.format('mse_value_by_array_and_array'))
        print('===============================================================================\n')
    
    def test_run_mse_array_by_array_and_double_array(self, true_array=[1,2,3], est_double_array=[[1,2,3],[4,5,6],[7,8,9]]):
        print('\n\n===============================================================================')
        print('RUN testing "mse_array_by_array_and_double_array"')
        start_time = timer()
        returned = src.precision.mse_array_by_array_and_double_array(true_array=true_array, est_double_array=est_double_array)
        duration = timer() - start_time
        print('Test parameters:')
        print('true_array = ', true_array)
        print('est_double_array = ', est_double_array)
        
        print('\nreturned = ', type(returned))
        if isinstance(returned, list):
            print('returned shape = ', len(returned))
        elif isinstance(returned, np.ndarray):
            print('returned shape = ', returned.shape)
        print('returned = ', returned)
            
        print("\nDuration: {:g} secs".format(duration))
        print('End of RUN test {}'.format('mse_array_by_array_and_double_array'))
        print('===============================================================================\n')

    def test_run_mean_array_by_double_array(self, est_double_array=[[1,2,3],[4,5,6],[7,8,9]]):
        print('\n\n===============================================================================')
        print('RUN testing "mean_array_by_double_array"')
        start_time = timer()
        returned = src.precision.mean_array_by_double_array(double_array=est_double_array)
        duration = timer() - start_time
        print('Test parameters:')
        print('double_array = ', est_double_array)
        
        print('\nreturned = ', type(returned))
        if isinstance(returned, list):
            print('returned shape = ', len(returned))
        elif isinstance(returned, np.ndarray):
            print('returned shape = ', returned.shape)
        print('returned = ', returned)
            
        print("\nDuration: {:g} secs".format(duration))
        print('End of RUN test {}'.format('mean_array_by_double_array'))
        print('===============================================================================\n')

    def test_run_variance_array_by_double_array(self, est_double_array=[[1,2,3],[4,5,6],[7,8,9]]):
        print('\n\n===============================================================================')
        print('RUN testing "variance_array_by_double_array"')
        start_time = timer()
        returned = src.precision.variance_array_by_double_array(double_array=est_double_array)
        duration = timer() - start_time
        print('Test parameters:')
        print('double_array = ', est_double_array)
    
        print('\nreturned = ', type(returned))
        if isinstance(returned, list):
            print('returned shape = ', len(returned))
        elif isinstance(returned, np.ndarray):
            print('returned shape = ', returned.shape)
        print('returned = ', returned)
            
        print("\nDuration: {:g} secs".format(duration))
        print('End of RUN test {}'.format('variance_array_by_double_array'))
        print('===============================================================================\n')

    def test_run_bias_array_by_double_array(self, true_array=[1,2,3], est_double_array=[[1,2,3],[4,5,6],[7,8,9]]):
        print('\n\n===============================================================================')
        print('RUN testing "bias_array_by_double_array"')
        start_time = timer()
        returned = src.precision.bias_array_by_double_array(true_array=true_array, double_array=est_double_array)
        duration = timer() - start_time
        print('Test parameters:')
        print('true_array = ', true_array)
        print('double_array = ', est_double_array)
        
        print('\nreturned = ', type(returned))
        if isinstance(returned, list):
            print('returned shape = ', len(returned))
        elif isinstance(returned, np.ndarray):
            print('returned shape = ', returned.shape)
        print('returned = ', returned)
            
        print("\nDuration: {:g} secs".format(duration))
        print('End of RUN test {}'.format('bias_array_by_double_array'))
        print('===============================================================================\n')


class Test_precision_correct(unittest.TestCase):
    def test_mse_value_by_value_and_array(self, true_value=3, est_array=[1, 2, 3, 4, 5],
                                          true_returned=2.0):
        print('\n\n===============================================================================')
        print('Testing "mse_value_by_value_and_array"')
        start_time = timer()
        returned = src.precision.mse_value_by_value_and_array(true_value=true_value, est_array=est_array)
        duration = timer() - start_time

        self.assertAlmostEqual(returned, true_returned, places=3, msg='Should be {}'.format(true_returned))

        print('Test parameters:')
        print('true_value = ', true_value)
        print('est_array = ', est_array)

        print('\nreturned = ', type(returned))
        print('returned = ', returned)
        print("\nDuration: {:g} secs".format(duration))
        print('End of test {}'.format('mse_value_by_value_and_array'))
        print('===============================================================================\n')

    def test_mse_value_by_array_and_array(self, true_array=[1, 2, 3, 4, 5], est_array=[6, 7, 8, 9, 10],
                                          true_returned=25.0):
        print('\n\n===============================================================================')
        print('Testing "mse_value_by_array_and_array"')
        start_time = timer()
        returned = src.precision.mse_value_by_array_and_array(true_value=true_array, est_array=est_array)
        duration = timer() - start_time

        self.assertAlmostEqual(returned, true_returned, places=3, msg='Should be {}'.format(true_returned))

        print('Test parameters:')
        print('true_value = ', true_array)
        print('est_array = ', est_array)

        print('\nreturned = ', type(returned))
        print('returned = ', returned)
        print("\nDuration: {:g} secs".format(duration))
        print('End of test {}'.format('mse_value_by_array_and_array'))
        print('===============================================================================\n')

    def test_mse_array_by_array_and_double_array_1(self, true_array=[1,2,3], est_double_array=[[1,2,3],[4,5,6],[7,8,9]],
                                                 true_returned=np.array([15., 15., 15., 15.])):
        print('\n\n===============================================================================')
        print('Testing "mse_array_by_array_and_double_array_1"')
        start_time = timer()
        returned = src.precision.mse_array_by_array_and_double_array(true_value=true_array, est_array=est_double_array)
        duration = timer() - start_time

        self.assertListEqual(list(returned), list(true_returned), msg='Should be {}'.format(true_returned))

        print('Test parameters:')
        print('true_value = ', true_array)
        print('est_array = ', est_double_array)

        print('\nreturned = ', type(returned))
        print('returned = ', returned)
        print("\nDuration: {:g} secs".format(duration))
        print('End of test {}'.format('mse_array_by_array_and_double_array_1'))
        print('===============================================================================\n')

    def test_mse_array_by_array_and_double_array_2(self, true_array=[9, 9, 9, 9],
                                                   est_double_array=[[1, 1, 1, 1], [5, 5, 5, 5], [7, 7, 7, 7]],
                                                   true_returned=np.array([28., 28., 28., 28.])):
        print('\n\n===============================================================================')
        print('Testing "mse_array_by_array_and_double_array_2"')
        start_time = timer()
        returned = src.precision.mse_array_by_array_and_double_array(true_value=true_array, est_array=est_double_array)
        duration = timer() - start_time

        self.assertListEqual(list(returned), list(true_returned), msg='Should be {}'.format(true_returned))

        print('Test parameters:')
        print('true_value = ', true_array)
        print('est_array = ', est_double_array)

        print('\nreturned = ', type(returned))
        print('returned = ', returned)
        print("\nDuration: {:g} secs".format(duration))
        print('End of test {}'.format('mse_array_by_array_and_double_array_2'))
        print('===============================================================================\n')


if __name__ == '__main__':
    unittest.main()
