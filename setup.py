#! /usr/bin/env python

from distutils.core import setup

setup (name='djvubind',
      version='0.1.0',
      description='Creates djvu files with positional ocr, metadata, and bookmarks.',
      author='Adam Zajac',
      author_email='strider1551@gmail.com',
      url='https://code.google.com/p/djvubind/',
      license='GPL-3',
      py_modules=['Djvubind/__init__', 'Djvubind/ocr', 'Djvubind/organizer', 'Djvubind/utils'],
      data_files=[('share/man/man1', ['docs/djvubind.1']),
                  ('bin', ['djvubind'])]
)
