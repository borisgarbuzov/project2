import numpy as np


def create_noise(noise_size: int, mean: float, sigma: float, type_of_noise: str) -> float:
    """
    create "gaussian" or "bernoulli" noise.

    :param noise_size: size of noise
    :param mean: mean
    :param sigma: sigma
    :param type_of_noise: type
    :return: float noise
    """
    if type_of_noise == "gaussian":
        return np.random.normal(mean, sigma, noise_size)
    elif type_of_noise == "bernoulli":
        classic_bernoulli = np.random.binomial(1, 1 / 2, noise_size)
        return sigma * ((2 * classic_bernoulli) - 1)
    else:
        raise ValueError("type_of_noise should be 'gaussian' or 'bernoulli'.")
