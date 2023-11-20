"""
Tool to visualize the architecture of your folder.
Often used to ask advices to ChatGPT about you project architecture.
To run, write : python folder_tree.py absolute\path\to\the\folder
"""

import os

def list_directories(startpath, max_depth=3):
    for root, dirs, _ in os.walk(startpath):
        # Compute the current depth
        depth = root.replace(startpath, '').count(os.sep)

        # Limit depth
        if depth >= max_depth:
            dirs[:] = []  # Do not visit subfolders
            continue

        # Print the stucture until the max depth
        indent = ' ' * 4 * depth
        print(f"{indent}{os.path.basename(root)}/")

if __name__ == "__main__":
    import sys
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    list_directories(path)