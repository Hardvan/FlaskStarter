# FlaskStarter

FlaskStarter is a project automation script designed to kickstart your Flask web application development. It helps you set up a Flask project structure, including a virtual environment, basic Flask app, templates, and static files.

## Features

- **Virtual Environment Creation**: FlaskStarter automates the creation of a virtual environment, isolating your project dependencies.

- **Flask App Boilerplate**: Generates a basic Flask application template with a Hello World home page.

- **Directory Structure**: Sets up a project structure with templates, static folders, and a .gitignore file to manage Flask assets and project files.

- **Dependency Management**: Includes a batch script for installing Flask and other project dependencies from a requirements.txt file.

- **Cleanup**: A separate script (deleter.py) is provided for testing and learning purposes. It deletes all project files and directories, leaving only FlaskStarter.py intact.

## Use Cases

- Quickly start a new Flask project with a clean structure.
- Prototype Flask web applications.
- Experiment with Flask and frontend development.
- Automate the setup and teardown of Flask projects for testing or learning purposes.

## Getting Started

1. Clone this repository

   ```bash
    git clone https://github.com/Hardvan/FlaskStarter.git
   ```

2. Navigate to the project folder:

   ```bash
    cd FlaskStarter
   ```

3. Run FlaskStarter:

   ```bash
    python FlaskStarter.py
   ```

4. Follow the setup instructions provided by FlaskStarter.

5. To clean up the project files, run deleter.py:

   ```bash
    python deleter.py
   ```

## Project Files

- **FlaskStarter.py**: The main automation script that sets up your Flask project.

- **deleter.py**: A script for deleting project files and directories, leaving only FlaskStarter.py intact. Useful for cleaning up after your project is complete.

- **after.bat**: A batch script for activating the virtual environment, installing Flask and other dependencies, and running your Flask app.

## Note

- FlaskStarter.py is the primary automation script, while deleter.py is intended for cleaning up the project files after use.

- Make sure to customize your Flask app code in app.py and add any additional dependencies to requirements.txt.

- Happy coding! 😊
