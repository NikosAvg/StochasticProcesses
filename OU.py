# StochasticProcesses/OU.py
"""
Simulates an Ornstein-Uhlenbeck process using the Euler-Maruyama method.

    The Ornstein-Uhlenbeck process is a mean-reverting stochastic process, often used
    to model systems influenced by both deterministic and random forces. This function
    generates a time series of the process over a specified time horizon.

    Parameters:
    -----------
    theta : float
        The rate of mean reversion. A larger value means the process reverts to the
        mean more quickly.
    mu : float
        The long-term mean or equilibrium value to which the process reverts.
    sigma : float
        The volatility of the process, controlling the intensity of random fluctuations.
    X0 : float
        The initial value of the process at time t=0.
    T : float
        The total time to simulate (in arbitrary time units).
    dt : float
        The time step for discretization. Smaller dt results in a more accurate approximation.

    Returns:
    --------
    X : numpy.ndarray
        An array containing the simulated values of the Ornstein-Uhlenbeck process at each
        time step.
    time : numpy.ndarray
        An array containing the time points corresponding to the values of the process.
"""
import numpy as np

def OU(theta=0.7, mu=0, sigma=1, X0=1, T=1, dt=0.1):
    # Generate the time grid
    N = int(T/dt)
    time = np.linspace(0, T, N)

    # Initialize the process array and set the initial value
    X = np.zeros(N)
    X[0] = X0
    # Generate the Ornstein-Uhlenbeck process
    for t in range(1, N):
        dW = np.random.normal(0, np.sqrt(dt))  # Wiener process increment
        X[t] = X[t-1] + theta * (mu - X[t-1]) * dt + sigma * dW
    return X, time
