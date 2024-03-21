from setuptools import setup, find_packages

with open("app/README.md", "r") as f:
    long_description = f.read()

setup(
    name="FlaskStarterApp",
    version="1.0.2",
    author="Hardik Pawar",
    author_email="hardikpawarh@gmail.com",
    description="FlaskStarter is a project automation script designed to kickstart your Flask web application development. It helps you set up a Flask project structure, including a virtual environment creation, a bare-bones app.py file for the backend, templates & static folders along with the index.html, index.css & index.js files for the frontend.",
    package_dir={"": "app"},
    packages=find_packages(where="app"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Hardvan/FlaskStarter",
    keywords=["flask", "automation", "flask-starter",
              "flask-starter-cli", "web-development", "web"],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
