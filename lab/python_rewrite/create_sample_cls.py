import numpy as np


class Sample:
    def __init__(self, size, t_par_count, mean, sigma, type_of_noise):
        self.size = size
        self.t_par_count = t_par_count
        self.mean = mean
        self.sigma = sigma
        self.type_of_noise = type_of_noise

    def create_noise(self, noise_size):
        if self.type_of_noise == "gaussian":
            return np.random.normal(self.mean, self.sigma, noise_size)
        elif self.type_of_noise == "bernoulli":
            classic_bernoulli = np.random.binomial(1, 1/2, noise_size)
            return self.sigma * ((2 * classic_bernoulli) - 1)
        else:
            raise ValueError("type_of_noise should be 'gaussian' or 'bernoulli'.")

    def create_t_par_array(self):
        if self.t_par_count <= 1:
            raise ValueError("t_par_count is 1 or smaller, whereas it should be 2 or greater")
        t_par_count_inner = self.t_par_count - 1
        t_par_array = np.arange(0, 1, 1/t_par_count_inner)
        return np.append(t_par_array, 1)

    def coef(self, t_par):
        return 2 - t_par

    def create_digonal_sample_tvma1(self):
        noise = self.create_noise(noise_size = self.size + 1)
        diagonal_sample_tvma1 = np.zeros(self.size)
        for i in range(1, self.size + 1):
            diagonal_sample_tvma1[i - 1] = self.coef(t_par = i / self.size) * noise[i - 1] + noise[i]
        return diagonal_sample_tvma1

    def create_horizontal_sample_tvma1(self):
        noise = self.create_noise(noise_size = self.size + 1)
        t_par_array = self.create_t_par_array()
        horizontal_sample_tvma1 = np.zeros((self.t_par_count, self.size))
        for i in range(self.t_par_count):
            for j in range(self.size):
                horizontal_sample_tvma1[i, j] = self.coef(t_par = t_par_array[i]) * noise[j] + noise[j + 1]
        return horizontal_sample_tvma1

    def create_digonal_sample_scaled_noise(self):
        noise = self.create_noise(noise_size = self.size + 1)
        diagonal_sample_scaled_noise = np.zeros(self.size)
        for i in range(1, self.size + 1):
            diagonal_sample_scaled_noise[i - 1] = self.coef(t_par = i / self.size) * noise[i - 1]
        return diagonal_sample_scaled_noise

    def create_horizontal_sample_scaled_noise(self):
        noise = self.create_noise(noise_size = self.size + 1)
        t_par_array = self.create_t_par_array()
        horizontal_sample_tvma1 = np.zeros((self.t_par_count, self.size))
        for i in range(self.t_par_count):
            for j in range(self.size):
                horizontal_sample_tvma1[i, j] = coef(t_par = t_par_array[i]) * noise[j]
        return horizontal_sample_tvma1
