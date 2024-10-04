from setuptools import setup, find_packages

setup(
    name='batchff',                  # Name of the package
    version='0.1',                      # Version of the package
    packages=find_packages(),           # Automatically finds all the packages in your directory
    entry_points={
        'console_scripts': [
            'batchff = batchff.cli:main',  # CLI name and reference to the main function
        ],
    },
    install_requires=[
        'ffmpeg'
    ],                # Add any dependencies here
)