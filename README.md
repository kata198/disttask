disttask
========

Disttask is a utility which provides the ability to distribute a task across a fixed number of processes and collate the output, for better utilization of multiprocessing.

Use it with existing single-threaded/process tools and scripts to take full advantage of your computer's resources.

Provides the ability to distribute a task across a fixed number of processes, for better utilization of multiprocessing.

**Usage**

	Usage: disttask [cmd] [concurrent tasks] [argset]

	Use a %s in [cmd] where you want the args to go. use %d for the pipe number.
	To run a list of commands (job server), have '%s' be your full command.
	If you need a literal %s or %d, use %%s or %%d.


		Options:

			-nc or --no-collate          By default, the output will be held until the task is completed, so output is not intermixed.
										   By providing "-nc" or "--no-collate", instead each line that comes in from any running task
										   is printed, prefixed with the argset in square-brackets (e.x.  "[arg1] Some message"


		Argsets from stdin

			If argset is '--', then the argset items will be read from stdin instead of being provided on the commandline.
			Execution begins immediately, so you can use disttask as a job manager with another process feeding in items
			as they become available.


		Max Concurrency

			You may use "0" or "MAX" as the "concurrent tasks" parameter to execute all items in the argset simultaneously


		Example Usage

			disttask "ssh root@%s hostname" 3 host1 host2 host3 host4 host5 host6 # Connect and get hostname on 6 hosts, 3 at a time.

	disttask version 2.2.0



**Concurrency**

The application runs at most "concurrent task" number of processes (good to match total number of processors available to this number - 1).
It captures stdout and stderr to ensure that any output is not intertwined between the applications. 

**Output**

The output is written in whole upon completion of each task, unless "-nc" or "--no-collate" argument is provided, in which case output is printed as soon as it is available, each line prefixed with the item name in square brackets.


**Specifying Command**


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


Same example, using "no-collate" option:

	disttask "echo -n 'pipe %d: ' && ssh root@%s hostname" 2 "host1" "host2" "host3" "host4"
	[host1] pipe 0: host1
	[host2] pipe 1: host2
	[host3] pipe 0: host3
	[host4] pipe 1: host4


Run pyflakes, using 10 simultaneous processes, on all python files in subdirectories (requires shopt -s globstar. Notice the backticks, not single-quotes.)

	disttask "pyflakes %s" 10 `echo **/*.py`

