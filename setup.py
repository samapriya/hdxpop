import sys
import os
import sys
import setuptools
from setuptools import find_packages
from setuptools.command.test import test as TestCommand
from distutils.version import StrictVersion
from setuptools import __version__ as setuptools_version

if StrictVersion(setuptools_version) < StrictVersion('38.3.0'):
    raise SystemExit(
        'Your `setuptools` version is old. '
        'Please upgrade setuptools by running `pip install -U setuptools` '
        'and try again.'
    )


def readme():
    with open('README.md') as f:
        return f.read()
setuptools.setup(
    name='hdxpop',
    version='0.0.3',
    packages=['hdxpop'],
    url='https://github.com/samapriya/hdxpop',
    install_requires=['requests>=2.21.1','beautifulsoup4>=4.8.2',],
    license='MIT License',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    python_requires='>=3.2',
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: GIS',
    ),
    author='Samapriya Roy',
    author_email='samapriya.roy@gmail.com',
    description='Simple tool to download High Resolution Population Density Maps from Humanitarian Data Exchange',
    entry_points={
        "console_scripts": ["hdxpop=hdxpop.hdxpop:main"]
    },
)
