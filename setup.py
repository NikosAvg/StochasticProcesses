from setuptools import setup, find_packages

setup(
    name='StochasticProcesses',
    version='0.1',
    packages=find_packages(),
    install_requires=[numpy, matplotlib],  # Add any dependencies here
    author='Avgoustis Nikolaos',
    author_email='nik.avg@hotmail.com',
    description='A library to generate data from different stochastic processes.',
    long_description=open('README.md').read(),  # Optional: include a README
    long_description_content_type='text/markdown',
    url='https://github.com/NikosAvg/StochasticProcesses',
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)
