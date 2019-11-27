from src.precision import compute_precision
from timeit import default_timer as timer
import numpy as np
import unittest


class Test_precision(unittest.TestCase):
    def test_compute_precision(self, true_array=[1,2,3,4,5,6],
                               hat_double_array=[0.975,2.075,3.025,4.147,5.066,6.104]):

        print('\n\n===============================================================================')
        print('Testing "test_compute_precision"')
        start_time = timer()
        returned = compute_precision(true_array=true_array, hat_double_array=hat_double_array)
        print('Test parameters:')
        print('true_array = ', true_array)
        print('hat_double_array = ', hat_double_array)
        
        print('\nreturned = ', type(returned))
        if isinstance(returned, list):
            print('returned shape = ', len(returned))
        elif isinstance(returned, np.ndarray):
            print('returned shape = ', returned.shape)
        print('returned = ', returned)
        
            
        print("\nDuration: {:g} secs".format(timer() - start_time))
        print('End of test {}'.format('test_compute_precision'))
        print('===============================================================================\n')


if __name__ == '__main__':
    unittest.main()
