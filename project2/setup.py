from setuptools import setup, setuptools

setup(
    name='project2_pkg',
    version='0.0.1',
    description='Python package for project 2',
    author='borisgarbuzov',
    url='https://github.com/borisgarbuzov/project2',
    packages=['src'],
    install_requires=[
        'numpy',
        'matplotlib',
        'pandas',
        'scikit-learn',
        'sphinx',
        'coverage',
        'joypy'
    ],
    python_requires='>=3.5'
)
