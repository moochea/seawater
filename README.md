# Read Me
To run/develop  this application, the hosting environment must have a minimum of the following installed:
* Python 3.8
* python3-pip
* virtualenv

# Developer set up
## back_end
* In the project folder, run the setup_venv.sh script to set up the virtual environment, and install dependencies
* Load the project in the IDE of choice. Ensure the interpreter is set to point to the python interpreter in the venv/bin folder (on Linux) or the venv/Scripts/ folder otherwise.
## front_end: 
Please see the README file in the front_end folder

# To run this application:
Note: These instructions assume the deployment environment is able to run shell scripts.
1. Build the Front-end components as per the README.md instructions in the front_end folder.
2. In the backend folder,  archive/zip the following files and folders
   1. blueprints
   2. data
   3. dist
   4. infrastructure
   5. logs
   6. Models
   7. app.py
   8. log_config.json
   9. requirements.txt
   10. setup_venv.sh
   11. start_app.sh
3. deploy the archive to the target environment
4. un-archive 
5. run setup_venv.sh to set up the virtual environment and install dependencies
6. run start_app.sh to start the server
7. open a browser, and navigate to the http://<IP>:80 address to access the UI.
