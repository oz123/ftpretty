#!/usr/bin/env python
from setuptools import setup
import os

__version__ = '0.1.2'

def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()

setup(name='ftpretty',
      version=__version__,
      description='Pretty FTP wrapper',
      long_description=read('README.rst'),
      license='MIT',
      author='Rob Harrigan',
      author_email='harrigan.rob@gmail.com',
      url='https://github.com/codebynumbers/ftpretty/',
      download_url='https://github.com/codebynumbers/ftpretty/tarball/%s' % __version__,
      py_modules=['ftpretty'],
     )

