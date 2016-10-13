from setuptools import setup, find_packages
import os

REPO_ROOT = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(REPO_ROOT, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='octotools',
    version='1.0',
    description='Utilities for the UK energy market from Octopus Energy',
    long_description=long_description,
    url='https://github.com/octoenergy/octotools',
    author='Octopus Energy',
    author_email='talent@octopus.energy',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
    ],
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'pytz'
    ],
    extras_require={
        'dev': [
            'wheel',
            'twine'
        ],
        'test': [
            'flake8',
            'pytest'
        ]
    }
)
