import os
import subprocess
import threading


# Global Variables
APP_PY_CODE = '''from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

'''
INDEX_HTML_CODE = """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>

    <!-- Favicon -->
    <link
      rel="shortcut icon"
      href="{{ url_for('static', filename='favicon/favicon.png') }}"
      type="image/x-icon"
    />

    <!-- Custom CSS -->
    <link
      rel="stylesheet"
      href="{{ url_for('static', filename='css/index.css') }}"
    />
  </head>

  <body>
    <h1 class="title">Hello, World!</h1>

    <!-- Custom JS -->
    <script src="{{ url_for('static', filename='js/index.js') }}"></script>
  </body>
</html>

"""
CSS_CODE = """html {
  padding: 0;
  margin: 0;
}

body {
  padding: 0;
  margin: 0;
}

/* Disable vertical scrollbar */
::-webkit-scrollbar {
  display: none;
}

.title {
  font-size: 3rem;
  text-align: center;
}

"""
JS_CODE = '// Add your JavaScript code here\n'
BATCH_CODE = '''@echo off
call .\.venv\Scripts\\activate
pip install Flask
pip freeze > requirements.txt
python app.py
'''


def get_choice(prompt):
    """Get user choice (y/n) and return True if 'y' and False if 'n'

    Args
    ----
    - prompt (str): Prompt message

    Returns
    -------
    - bool: True if 'y' and False if 'n'
    """

    while True:
        try:
            print(prompt, end='')
            choice = input().lower()
            if choice in ['y', 'n']:
                return choice == 'y'
            raise ValueError
        except ValueError:
            print("Invalid input. Please enter 'y' or 'n'.")


def create_flask_project(root_dir=os.getcwd(), create_venv=True, create_app=True, create_html=True, create_css=True, create_js=True, create_gitignore=True, execute_batch=True):
    """Create a Flask project with the given options in the 'root_dir' and display the step-by-step instructions to run the app. The virtual environment is created in a separate thread. 'templates' and 'static' folders are created if they don't exist. 'app.py', 'index.html', 'index.css', 'index.js', and '.gitignore' are created if the user chooses to overwrite them. A batch file 'after.bat' is created to install Flask and other dependencies.

    Args
    ----
    - root_dir (str, optional): Root directory for the project. Defaults to os.getcwd().
    - create_venv (bool, optional): Create virtual environment. Defaults to True.
    - create_app (bool, optional): Create app.py. Defaults to True.
    - create_html (bool, optional): Create index.html. Defaults to True.
    - create_css (bool, optional): Create index.css. Defaults to True.
    - create_js (bool, optional): Create index.js. Defaults to True.
    - create_gitignore (bool, optional): Create .gitignore. Defaults to True.
    - execute_batch (bool, optional): Execute the batch file. Defaults to True.
    """

    # Welcome message
    print("🚀 Welcome to Flask Starter! Let's set up your Flask project.")
    print("Note: Use this script only once at the start of your project.")
    print("Run the following commands to after executing this script and exiting the running process in the terminal:")
    print("\n1️⃣  Activate the virtual environment:")
    print("For Windows:")
    print(r".\.venv\Scripts\activate")
    print("For Mac/Linux:")
    print("source .venv/bin/activate")
    print("\n2️⃣  Run the app:")
    print("python app.py")
    print()
    print("=" * 50)
    print("\nLet's get started...")

    # Change directory to the root directory
    original_dir = os.getcwd()
    if root_dir == os.getcwd():
        print("🌲 Already in the root directory")
    else:
        print(f"📂 Changing directory to {root_dir}")
        if not os.path.exists(root_dir):
            os.makedirs(root_dir, exist_ok=True)
        os.chdir(root_dir)
        print(f"Current working directory: \033[94m{os.getcwd()}\033[0m\n")

    # Create virtual environment (skip if .venv exists)
    def run_venv():  # Function to create virtual environment
        subprocess.run(["python", "-m", "venv", ".venv"], check=True)
    if os.path.exists(".venv"):
        print("🔍 Found an existing virtual environment '.venv'. Skipping virtual environment creation...")
        create_venv = False
    if create_venv:  # Create a thread for creating the virtual environment
        venv_thread = threading.Thread(target=run_venv)
        venv_thread.start()
        print("🧵 Starting virtual environment creation via thread...")

    # Create app.py (ask to overwrite if exists)
    if os.path.exists("app.py"):
        create_app = get_choice(
            "🔍 Found an existing app.py. Overwrite (y/n)?: ")
    if create_app:
        print("Overwriting app.py...")
        with open("app.py", "w") as app_file:
            app_file.write(APP_PY_CODE)
        print("✅ Created app.py")
    else:
        print("Skipping app.py creation...")

    # Set up templates folder
    os.makedirs("templates", exist_ok=True)
    print("✅ Created templates folder (No changes if it already exists)")

    # Inside templates folder, create index.html (ask to overwrite if exists)
    if os.path.exists("templates/index.html"):
        create_html = get_choice(
            "🔍 Found an existing index.html. Overwrite (y/n)?: ")
    if create_html:
        with open("templates/index.html", "w") as index_html:
            index_html.write(INDEX_HTML_CODE)
        print("✅ Created index.html")
    else:
        print("Skipping index.html creation...")

    # Set up static folder (if subfolders exist, skip creation)
    os.makedirs("static/css", exist_ok=True)
    os.makedirs("static/js", exist_ok=True)
    os.makedirs("static/images", exist_ok=True)
    os.makedirs("static/favicon", exist_ok=True)
    print("✅ Created static folder with subfolders: css, js, images, favicon (No changes if they already exist)")

    # Inside static folder, create css/index.css and js/index.js (ask to overwrite if exists)
    if os.path.exists("static/css/index.css"):
        create_css = get_choice(
            "🔍 Found an existing index.css. Overwrite (y/n)?: ")
    if create_css:
        with open("static/css/index.css", "w") as css_file:
            css_file.write(CSS_CODE)
        print("✅ Created index.css")
    else:
        print("Skipping index.css creation...")
    if os.path.exists("static/js/index.js"):
        create_js = get_choice(
            "🔍 Found an existing index.js. Overwrite (y/n)?: ")
    if create_js:
        with open("static/js/index.js", "w") as js_file:
            js_file.write(JS_CODE)
        print("✅ Created index.js")
    else:
        print("Skipping index.js creation...")

    # Create .gitignore (overwrite if exists)
    if os.path.exists(".gitignore"):
        create_gitignore = get_choice(
            "🔍 Found an existing .gitignore. Overwrite (y/n)?: ")
    if create_gitignore:
        gitignore_content = '.venv/\n__pycache__/\n.vscode/\n.env\n'
        with open(".gitignore", "w") as gitignore_file:
            gitignore_file.write(gitignore_content)
        print("✅ Created .gitignore")
    else:
        print("Skipping .gitignore creation...")

    print("🎉 Flask project backbone setup complete.")

    # Wait for virtual environment to be created
    if create_venv:
        print("🧵 Waiting for virtual environment creation to complete...")
        venv_thread.join()
        print("✅ Virtual environment created")

    # Create & execute batch file
    with open("after.bat", "w") as batch_file:
        batch_file.write(BATCH_CODE)
    print("✅ Created batch file")
    print("📦 Installing dependencies...")
    if execute_batch:
        try:
            subprocess.run(["after.bat"], shell=True, check=True)
            print("✅ Installed dependencies")
        except KeyboardInterrupt:  # To handle Ctrl+C
            print("You have successfully exited the process.")
    else:
        print("Skipping batch file execution...")

    # Change the directory back to the original directory
    os.chdir(original_dir)
    print(f"📂 Changing directory back to {original_dir}")

    print("\nHappy coding 😊 !")


if __name__ == "__main__":
    create_flask_project()
