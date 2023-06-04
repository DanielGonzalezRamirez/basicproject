from setuptools import setup, find_packages

setup(
    name='basicproject',
    version='0.0.0',
    author='Daniel',
    author_email='your@email.com',
    description='Your package description',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'test_cli = cli.cli:main',
        ],
    },
)