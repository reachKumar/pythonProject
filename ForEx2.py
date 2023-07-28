from pathlib import Path
src_folder_path = Path("c:/repos")
src_folder_in = src_folder_path.glob("*")

for file_path in src_folder_in:
        print(file_path.name)

