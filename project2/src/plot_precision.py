from src.precision_of_t import precision_of_t
import matplotlib.pyplot as plt

precision_arrays = precision_of_t([1,2,3], est_double_array=[[1,2,3],[4,5,6],[7,8,9]])
mse = precision_arrays.get('mse')
bias = precision_arrays.get('bias')
mean = precision_arrays.get('mean')
variance = precision_arrays.get('variance')

plt.plot(bias)
plt.savefig(fname='1', dpi=300, bbox_inches='tight')
plt.close()

plt.plot(mse)
plt.savefig(fname='2', dpi=300, bbox_inches='tight')
plt.close()

plt.plot(mean)
plt.savefig(fname='3', dpi=300, bbox_inches='tight')
plt.close()

plt.plot(variance)
plt.savefig(fname='4', dpi=300, bbox_inches='tight')
plt.close()