from sample import Sample
import estimators
import generators
import numpy as np

if __name__ == '__main__':
    generate_meta={}
    replecations = 5
    sample_sizes = [2,3,5,7,9]
    raw_replecation_meta = range(1, replecations+1)
    column_sample_sizes_meta = sample_sizes
    shape=(replecations, len(sample_sizes))
    newey_west_meta={}
    threshold_meta={}
    
    all_newey_west_array = np.empty(shape)
    all_threshold_array = np.empty(shape)
    for sample_size in range(0,len(sample_sizes)):
        for replecation in range(0,replecations):
            new_sample = generators.generate1(sample_size = sample_size)
            new_newey_west = estimators.newey_west(new_sample)
            new_threshold = estimators.threshold(new_sample)
            all_newey_west_array[sample_size][replecation] = new_newey_west
            all_threshold_array[sample_size][replecation] = new_threshold
            
    printer.printer(all_newey_west_array, generate_meta, raw_replecation_meta, column_sample_sizes_meta, newey_west_meta)
        
    
    
    


    



