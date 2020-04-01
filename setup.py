try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='pymcx',
      version='1.0',
      py_modules=['pymcx'],
      requires=['numpy'],
      description='Simple Python interface for working with MCX Monte-Carlo light simulations.',
      author='Thomas Else',
      author_email='thomas.else@cruk.cam.ac.uk',
      url='https://github.com/tre26/MCXTools',
      )