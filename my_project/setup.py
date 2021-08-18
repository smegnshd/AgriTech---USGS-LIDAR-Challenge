# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 20:55:35 2021

@author: Smegn
"""

from setuptools import setup


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="my_lidar",
    version="0.0.1",
    author="Smegnsh Demelash",
    author_email="smegnshdem@gmail.com",
    license='MIT',
    description="Python package that contains an implementation for data fetching, loading, transforming, and visualization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/smegnshd/AgriTech---USGS-LIDAR-Challenge",
    packages=['my_lidar'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
    ],
    python_requires='>=3.5',
    install_requires =[],
    include_package_data=True,
    zip_safe=False
)
#setuptools.find_packages()