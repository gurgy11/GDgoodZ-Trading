#!/bin/bash

# Install virtual environment
if [ -d "./venv" ]
then
    echo "The virtual environment is already created!"
else
    echo "The virtual environment does not exist! Creating it now..."
    virtualenv venv
fi

# Activate the virtual environment
source venv/bin/activate

# Upgrade pip
python -m pip install --upgrade pip

# Install required packages through pip
pip install flask mysql-connector-python openpyxl pandas python-dotenv

# Prepare the Flask application
export FLASK_APP=gdgoodz
export FLASK_ENV=development

# Set active Flask application as this one
FLASK_APP=gdgoodz

# Run Flask
flask run