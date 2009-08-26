#!/usr/bin/env python

from distutils.core import setup

data = {
    "name": "files",
    "version": "1.1.1",
    "description": "Python file and path manipulation",
    "license": "GNU GPL 3",
    "author": "Pavel Panchekha",
    "author_email": "pavpanchekha@gmail.com",
    "url": "http://panchekha.no-ip.com:8080/pavpan/files.py/",
    "py_modules": ["files"],
    "classifiers": [
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
}

setup(**data)
