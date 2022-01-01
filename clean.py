from pathlib import Path
from shutil import rmtree

root = Path(__file__).parent

folders = [root/'HTML']
files   = [root/'autodoc.txt']

folder_names = ['__pycache__']
for folder_name in folder_names:
    for folder in root.rglob(folder_name):
        folders.append(folder)

for folder in folders:
    if folder.is_dir():
        rmtree(folder, ignore_errors=True)

for file in files:
    if file.is_file():
        file.unlink()
