#name =!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='spotify-python',
    version='0.0.1',
    author='Jingming Niu',
    author_email='niu@jingming.ca',
    description='Python Library for Spotify Web API',
    url='https://github.com/jingming/spotify/',
    keywords=['spotify', 'music'],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'requests>=2.0.0',
        'six'
    ]
)
