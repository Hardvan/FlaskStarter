import os

# List of files and folders to exclude from deletion
excluded_items = ['FlaskStarter.py']

def delete_folder_contents(path):
    for root, dirs, files in os.walk(path, topdown=False):
        for file in files:
            item_path = os.path.join(root, file)
            if os.path.basename(item_path) not in excluded_items:
                os.remove(item_path)
        for dir in dirs:
            item_path = os.path.join(root, dir)
            if os.path.basename(item_path) not in excluded_items:
                os.rmdir(item_path)

# Folders and files to delete
items_to_delete = [
    "templates",
    "static",
    ".venv",
    "__pycache__",
    ".gitignore",
    "app.py"
]

for item in items_to_delete:
    if os.path.isdir(item):
        delete_folder_contents(item)
        os.rmdir(item)
    elif os.path.isfile(item):
        os.remove(item)

print("🗑️ Folders and files have been deleted (except for FlaskStarter.py).")
