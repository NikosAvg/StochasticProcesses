# StochasticProcesses Library

**StochasticProcesses** is an in-development Python package that provides implementations of various stochastic processes. Currently, the package includes:

- **Ornstein-Uhlenbeck Process**
- **Brownian Motion**

The package is available for development purposes on GitHub and is not yet officially released.

### Table of Contents
- [Installation](#installation)
- [Usage](#usage)
  - [Ornstein-Uhlenbeck Process](#ornstein-uhlenbeck-process)
  - [Brownian Motion](#brownian-motion)
- [Future Plans](#future-plans)
- [Contributing](#contributing)

### Installation

To install **StochasticProcesses**, you can clone the repository from GitHub and install it locally.

1. Clone the repository:

```bash
git clone https://github.com/NikosAvg/StochasticProcesses.git
cd StochasticProcesses
```

2. Install the package

```bash
pip install .
```

3. Usage

Once installed, you can easily simulate the Ornstein-Uhlenbeck process and Brownian motion with the following examples.

```Python
from StochasticProcesses import OU

# Parameters for the Ornstein-Uhlenbeck process
mu = 0        # Long-term mean
theta = 0.7   # Rate of mean reversion
sigma = 0.1   # Volatility
X0 = 1        # Initial value
T = 1         # Total time
dt = 0.01     # Time step

# Simulate the process
X, time = OU(mu=mu, theta=theta, sigma=sigma, X0=X0, T=T, dt=dt)

# Plot the result
import matplotlib.pyplot as plt
plt.plot(time, X)
plt.xlabel('Time')
plt.ylabel('X(t)')
plt.title('Ornstein-Uhlenbeck Process')
plt.show()
```

```Python
from StochasticProcesses import BrownianMotion

# Parameters for the Brownian motion
mu = 0        # Drift (mean direction)
sigma = 1     # Volatility
X0 = 0        # Initial value
T = 1         # Total time
dt = 0.01     # Time step

# Simulate the Brownian motion
X, time = BrownianMotion(mu=mu, sigma=sigma, X0=X0, T=T, dt=dt)

# Plot the result
import matplotlib.pyplot as plt
plt.plot(time, X)
plt.xlabel('Time')
plt.ylabel('W(t)')
plt.title('Brownian Motion')
plt.show()
```
### Future Plans

This package aims to include additional stochastic processes over time. Future additions may include:

- Geometric Brownian Motion (GBM)
- Poisson Process
- Levy Process
- Jump Diffusion Process


### Contributing

Contributions are welcome! If you'd like to add new processes, features, or improvements, feel free to fork the repository and submit a pull request.

Here are some guidelines:

- Fork the repository.
- Create a new branch for your changes.
- Write tests for your new feature (or process).
- Submit a pull request describing your changes.
