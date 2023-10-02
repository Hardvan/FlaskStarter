import os
import subprocess

# Create a virtual environment
subprocess.run(["python", "-m", "venv", ".venv"], check=True)

# Install Flask
subprocess.run(["pip", "install", "Flask"], check=True)

# Create app.py (overwrite if exists)
app_code = '''from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
'''

with open("app.py", "w") as app_file:
    app_file.write(app_code)

# Set up templates and static folders (overwrite if exists)
os.makedirs("templates", exist_ok=True)
os.makedirs("static/css", exist_ok=True)
os.makedirs("static/js", exist_ok=True)
os.makedirs("static/images", exist_ok=True)

# Inside templates folder, create index.html (overwrite if exists)
index_html_code = """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>

    <!-- Custom CSS -->
    <link
      rel="stylesheet"
      href="{{ url_for('static', filename='css/index.css') }}"
    />
  </head>

  <body>
    <h1>Hello, World!</h1>

    <!-- Custom JS -->
    <script src="{{ url_for('static', filename='js/index.js') }}"></script>
  </body>
</html>

"""

with open("templates/index.html", "w") as index_html:
    index_html.write(index_html_code)

# Inside static folder, create css/index.css and js/index.js (overwrite if exists)
css_code = '/* Add your CSS styles here */'
js_code = '// Add your JavaScript code here'

with open("static/css/index.css", "w") as css_file:
    css_file.write(css_code)

with open("static/js/index.js", "w") as js_file:
    js_file.write(js_code)

# Create .gitignore (overwrite if exists)
gitignore_content = '.venv/\n__pycache__/\n.vscode/\n'

with open(".gitignore", "w") as gitignore_file:
    gitignore_file.write(gitignore_content)

# Create README.md (overwrite if exists)
readme_content = '# Flask Project\n\nThis is a simple Flask project.'

with open("README.md", "w") as readme_file:
    readme_file.write(readme_content)

print("Flask project setup complete.")
print("Run the following commands to get started:")

print("\n1️⃣  Activate the virtual environment:")
print("For Windows:")
print(".\.venv\Scripts\activate")
print("For Mac/Linux:")
print("source .venv/bin/activate")

print("\n2️⃣  Install Flask:")
print("pip install Flask")

print("\n3️⃣  Run the app:")
print("python app.py")

print("\nHappy coding 😊 !")
