:mod:`files` -- Python File and Path manipulation
==================================================

.. module:: files
   :platform: Windows, Unix
   :synopsis: File, directory, and path manipulation
.. sectionauthor:: Pavel Panchekha
.. revised by Pavel Panchekha, December 2008

.. index:: pair: files; path

:Release: |version|
:Date: |today|

The :mod:`files` module for Python provides an easy way to deal with files,
directories, and paths in a Pythonic way. It was created out of a frustration
with the standard Python approach to files and directories, the venerable `os`
module.

While the :mod:`os` module and its path component, :mod:`os.path` are quite
usable and full-featured, they don't feel pythonic. The :mod:`files` module
tries to change that by grouping all the relevant features of :mod:`os` and
:mod:`os.path` into three simple classes.

The :mod:`files` module has currently been tested on Unix. Windows testing will
begin as soon as I get near enough to a Windows computer.

A quick word on usage: the :mod:`files` module was developed to be used with
Python's ``from ... import *`` syntax. Please save yourself the trouble of
typing ``files.`` all the time.

Also, the :mod:`files` module is intended to be used with Python 3. It may
break significantly in Python 2 (and then again, maybe not).

.. toctree::
   :maxdepth: 2

   path.rst
   file.rst
   dir.rst
   examples.rst
   

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
