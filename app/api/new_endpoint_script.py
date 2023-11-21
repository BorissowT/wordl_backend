"""new_package_script.py

This script creates a new package for a new entity.
"""

import os


def create_directory_structure(name):
    directory_path = os.path.join(os.getcwd(), name)
    os.makedirs(directory_path, exist_ok=True)

    subdirectories = ["__init__.py", "model.py",
                      "controllers.py", "schema.py", "repository.py",
                      "dto_handler.py"]

    for subdirectory in subdirectories:
        file_path = os.path.join(directory_path, subdirectory)
        with open(file_path, "w") as file:
            # You can customize the content of each file as needed
            file.write('""" ' + subdirectory + ' """')

    print(f"Directory structure for '{name}' created successfully.")


if __name__ == "__main__":
    name = input("Enter a name for the directory: ")
    create_directory_structure(name)