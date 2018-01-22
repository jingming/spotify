#name =!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='spotify-python',
    version='0.0.1',
    author='Jingming Niu',
    author_email='niu@jingming.ca',
    description='Python Library for Spotify Web API',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'requests==2.18.4'          
    ]
)
