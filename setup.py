#!/usr/bin/env python

import sys
from setuptools import setup

if __name__ == '__main__':

    summary = "Utility which distributes a task across a fixed number of processes, and collates the output, for better utilization of multiprocessing"
    try:
        with open('README.rst', 'rt') as f:
            long_description = f.read()
    except Exception as e:
        sys.stderr.write('Unable to read README.rst: %s\n' %(str(e),))
        long_description = summary

    setup(name='disttask',
            version='2.3.0',
            scripts=['disttask'],
            keywords=['disttask', 'multiprocessing', 'distributed', 'concurrent', 'execution', 'command', 'xargs', 'parallel', 'threading', 'pipes', 'task', 'management'],
            description=summary,
            long_description=long_description,
            license='GPLv3',
            author='Tim Savannah',
            author_email='kata198@gmail.com',
            maintainer='Tim Savannah',
            maintainer_email='kata198@gmail.com',
            classifiers=['Development Status :: 6 - Mature',
                         'Programming Language :: Python',
                         'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
                         'Programming Language :: Python :: 2',
                          'Programming Language :: Python :: 2',
                          'Programming Language :: Python :: 2.5',
                          'Programming Language :: Python :: 2.6',
                          'Programming Language :: Python :: 2.7',
                          'Programming Language :: Python :: 3',
                          'Programming Language :: Python :: 3.4',
                          'Programming Language :: Python :: 3.5',
                          'Programming Language :: Python :: 3.6',
                          'Topic :: System :: Distributed Computing',
            ]
    )
