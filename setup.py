#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(name="prime_functions",
      version="0.1.0",
      description="Prime number-related functions",
      author="Tom McSweeney",
      packages=find_packages("src"),
      package_dir={"": "src"},
      author_email="thomas.mcsweeney1990@gmail.com",
      install_requires=["numpy==1.20.3",
                        "pytest==6.2.4"
                        ],
      )
