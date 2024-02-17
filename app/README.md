# FlaskStarter

FlaskStarter is a project automation script designed to kickstart your Flask web application development. It helps you set up a Flask project structure, including a virtual environment creation, a bare-bones app.py file for the backend, templates & static folders along with the index.html, index.css & index.js files for the frontend.

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

1. Install the FlaskStarter package using the following command:

   ```bash
   pip install FlaskStarterApp
   ```

   OR

   Clone this repository using the following command:

   ```bash
   git clone https://github.com/Hardvan/FlaskStarter
   cd FlaskStarter
   pip install .
   ```

2. Call the `create_flask_project` function from the FlaskStarter package to create a new Flask project:

   ```python
   from FlaskStarter import create_flask_project

   create_flask_project()
   ```

   After clicking on the link `http://127.0.0.1:5000`, you should see a Hello, World message h1 title on the webpage.

   The function accepts the following parameters:

   - **root_dir (str, optional):** Root directory for the project. Defaults to os.getcwd().
   - **create_venv (bool, optional):** Create virtual environment. Defaults to True.
   - **create_app (bool, optional):** Create app.py. Defaults to True.
   - **create_html (bool, optional):** Create index.html. Defaults to True.
   - **create_css (bool, optional):** Create index.css. Defaults to True.
   - **create_js (bool, optional):** Create index.js. Defaults to True.
   - **create_gitignore (bool, optional):** Create .gitignore. Defaults to True.
   - **execute_batch (bool, optional):** Execute the batch file. Defaults to True.

3. View the [`run.py`](./run.py) file for a complete example.

## Project Files

- **FlaskStarter.py**: The main automation script that sets up your Flask project.

- **deleter.py**: A script for deleting project files and directories, leaving only FlaskStarter.py intact. Useful for cleaning up after your project is complete. Mainly for testing purposes, not recommended for production use.

- **after.bat**: A batch script for activating the virtual environment, installing Flask and other dependencies, and running your Flask app.

## Note

- FlaskStartApp is the name of the package on PyPI, while FlaskStarter is the name of the package in the repository.

- FlaskStarter.py is the primary automation script, while deleter.py is intended for cleaning up the project files after use.

- Make sure to customize your Flask app code in app.py and add any additional dependencies to requirements.txt.

- Happy coding! 😊
