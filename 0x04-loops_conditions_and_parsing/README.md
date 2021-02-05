# 0x04. Loops, conditions and parsing

<h4>For this project, students are expected to look at this concept:</h4>

- <a href="https://intranet.hbtn.io/concepts/9">Shell</a>

## Background Context
<a href="https://www.youtube.com/watch?v=BC2neyc5GcI&feature=youtu.be">loops, conditions, and parsing</a>

## Resources
Read or watch:

<a href="https://tldp.org/LDP/Bash-Beginners-Guide/html/sect_09_01.html">Loops sample</a>
<a href="https://tldp.org/LDP/abs/html/ops.html">Variable assignment and arithmetic</a>
<a href="https://tldp.org/LDP/abs/html/comparison-ops.html">Comparison operators</a>
<a href="https://tldp.org/LDP/abs/html/fto.html">File test operators</a>
<a href="https://www.cyberciti.biz/tips/finding-bash-perl-python-portably-using-env.html">Make your scripts portable</a>

### man or help:

- env
- cut
- for
- while
- until
- if

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
- How to create SSH keys
- What is the advantage of using #!/usr/bin/env bash over #!/bin/bash
- How to use while, until and for loops
- How to use if, else, elif and case condition statements
- How to use the cut command
- What are files and other comparison operators, and how to use them

## Requirements

### General

- Allowed editors: vi, vim, emacs
- All your files will be interpreted on Ubuntu 14.04 LTS
- All your files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- You are not allowed to use awk
- Your Bash script must pass Shellcheck (version 0.3.3-1~ubuntu14.04.1 via apt-get) without any error
- The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
- The second line of all your Bash scripts should be a comment explaining what is the script doing.

## More Info

### Shellcheck

<a haref="https://github.com/koalaman/shellcheck"><strong>Shellcheck</strong></a>is a tool that will help you write proper Bash scripts. It will make recommendations on your syntax and semantics and provide advice on edge cases that you might not have thought about. Shellcheck is your friend! All your Bash scripts must pass Shellcheck without any error or you will not get any points on the task.

Shellcheck is available on the school’s computers. If you want to use it on your own computer, here is how to <a haref="https://github.com/koalaman/shellcheck#installing">install it</a>.

Examples:

Not passing Shellcheck:

<a href="https://github.com/koalaman/shellcheck/wiki/SC2034"><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/251/Vxotqyj.png"></a>

Passing Shellcheck:
<a href="https://github.com/koalaman/shellcheck/wiki/SC2034"><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/251/ubHWxDU.png"></a>