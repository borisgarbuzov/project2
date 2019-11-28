import numpy as np


def create_noise(noise_size: int, mean: float, sigma: float,
                 noise_type: str) -> float:
    """
    create "gaussian" or "bernoulli" noise.

    :param noise_size: size of noise
    :param mean: mean
    :param sigma: sigma
    :param noise_type: type
    :return: float noise
    """
    if noise_type == "gaussian":
        return np.random.normal(mean, sigma, noise_size)
    elif noise_type == "bernoulli":
        classic_bernoulli = np.random.binomial(1, 1 / 2, noise_size)
        return sigma * ((2 * classic_bernoulli) - 1)
    else:
        raise ValueError("noise_type should be 'gaussian' or 'bernoulli'.")
