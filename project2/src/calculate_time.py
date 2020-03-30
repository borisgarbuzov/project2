import pandas as pd
from timeit import default_timer as timer
from os.path import dirname
import datetime
import os

"""
The caller should measure duration and pass here along with parameters. 
This program will create CSV if it does not exist.
If this CSV exists, we will update it. 
Thus we will add a new line in the end. 
The format is:
func_name	time	duration, sec	parameters
In the parameters we have the dictionary.
"""
def calculate_time(name: str, duration: float, **parameters):

    # create directory for data if it doesn't exist
    now = datetime.datetime.now()
    parent_dir = dirname(dirname(__file__))
    data_folder = os.path.join(parent_dir, "data")
    if not os.path.exists(data_folder):
        os.mkdir(data_folder)

    out = {
        'func_name': name,
        'time': now.strftime("%m.%d.%y-%H:%M:%S"),
        'duration, sec': duration,
        'parameters': parameters
    }
    df = pd.DataFrame(out)

    # if csv do not exist, create new csv with header
    if not os.path.exists(data_folder + '/durations.csv'):
        df.to_csv(os.path.join(data_folder, 'durations.csv'), index=False)
    else:
        # if csv exist, create new csv without header
        with open('durations.csv', 'a'):
            df.to_csv(os.path.join(data_folder, 'durations.csv'), mode='a', index=False, header=False)

# Internal test
if __name__ == '__main__':
    start_time = timer()
    duration = timer() - start_time

    par = ''' 
        replication_count=10,sample_size_array=sample_size_array,
        mean=0,
        sigma=2,
        noise_type='bernoulli',
        is_data=False,
        fix_number_of_lags=300,
        sample_type='ma3'
    '''

    calculate_time(name='compute_and_save_var_cov_hat_native_matrix',
                   duration=duration,
                   parameters=par)
