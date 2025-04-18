# StochasticProcesses/Brownian.py
"""
Simulates a Browninan Motion process using the Euler-Maruyama method.
"""
import numpy as np

def BrownianMotion(mu=0, sigma=1, X0=1, T=1, dt=0.1):
    N = int(T/dt)
    time = np.linspace(0, T, N)
    # Initialize the process array and set the initial value
    X = np.zeros(N+1)
    X[0] = X0
    for t in range(1,N+1):
        dW = np.random.normal(0, np.sqrt(dt))  # Wiener process increment
        X[t] = X[t-1] + mu*dt + sigma*dW

    return X, time
