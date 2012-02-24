#! /usr/bin/env python

from setuptools import setup

setup(
    name="warc",
    version="0.1",
    description="Python library to work with WARC files",
    license='BSD',
    author="Anand Chitipothu",
    author_email="anandology@gmail.com",
    url="http://github.com/anandology/warc",
    packages=["warc"],
    platforms=["any"],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
