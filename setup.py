from setuptools import setup

long_description = """
Disttask is a utility which provides the ability to distribute a task across a fixed number of processes, for better utilization of multiprocessing.

Use it with existing single-threaded/process tools and scripts to take full advantage of your computer's resources.

 | Usage: ./disttask [cmd] [concurrent tasks] [argset]
 | Use a %s in [cmd] where you want the args to go. use %d for the pipe number.


The application runs at most "concurrent task" # of processes ( good to match total number of processors available to this number - 1 ).
It captures stdout and stderr to ensure that any output is not intertwined between the applications.

Each command should specify a "%s" to where each argument will go (one argument from @argset per application). "%d" is also available as the pipe number, but may not be very useful.

Example:

 | ./disttask "echo %d %s" 3 "this" "is" "some" "text" "blah" "whooptie" "Doo"
 | 0 this
 | 1 is
 | 2 some
 | 0 text
 | 1 blah
 | 2 whooptie
 | 0 Doo

Another Example:

Run pyflakes, using 10 simultanious processes, on all python files in subdirectories (requires shopt -s globstar. Notice the backticks, not single-quotes.)

 | ./disttask "pyflakes %s" 10 `echo **/*.py`

"""

setup(name='disttask',
        version='1.1',
        scripts=['disttask'],
        keywords=['disttask', 'multiprocessing', 'distributed', 'concurrent', 'execution', 'command'],
        description="Utility which provides the ability to distribute a task across a fixed number of processes, for better utilization of multiprocessing",
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
		]
)
