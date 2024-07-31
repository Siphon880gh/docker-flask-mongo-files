# Supervisor - Pyenv - Pipenv for: ARM
# ARM is commonly found in many mobile and embedded devices as well as newer Macs
# Mac's Apple Silicon processor is ARM-based. c d

# Install or select a specific Python version with pyenv
pyenv install 3.8.12  # Replace with your desired Python version

# Create a virtual environment that combines pyenv and pipenv
pyenv virtualenv 3.8.12 app1

# Activate the virtual environment
pyenv activate app1

# Install the dependencies using pipenv
cd /path/to/your/app1
pipenv install flask
pipenv install pymongo
pipenv install flask_cors
