# Read Me
To run/develop  this application, the hosting environment must have a minimum of the following installed:
* Python 3.8
* python3-pip
* virtualenv

# Developer set up
## front_end 
Please see the README file in the front_end folder
## back_end and gsw_service projects
* In the project folder, run the setup_venv.sh script to set up the virtual environment, and install dependencies. This needs to be done seperately for each project.
* Load the project in the IDE of choice. Ensure the interpreter is set to point to the python interpreter in the venv/bin folder (on Linux) or the venv/Scripts/ folder otherwise.


**Notes on the setup_venv.sh and start_app.sh scripts**
* The setup_venv.sh and start_app.sh scripts were written for a Linux environment.
* python3 is the interpreter command used in the shell scripts. This may need to be changed depending on how the python interpreter is called on the system
* it may be necessary to run the start_app.sh and setup_venv.sh scripts through dos2linux to fix the line endings
