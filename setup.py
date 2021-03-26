# -*- coding: utf-8 -*-
# @Author: Anderson
# @Date:   2019-11-14 17:45:03
# @Last Modified by:   ander
# @Last Modified time: 2021-03-26 15:50:02
import setuptools


setuptools.setup(
    name="unzip-rename",
    version="0.0.1",
    author="MakerBi",
    author_email="andersonby@163.com",
    description="Extract zip file and rename all files base on 'cp437' codec.",
    long_description_content_type="text/markdown",
    url="https://makerbean.com",
    packages=setuptools.find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
