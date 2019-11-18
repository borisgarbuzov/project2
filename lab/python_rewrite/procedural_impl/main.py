from create_diagonal_sample_tvma1 import *
from compute_cov_double_array import *
sample = create_diagonal_sample_tvma1(sample_size=100, mean=0, sigma=2, type_of_noise='bernoulli')
cov_matrix = compute_cov_double_array(sample=sample, t_par_count=11)
print(cov_matrix)