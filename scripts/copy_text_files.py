import os
import shutil

def copy_files(dataset):

    # Define the source and destination directories
    source_base_dir = '/home/jess2/wd_speciesid/data/processed/yolo/'+dataset+'/'
    destination_base_dir = '/home/jess2/data/wild_deserts/Beyond the Fence- Tagged/labels/'

    # Iterate through subdirectories within the source directory
    for subdir in os.listdir(source_base_dir):
        source_subdir = os.path.join(source_base_dir, subdir)
        destination_subdir = os.path.join(destination_base_dir, subdir)

        # Create the corresponding destination subdirectory if it doesn't exist
        os.makedirs(destination_subdir, exist_ok=True)

        # Iterate through files in the source subdirectory
        for filename in os.listdir(source_subdir):
            source_file = os.path.join(source_subdir, filename)
            destination_file = os.path.join(destination_subdir, filename)

            # Copy the file from the source to the destination
            shutil.copy(source_file, destination_file)

    print("Files have been copied to the 'labels' directory.")

copy_files('training')
copy_files('validation')
copy_files('testing')