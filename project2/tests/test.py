import unittest
from old_code import compute_and_save_lrv_hat
from timeit import default_timer as timer


class TestSum(unittest.TestCase):
    def test_compute_and_save_lrv_hat(self,
                                      sample_size_from=1000,
                                      sample_size_to=3000,
                                      sample_size_step=1000,
                                      replication_count=100,
                                      method1='threshold',
                                      method2='newey west'):

        print('\n\n===============================================================================')
        print('Testing "compute_and_save_lrv_hat"')
        start_time = timer()
        compute_and_save_lrv_hat(sample_size_from=sample_size_from,
                                 sample_size_to=sample_size_to,
                                 sample_size_step=sample_size_step,
                                 replication_count=replication_count,
                                 method1=method1,
                                 method2=method2)
        print('Test parameters:')
        print('sample_size_from = ', sample_size_from)
        print('sample_size_to = ', sample_size_to)
        print('sample_size_step = ', sample_size_step)
        print('replication_count = ', replication_count)
        print('method1 = ', method1)
        print('method2 = ', method2)
        print("\nDuration: {:g} secs".format(timer() - start_time))
        print('End of test {}'.format('test_compute_and_save_lrv_hat'))
        print('===============================================================================\n')


if __name__ == '__main__':
    unittest.main()
