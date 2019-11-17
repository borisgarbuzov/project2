from scipy.stats import norm


def gamma_hat(sample, t_par, lag, b_cov):
    sample_size = len(sample)
    partial_sum = 0
    for term_index in range(1, (sample_size - lag) + 1):
        term = (sample[term_index - 1] * sample[
            (term_index - 1) + lag] *
                norm.pdf(((
                                  term_index / sample_size - t_par) / b_cov) /
                         0.1)) / 0.1
        partial_sum += term

    cov_hat = partial_sum / (sample_size * b_cov)
    return cov_hat
