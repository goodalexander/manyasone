#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='manyasone',
    version='1.0.0',
    description='manyasone is a project that lets users create spell recipes that can be cast using openAI and applied to financial markets',
    author='Alex Good',
    author_email='goodalexander@gmail.com',
    url='https://github.com/goodalexander/manyasone',
    packages=find_packages(),
    install_requires=[
        'pandas>=1.1.4',
        'numpy>=1.19.2',
    ],
    entry_points={
        'console_scripts': [
            'manyasone = manyasone.__main__:main'
        ]
    }
)
