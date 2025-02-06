import json
from pathlib import Path
import shutil

# ===================================================================================
# Create fake dataset by duplication
# ===================================================================================
def copy_folder(folder_path, new_name):

		
	folder = Path(folder_path)

	if not folder.is_dir():
		print(f"Error: '{folder_path}' is not a valid directory.")
		return

	parent_dir = folder.parent
	new_folder = parent_dir / new_name

	# Ensure a unique name if _copy already exists
	counter = 1
	assert not new_folder.exists(), f"Error: '{new_folder}' already exists."

	shutil.copytree(folder, new_folder)
	print(f"Folder copied to: {new_folder}")


if __name__ == '__main__':

    # Load valid sample names
    json_path = './data/objaverse/lvis-annotations.json'
    with open(json_path, 'r') as f:
        json_data = json.load(f)
    valid_sample_names = []
    for key in json_data.keys():
        valid_sample_names.extend(json_data[key])

    # Duplicate training samples
    n_simul_train = 5 * 6
    train_sample_names = valid_sample_names[:n_simul_train]
    for train_sample_name in train_sample_names:
        copy_folder('./data/objaverse/rendering_zero123plus/original', new_name=train_sample_name)
    print(f"{len(train_sample_names)} simulataneous(duplicate) training samples created")

    # Duplicate validation samples
    val_sample_names = valid_sample_names[-16:]
    for val_sample_name in val_sample_names:
        copy_folder('./data/objaverse/rendering_zero123plus/original', new_name=val_sample_name)
