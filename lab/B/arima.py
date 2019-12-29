import statsmodels.api as sm
import numpy as np


np.random.seed(12345)
arparams = np.array([.75])
maparams = np.array([.0, .0])
ar = np.r_[1, -arparams] # add zero-lag and negate
ma = np.r_[1, maparams] # add zero-lag
y = sm.tsa.arma_generate_sample(ar, ma, 2500)
model = sm.tsa.ARMA(y, (2, 2)).fit(trend='nc', disp=0)
print(model.params)
