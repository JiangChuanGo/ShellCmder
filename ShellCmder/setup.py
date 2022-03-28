#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages

setup(
    name='ShellCmder',
    version=0.01,
    description=(
        'A shell wrapper for Linux.'
    ),
    long_description=open('../ReadMe.md').read(),
    author='JiangChuanGo',
    author_email='jiang.huchuan@qq.com',
    maintainer='JiangChuanGo',
    maintainer_email='jiang.huchuan@qq.com',
    license='GPL 2.0 License',
    packages=find_packages(),
    platforms=["Linux"],
    url='https://github.com/JiangChuanGo/ShellCmder',
    install_requires = []
)
