from scipy.stats import norm


def custom_kernel(v, kernel_type='gaussian'):
    
    if kernel_type == 'triangular':
        kernel = triangular_kernel(v)
            
    if kernel_type == 'boxcar':
        kernel = boxcar_kernel
        
    if kernel_type == 'gaussian':
        kernel = gaussian_kernel(v)
    return kernel 


def triangular_kernel(v):
    if abs(v) <= 1:
        kernel = 1 - abs(v)
    else:
        kernel = 0
    return kernel 
            
def boxcar_kernel(v):
    if abs(v) <= 1:
        kernel = 1 / 2
    else:
        kernel = 0            
    return kernel 
            
def gaussian_kernel(v):
    kernel = norm.pdf(v)            
    return kernel 


