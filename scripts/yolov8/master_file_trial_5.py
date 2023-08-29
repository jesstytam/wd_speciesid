import os

def create_master_text_file(dataset):

    labels_dir = '/home/jess/data/wild_deserts/Beyond the Fence- Tagged/trial_5/labels'

    # Create a set to store the image names
    image_names = set()

    # Read the image names from the labels directory
    for camera_folder in os.listdir(labels_dir):
        camera_folder_path = os.path.join(labels_dir, camera_folder)
        if os.path.isdir(camera_folder_path):
            for text_file in os.listdir(camera_folder_path):
                image_name = text_file.split('.')[0]
                image_names.add(image_name)

    # Create a list to store the lines to keep
    lines_to_keep = []

    # Read the lines from the input file
    with open('/home/jess/wd_speciesid/data/processed/yolo/11 classes/'+dataset+'.txt', 'r') as file:
        for line in file:
            # Extract the image name from the line
            parts = line.strip().split('/')
            image_name = parts[-1].split('.')[0]
            if image_name in image_names:
                lines_to_keep.append(line)

    # Write the filtered lines back to the file
    with open('/home/jess/wd_speciesid/data/processed/yolo/11 classes/'+dataset+'.txt', 'w') as file:
        file.writelines(lines_to_keep)

create_master_text_file('training')
create_master_text_file('validation')
create_master_text_file('testing')