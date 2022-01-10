# Interstit
## A quick and dirty time-stamped note-taking app using principles of interstitial note-taking.

### Pre-requisites
| Requirement | Sub-requirement | Notes |
| --- | --- | --- |
| Python | 3.7 or above | f-strings are used throughout |
| Required modules | ***termcolor***, os, subprocess, sys, pathlib, datetime | ***highlighted*** modules are not included with python by default and must be installed using pip | 
| Ideal terminal emulator | iTerm2 | Tested and working |

 ### Installation instructions
Install [Python 3.7 or greater](https://www.python.org/download)

Install termcolor from the terminal: 
```pip install termcolor```

To make this script easy to run, type the following in your terminal:
```alias is ='python3 <script location> ```


###Usage instructions

From there, you can use the following command line args - 
```is note "your note here"```
This creates a new note with a current timestamp.

```is todo "your todo here"```
This creates a todo with checkbox for the current timestamp.

```is open```
Opens today's file in a web browser tab.

```is help```
Shows the available command line arguments.




