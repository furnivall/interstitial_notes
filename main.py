import os
from datetime import datetime
from pathlib import Path
import sys
import subprocess
from termcolor import colored, cprint

# create folder for logs if doesn't exist
dirname = str(Path.home()) + "/interstit"

if not os.path.isdir(dirname):
    os.mkdir(dirname)
    cprint(f'Directory does not exist {dirname}','red')

# get date for filename
today = datetime.now().strftime('%d-%m-%y')
curr_time = datetime.now().strftime('%H:%M')




filename = dirname + '/' + today + '.html'
content = " ".join(sys.argv[2:])

def if_file_not_exist():
    # if today's file does not exist, create and add header
    if not os.path.isfile(filename):
        cprint(f"File for today does not yet exist.",'magenta')
        with open(filename, 'w') as f:
            f.write("<head>"
                    "<style>"
                    "h1{font-family:'arial'; "
                    "text-align:center;"
                    "color:white;}"
                    "body{background-color:black;}"
                    "#content{background-color:white;"
                    "width:80%;"
                    "margin:auto;"
                    "border-radius:15px;"
                    "border:1px solid black;"
                    "padding:15px;}"
                    "p{padding-left:50px;"
                    "padding-right:50px;"
                    "font-size:18px;"
                    "font-family:helvetica, arial, verdana;}"
                    ".timestamp{font-size:14;"
                    "color:grey;"
                    "}"
                    "label{display:block;"
                    "padding-left:50px;"
                    "padding-right:50px;"
                    "font-size:18px;"
                    "font-family:helvetica, arial, verdana;"
                    "margin-top:1em; margin-bottom:1em;"
                    "}"
                    "</style></head><body>")
            f.write(f'<h1>Interstit file for {today}</h1><div id="wrapper"><div id="content">')
            cprint(f'File created at \u001b]8;;{filename}\u001b\\{filename}\u001b]8;;\u001b\\', 'magenta')


def appendNote():
    with open(filename, 'a') as f:
        f.write(f'<p><span class="timestamp">{curr_time}:</span> {content}</p>')
    cprint(f'Note added - "{content}"', 'cyan')

def appendTodo():
    with open(filename, 'a') as f:
        f.write(f'<label><span class="timestamp">{curr_time}:</span> {content}<input type="checkbox"/></label>')
    cprint(f'Todo added - "{content}"', 'blue')


def openFile():
    try:
        os.startfile(filename)
    except:
        subprocess.call(['open', filename])

def bad_args():
    cprint(f'Sorry, the arguments you have provided are incorrect. Try using "todo" or "time" as your initial argument.'
           'red')

def help_text():
    cprint(f'Interstit - a timestamped note-taking application for the command line developed by Danny Furnivall.',
           attrs=['underline'])
    cprint(f'You can use the following command line arguments:', 'cyan')
    cprint(f'"time <your text here>" - this creates a note within the note file for today', 'green')
    cprint(f'"todo <your text here>" - this creates a todo item within the note file for today', 'yellow')
    cprint(f'"open" - this opens the file for today in your default browser', 'blue')

if len(sys.argv) > 1:
    if_file_not_exist()
    if sys.argv[1] == 'note':
        appendNote()
    elif sys.argv[1] == 'todo':
        appendTodo()
    elif sys.argv[1] == 'open':
        openFile()
    elif sys.argv[1] == 'help':
        help_text()
    else:
        bad_args()
else:
    help_text()


