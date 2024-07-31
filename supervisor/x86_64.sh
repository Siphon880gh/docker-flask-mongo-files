#!/bin/bash
# Above must be first line of script. Tells shell which interpreter to use. /bin/bash is most common shell.

# Supervisor - Pyenv - Pipenv for: x86_64
# Not to be confused with x86. x86 is on even older computers' CPUs using the 32-bit x86 architecture.
# x86_64 is the architecture found in most desktops and servers.
# x86_64 is commonly used in Intel and AMD processors

# If you had to append to $PATH for any of below commands, you need to source the .bash_profile to update the $PATH
source /root/.bash_profile

# Activate pyenv environment (python interpreter) associated with app "app1"
pyenv activate app1

# Activate pipenv environment (python packages) associated with the file path as referenced by /etc/supervisor.d/*.conf

cd /home/bse7iy70lkjz/public_html/tools/flask-pipenv-supervisor/
pipenv shell

# Run script in container
python /home/bse7iy70lkjz/public_html/tools/flask-pipenv-supervisor/server.py
