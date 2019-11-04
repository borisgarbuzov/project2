import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from create_sample_cls import Sample


class GammaSmall(Sample):
    def __init__(self, size, t_par_count, gamma_count, mean, sigma, lag,
        type_process, type_of_noise, diag_or_horiz):
        self.size = size
        self.t_par_count = t_par_count
        self.gamma_count = gamma_count
        self.mean = mean
        self.sigma = sigma
        self.lag = lag
        self.type_process = type_process
        self.type_of_noise = type_of_noise
        self.diag_or_horiz = diag_or_horiz
        super().__init__(size = size, t_par_count = t_par_count, mean = mean, sigma = sigma, type_of_noise = type_of_noise)
        self.t_par_array = super().create_t_par_array()
        self.b_cov = 1 *self.size ** (-1/4)

    def true_gamma(self, t):
        if self.type_process == "MA1":
            if self.lag == 0:
                gamma = ((self.sigma ** 2) * (1 + (super.coef(t) ** 2)))
            elif self.lag == 1:
                gamma = (super.coef(t) * (self.sigma ** 2))
            else:
                gamma = 0
        elif self.type_process == "scaled_noise":
            if self.lag == 0:
                gamma = super.coef(t) ** 2 * self.sigma ** 2
            elif self.lag != 0:
                gamma = 0
        else:
            raise ValueError("type_process should be 'MA1' or 'scaled_noise'")
        return gamma

    def gamma_hat(self, sample, t):
        partial_sum = 0
        for term_index in range(1, (self.size - self.lag) + 1):
            term = (sample[term_index - 1] * sample[(term_index - 1) + self.lag] *
                norm.pdf(((term_index / self.size - t) / self.b_cov) / 0.1)) / 0.1
            partial_sum += term

        cov_hat = partial_sum / (self.size * self.b_cov)
        return cov_hat

    def plot(self, double_array, gamma_array):
        plt.style.use('ggplot')
        for i in range(self.gamma_count):
            plt.plot(self.t_par_array, double_array[:, i])
        plt.plot(self.t_par_array, gamma_array)
        plt.xlabel('t_par')
        plt.ylabel('value')
        plt.title('Autocovariance')
        plt.savefig('gamma_try.png')

    def compute(self):
        true_gamma_array = np.zeros(self.t_par_count)
        gamma_hat_double_array = np.zeros((self.t_par_count, self.gamma_count))

        # compute true gamma
        for t in range(self.t_par_count):
            true_gamma_array[t] = self.true_gamma(t = self.t_par_array[t])

        for index in range(self.gamma_count):
            # create sample
            if self.type_process == "MA1":
                if self.diag_or_horiz == "diag":
                    sample = super().create_digonal_sample_tvma1()
                elif self.diag_or_horiz == "horiz":
                    horizontal = super().create_horizontal_sample_tvma1()
            elif self.type_process == "scaled_noise":
                if self.diag_or_horiz == "diag":
                    sample = super().create_digonal_sample_scaled_noise()
                elif self.diag_or_horiz == "horiz":
                    horizontal = super().create_horizontal_sample_scaled_noise()
            for t_index in range(self.t_par_count):
                if self.diag_or_horiz == "horiz":
                    sample = horizontal[t_index]
                gamma_hat_double_array[t_index, index] = self.gamma_hat(sample = sample, t = self.t_par_array[t_index])

        self.plot(gamma_hat_double_array, true_gamma_array)


obj = GammaSmall(size = 1000, t_par_count = 11, gamma_count = 5, mean = 0,
    sigma = 2, lag = 2, type_process = "MA1", type_of_noise = "gaussian",
    diag_or_horiz = "horiz")
obj.compute()
