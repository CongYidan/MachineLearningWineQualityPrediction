from setuptools import find_packages, setup

setup(
    name='WineQualityPrediction',  # Your project's name
    version='0.1.0',
    packages=find_packages(),  # Automatically find and include all packages
    description='A project for predicting wine quality',
    author='CS5100 Team',  # Optionally add your name
    license='',  # Optionally add your license
    install_requires=[
        # List your project's dependencies here.
        # This ensures that they are installed when your project is installed.
        # Example:
        'pandas',
        'numpy',
        'scikit-learn',
        'tensorflow',
        # etc.
    ],
    # If you have scripts that should be made available when the package is installed,
    # you can list them here.
    entry_points={
        'console_scripts': [
            # Example of a console script:
            # 'script-name = mymodule.myscript:main_func',
        ],
    },
)
