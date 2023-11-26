"""
Tool used to visualize the architecture of your folder.
Often used to ask advices to ChatGPT about you project architecture.

Few use case :
-python folder_tree.py absolute\path\to\the\folder
By default it will show the architecture with a depth of 3 in the folders only.

-python folder_tree.py absolute\path\to\the\folder 5
Show the architecture with a depth of 5 in the folders only.

-python folder_tree.py absolute\path\to\the\folder 5 True
Show the architecture with folder AND files with a depth of 5.
"""

import os
import sys


def list_directories(startpath, max_depth=3, show_files=False):
    for root, dirs, files in os.walk(startpath):
        # Remove directories starting with '.'
        dirs[:] = [d for d in dirs if not d.startswith(".")]

        # Compute the current depth
        depth = root.replace(startpath, "").count(os.sep)

        # Limit depth
        if depth >= max_depth:
            dirs[:] = []  # Do not visit subfolders
            continue

        # Print the structure until the max depth
        indent = " " * 4 * depth
        print(f"{indent}{os.path.basename(root)}/")

        # If show_files is True, list the files as well
        if show_files:
            file_indent = " " * 4 * (depth + 1)
            for file in files:
                print(f"{file_indent}{file}")


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "."
    max_depth = int(sys.argv[2]) if len(sys.argv) > 2 else 3
    show_files = sys.argv[3].lower() == "true" if len(sys.argv) > 3 else False
    list_directories(path, max_depth=max_depth, show_files=show_files)
