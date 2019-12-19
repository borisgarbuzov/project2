import unittest
import numpy as np
from timeit import default_timer as timer
from src.bias_t_free import bias_t_free

class Test_bias_t_free(unittest.TestCase):
    def test_bias_t_free(self, true_value=5, est_array=np.array([1, 2, 3]), expected=-3.0):
        print('\n\n===============================================================================')
        print('Testing "bias_t_free"')
        start_time = timer()
        returned = bias_t_free(true_value=true_value, est_array=est_array)
        duration = timer() - start_time
        self.assertEqual(returned, expected)
        print('Test parameters:')
        print('true_value = ', true_value)
        print('est_array = ', est_array)
        print('\nreturned = ', returned)
        print('expected = ', expected)
        print("\nDuration: {:g} secs".format(duration))
        print('End of RUN test {}'.format('bias_t_free'))
        print('===============================================================================\n')
        
if __name__ == '__main__':
    unittest.main()
