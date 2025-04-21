# StochasticProcesses/Levy.py
import numpy as np

def simulate_levy_process(T=1.0, N=1000, gamma=0.1, sigma=0.2,
                          jump_intensity=5, jump_scale=0.5, seed=None):
    """
    Simulate a Lévy process with drift, Brownian motion, and jumps.

    Parameters:
        T (float): Total time
        N (int): Number of steps
        gamma (float): Drift coefficient
        sigma (float): Volatility of Brownian motion
        jump_intensity (float): λ, the rate of the Poisson process (mean jumps per unit time)
        jump_scale (float): Mean size of exponential jumps
        seed (int or None): Random seed for reproducibility

    Returns:
        X (np.ndarray): Simulated Lévy process values
        t (np.ndarray): Time points
    """
    if seed is not None:
            np.random.seed(seed)

    dt = T / N
    time = np.linspace(0, T, N)

    # Drift and Brownian motion part
    dW = np.random.normal(loc=0.0, scale=np.sqrt(dt), size=N)
    W = np.cumsum(dW)
    diffusion = gamma * time + sigma * W

    # Jump part: simulate jump times and assign jump sizes
    num_jumps = np.random.poisson(jump_intensity * T)
    jump_times = np.random.uniform(0, T, size=num_jumps)
    jump_sizes = np.random.exponential(scale=jump_scale, size=num_jumps)

    jumps = np.zeros(N)
    jump_indices = np.searchsorted(time, jump_times)
    for idx, size in zip(jump_indices, jump_sizes):
        if idx < N:
            jumps[idx] += size  # do not accumulate over multiple steps

    # Build Lévy process: diffusion + jump process
    jump_process = np.cumsum(jumps)
    X = diffusion + jump_process

    return X, time
