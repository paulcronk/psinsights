#!/usr/bin/env python

from distutils.core import setup
from os.path import join

setup(name="psinsights",
      version="0.1",
      description="Python bindings to the PageSpeed Insights API",
      license="Apache License, Version 2.0",
      author="Devin Anderson",
      author_email="danderso@akamai.com",
      url="http://psinsights.googlecode.com/",
      packages=["psinsights"],
      scripts=[join("bin", "psinsights-analyze-url")])
