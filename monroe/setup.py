"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

setup(
    name='monroe-lib',
   version='1.0.0',

    description='Python library for interacting with the MONROE scheduler',
    long_description='Library for interacting with the MONROE scheduler',

    url='https://github.com/ana-cc/monroe-lib',

    author='Ana Custura',
    author_email='ana@netstat.org.uk',

    license='BSD 2-clause',

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: MONROE Researchers',
        'License :: OSI Approved :: BSD 2-clause License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    packages=find_packages(exclude=['docs', 'tests']),

    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    #py_modules=["monroe"],
    #install_requires=['peppercorn'],

)
