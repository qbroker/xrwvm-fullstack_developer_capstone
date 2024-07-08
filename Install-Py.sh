#!/bin/bash
# Latest upd
# notice] A new release of pip is available: 24.1 -> 24.1.2
# [notice] To update, run: pip install --upgrade pip

clear
echo "cd to folder server"
cd /home/project/xrwvm-fullstack_developer_capstone/server

echo "Install Python essentials"
pip install virtualenv
virtualenv djangoenv
source djangoenv/bin/activate

echo "Install packeges required"
python3 -m pip install -U -r requirements.txt

# Perform migrations and activate models
python3 manage.py makemigrations
python3 manage.py migrate

# Start the server
python3 manage.py runserver