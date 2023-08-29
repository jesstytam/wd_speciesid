import os

yolo_dir = '/home/jess/data/wild_deserts/Beyond the Fence- Tagged/trial_5/labels'

# List of classes to remove
classes_to_remove = [1, 5, 6]

for camera_folder in os.listdir(yolo_dir):
    camera_folder_path = os.path.join(yolo_dir, camera_folder)
    for filename in os.listdir(camera_folder_path):
        filename_path = os.path.join(camera_folder_path, filename)
        with open(filename_path, 'r') as file:
            for line in file:
                # Extract category_id from the text file
                category_id = line[0]
                try:
                    # Check if the category_id is in the classes_to_remove list
                    if category_id in classes_to_remove:
                        os.remove(filename_path)
                        print(f"Removed {filename_path}")
                except:
                    continue

new_classes = {
    0: 'Red Kangaroo',
    1: 'Western Grey Kangaroo',
    2: 'Dingo',
    3: 'Rabbit',
    4: 'Cat',
    5: 'Small mammal',
    6: 'Goat',
    7: 'Pig',
    8: 'Euro',
    9: 'Fox',
    10: 'Echidna'
}

old_to_new_mapping = {
    11: 1,
    12: 5,
    14: 6
}

for camera_folder in os.listdir(yolo_dir):
    camera_folder_path = os.path.join(yolo_dir, camera_folder)
    
    for text_file in os.listdir(camera_folder_path):
        text_file_path = os.path.join(camera_folder_path, text_file)
        
        # Read the contents of the YOLO text file
        with open(text_file_path, 'r') as file:
            lines = file.readlines()
        
        # Modify category IDs based on the mapping
        modified_lines = []
        for line in lines:
            parts = line.strip().split(' ')
            category_id = parts[0]
            
            if category_id in old_to_new_mapping:
                parts[0] = str(old_to_new_mapping[category_id])
            
            modified_lines.append(' '.join(parts))
        
        # Write the modified content back to the file
        with open(text_file_path, 'w') as file:
            file.write('\n'.join(modified_lines))
            print(file, ' replaced')