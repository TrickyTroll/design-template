import shutil
from pathlib import Path

TEMPLATE = Path("./template")

for i in range(1, 16):
	if TEMPLATE.is_dir():
		new_folder = Path(f"semaine_{i}")
		if new_folder.is_dir():
			print(f"Folder {new_folder} exists!")
		else:
			shutil.copytree("./template", new_folder)
	else:
		print(f"Can't find {TEMPLATE}. Are you in the right directory?")

print("Done!")