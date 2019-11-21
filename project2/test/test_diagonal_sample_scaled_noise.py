import unittest
import numpy as np
from src.diagonal_sample_scaled_noise import diagonal_sample_scaled_noise  
from timeit import default_timer as timer


class Test_diagonal_sample_scaled_noise(unittest.TestCase):
    def test_diagonal_sample_scaled_noise(self, sample_size=8, mean=5, sigma=0.12, noise_type= ["bernoulli","gaussian"]):

        print('\n\n===============================================================================')
        print('Testing "diagonal_sample_scaled_noise"')
        start_time = timer()
        
        for each in noise_type:
            
            returned = diagonal_sample_scaled_noise(sample_size=sample_size, mean=mean, sigma=sigma, noise_type=each)
            print('Test parameters:')
            print('sample_size = ', sample_size)
            print('mean = ', mean)
            print('sigma = ', sigma)
            print('type_of_noise = ', each)
            
            
            print('\nreturned = ', type(returned))
            if isinstance(returned, list):
                print('returned shape = ', len(returned))
            elif isinstance(returned, np.ndarray):
                print('returned shape = ', returned.shape)
            print('returned = ', returned)
            
                
            print("\nDuration: {:g} secs".format(timer() - start_time))
            print('End of test {}'.format('diagonal_sample_scaled_noise'))
            print('===============================================================================\n')


if __name__ == '__main__':
    unittest.main()
