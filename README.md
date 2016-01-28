disttask
========

Disttask is a utility which provides the ability to distribute a task across a fixed number of processes and collate the output, for better utilization of multiprocessing.

Use it with existing single-threaded/process tools and scripts to take full advantage of your computer's resources.

Provides the ability to distribute a task across a fixed number of processes, for better utilization of multiprocessing.

**Usage**

	Usage: disttask [cmd] [concurrent tasks] [argset]

	Use a %s in [cmd] where you want the args to go. use %d for the pipe number.
	To run a list of commands, make '%s' be your full command.

	If argset is '--', the items will be read from stdin instead of providing the arguments to disttask.
	  Execution will start immediately, so you can have disttask manage processing items that another program is feeding in.

	Disttask version 2.0.0


The application runs at most "concurrent task" number of processes (good to match total number of processors available to this number - 1).
It captures stdout and stderr to ensure that any output is not intertwined between the applications. The output is written in whole upon completion of each task.

Each command should specify a "%s" to where each argument will go (one argument from @argset per application). To feed entire commands, use simply "%s" as the "cmd" and provide the commands in your "argset".
The commands are executed by a shell, and thus can contain shell expressions.

"%d" is also available as the pipe number, which can be used to differentiate the running processes.

You can also have a program or file pipe output to disttask, by providing '--' as the argset. Disttask will run and read from stdin, treating each line as an argset item, and will terminate when stdin has been closed and all subprocesses have completed.


Examples
--------

Use disttask to connect to various hosts in parallel and execute commands:

	disttask "echo -n 'pipe %d: ' && ssh root@%s hostname" 2 "host1" "host2" "host3" "host4"
	pipe 0: host1
	pipe 1: host2
	pipe 0: host3
	pipe 1: host4


Run pyflakes, using 10 simultaneous processes, on all python files in subdirectories (requires shopt -s globstar. Notice the backticks, not single-quotes.)

	disttask "pyflakes %s" 10 `echo **/*.py`

