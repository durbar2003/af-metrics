#!/usr/bin/env python
# Copyright (c) 2022, Durbar Chakraborty
#
# Distributed under the 3-clause BSD license, see accompanying file LICENSE
# or https://github.com/durbar2003/af-metrics for details.

from __future__ import annotations

from setuptools import setup

setup(
    name='af-metrics',
    version='0.1.0',
    description='A Python package for monitoring the Coffea Casa Analysis Facility',
    author='Durbar Chakraborty',
    author_email='durbardibyo@gmail.com',
    packages=['af_metrics'],
    install_requires=['prometheus-client']
)

# This file is optional, on recent versions of pip you can remove it and even
# still get editable installs.
