#!/usr/bin/env python

from setuptools import setup

setup(name='harmonic_centrality',
      version='0.2',
       description='Harmonic Centrality metric realization for networkx',
       author='Alexander Petrov',
       author_email='firexel@gmail.com',
       url='https://github.com/asash/harmonic_centrality',
       packages=['harmonic_centrality'],
       install_requires = [
              'networkx',
              'HLL'],
      )

