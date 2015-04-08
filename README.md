disttask
========

Disttask is a utility which provides the ability to distribute a task across a fixed number of processes, for better utilization of multiprocessing.
It is both python 2 and python 3 compatible.

Use it with existing single-threaded/process tools and scripts to take full advantage of your computer's resources.

Provides the ability to distribute a task across a fixed number of processes, for better utilization of multiprocessing.

	Usage: ./disttask [cmd] [concurrent tasks] [argset]
	Use a %s in [cmd] where you want the args to go. use %d for the pipe number.


The application runs at most "concurrent task" # of processes (good to match total number of processors available to this number - 1).
It captures stdout and stderr to ensure that any output is not intertwined between the applications.

Each command should specify a "%s" to where each argument will go (one argument from @argset per application).
"%d" is also available as the pipe number, but may not be very useful.


Example:

	./disttask "echo %d %s" 3 "this" "is" "some" "text" "blah" "whooptie" "Doo"
	0 this
	1 is
	2 some
	0 text
	1 blah
	2 whooptie
	0 Doo

Another Example:

	Run pyflakes, using 10 simultanious processes, on all python files in subdirectories (requires shopt -s globstar. Notice the backticks, not single-quotes.)
	Run php lint, using 10 simultanious processes, on all php files in subdirectories (requires shopt -s globstar)

	./disttask "php -l %s" 10 `echo **/*.php`


