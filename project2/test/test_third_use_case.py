import unittest
from src.third_use_case import third_use_case
from timeit import default_timer as timer


class Test_third_use_case(unittest.TestCase):
    def test_third_use_case(self, sample_size_min=1000, sample_size_max=10000, sample_size_by=1000, replications=5, sigma=2, model='MA1',
                   coef=1):

        print('\n\n===============================================================================')
        print('Testing "third_use_case"')
        
        start_time = timer()
        third_use_case(sample_size_min=sample_size_min, 
                     sample_size_max=sample_size_max, 
                     sample_size_by=sample_size_by, 
                     replications=replications, 
                     sigma=sigma, 
                     model=model,
                     coef=coef)
        print('Test parameters:')
        print('sample_size_min = ', sample_size_min)
        print('sample_size_max = ', sample_size_max)
        print('sample_size_by = ', sample_size_by)
        print('replications = ', replications)
        print('sigma = ', sigma)
        print('model = ', model)
        print('coef = ', coef)

        print("\nDuration: {:g} secs".format(timer() - start_time))
        print('End of test {}'.format('third_use_case'))
        print('===============================================================================\n')


if __name__ == '__main__':
    unittest.main()
