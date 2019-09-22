# I am using macOS and virtualenvwrapper so you might have to tune the script if you're not 
# using a virtual environment or are on another OS
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3
source /usr/local/bin/virtualenvwrapper.sh
workon dl
jupyter notebook