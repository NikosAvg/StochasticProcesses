from setuptools import setup, find_packages

setup(
    name='StochasticProcesses',
    version='0.1',
    packages=find_packages(),
    install_requires=[],  # Add any dependencies here
    author='Avgoustis Nikolaso',
    author_email='nik.avg@hotmail.co,',
    description='A library to generate data from different stochastic processes.',
    long_description=open('README.md').read(),  # Optional: include a README
    long_description_content_type='text/markdown',
    url='https://github.com/NikosAvg/StochasticProcesses',
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)
