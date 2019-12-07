from timeit import default_timer as timer
from src.treshold_indicator import treshold_indicator
import unittest

class Test_treshold_indicator(unittest.TestCase):
    def test_treshold_indicator(self,
                                sample_size = 10,
                                cov_hat = 0,
                                lag = 0):
        print('\n\n===============================================================================')
        print('Testing "treshold_indicator"')
        
        start_time = timer()
        returned = treshold_indicator(sample_size, cov_hat, lag)
        duration = timer() - start_time
        expected = 1
        self.assertEqual(returned, expected)
        
        print('Test parameters:')
        print('sample_size =', sample_size)
        print('cov_hat =', cov_hat)
        print('lag = ', lag)
        print('expected = ', expected)
        print('returned = ', returned)
        print("\nDuration: {:g} secs".format(duration))
        print('End of test {}'.format('treshold_indicator'))
        print('===============================================================================\n')

if __name__ == '__main__':
    unittest.main()