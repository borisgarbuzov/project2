from setuptools import setup, setuptools

setup(
    name='project2_pkg',
    version='0.0.1',
    description='Python package for project 2',
    author='statistics101',
    url='https://github.com/statistics101/project2',
    packages=['src'],
    install_requires=[
        'numpy',
        'matplotlib',
        'pandas',
        'scikit-learn',
        'sphinx'
    ],
    python_requires='>=3.5'
)
