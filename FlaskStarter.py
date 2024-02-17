import os
import subprocess
import threading


# Global Variables
app_code = '''from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
'''
index_html_code = """<!DOCTYPE html>
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
css_code = """html {
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
js_code = '// Add your JavaScript code here\n'
batch_content = '''@echo off
call .\.venv\Scripts\\activate
pip install Flask
pip freeze > requirements.txt
python app.py
'''


def get_choice():
    """Get user choice (y/n) and return True if 'y' and False if 'n'

    Raises:
        ValueError: If the input is not 'y' or 'n'

    Returns:
        bool: True if 'y' and False if 'n'
    """

    while True:
        try:
            choice = input().lower()
            if choice in ['y', 'n']:
                return choice == 'y'
            else:
                raise ValueError
        except ValueError:
            print("Invalid input. Please enter 'y' or 'n'.")


def create_flask_project(create_venv=True, create_app=True, create_html=True, create_css=True, create_js=True, create_gitignore=True):

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
    print("Let's get started...")

    # Create virtual environment (skip if .venv exists)
    def create_venv():  # Function to create virtual environment
        subprocess.run(["python", "-m", "venv", ".venv"], check=True)
    if os.path.exists(".venv"):
        print("🔍 Found an existing virtual environment '.venv'. Skipping virtual environment creation...")
        create_venv = False
    if create_venv:  # Create a thread for creating the virtual environment
        venv_thread = threading.Thread(target=create_venv)
        venv_thread.start()
        print("🧵 Starting virtual environment creation via thread...")

    # Create app.py (ask to overwrite if exists)
    if os.path.exists("app.py"):
        print("🔍 Found an existing app.py. Overwrite (y/n)?")
        create_app = get_choice()
    if create_app:
        print("Overwriting app.py...")
        with open("app.py", "w") as app_file:
            app_file.write(app_code)
        print("✅ Created app.py")
    else:
        print("Skipping app.py creation...")

    # Set up templates folder
    os.makedirs("templates", exist_ok=True)
    print("✅ Created templates folder (No changes if it already exists)")

    # Inside templates folder, create index.html (ask to overwrite if exists)
    if os.path.exists("templates/index.html"):
        print("🔍 Found an existing index.html. Overwrite (y/n)?")
        create_html = get_choice()
    if create_html:
        with open("templates/index.html", "w") as index_html:
            index_html.write(index_html_code)
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
        print("🔍 Found an existing index.css. Overwrite (y/n)?")
        create_css = get_choice()
    if create_css:
        with open("static/css/index.css", "w") as css_file:
            css_file.write(css_code)
        print("✅ Created index.css")
    else:
        print("Skipping index.css creation...")
    if os.path.exists("static/js/index.js"):
        print("🔍 Found an existing index.js. Overwrite (y/n)?")
        create_js = get_choice()
    if create_js:
        with open("static/js/index.js", "w") as js_file:
            js_file.write(js_code)
        print("✅ Created index.js")
    else:
        print("Skipping index.js creation...")

    # Create .gitignore (overwrite if exists)
    if os.path.exists(".gitignore"):
        print("🔍 Found an existing .gitignore. Overwrite (y/n)?")
        create_gitignore = get_choice()
    if create_gitignore:
        gitignore_content = '.venv/\n__pycache__/\n.vscode/\n.env\n'
        with open(".gitignore", "w") as gitignore_file:
            gitignore_file.write(gitignore_content)
        print("✅ Created .gitignore")
    else:
        print("Skipping .gitignore creation...")

    print("🎉 Flask project setup complete.")
    print("📦 Installing dependencies...")

    # Wait for virtual environment to be created
    if create_venv:
        venv_thread.join()
        print("✅ Virtual environment created")

    # Create the batch file
    with open("after.bat", "w") as batch_file:
        batch_file.write(batch_content)
    print("✅ Created batch file")

    # Execute the batch file
    try:
        subprocess.run(["after.bat"], shell=True, check=True)
        print("✅ Installed dependencies")
    except KeyboardInterrupt:
        print("You have successfully exited the process.")

    print("\nHappy coding 😊 !")


if __name__ == "__main__":

    create_flask_project()
