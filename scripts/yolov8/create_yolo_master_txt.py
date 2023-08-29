import os

def write_text_file(dataset):

    # Define the source and destination directories
    source_directory = '/home/jess/data/wild_deserts/Beyond the Fence- Tagged/labels/'
    destination_directory = '/home/jess/wd_speciesid/data/processed/yolo/'+dataset

    # Define the text file where you want to write the file paths
    output_file = os.path.join(destination_directory, (dataset+'.txt'))

    # Iterate through subdirectories in the source directory
    for subdirectory in os.listdir(source_directory):
        source_subdir = os.path.join(source_directory, subdirectory)
        destination_subdir = os.path.join(destination_directory, subdirectory)

        # Check if the subdirectory exists in the destination directory
        if os.path.exists(destination_subdir):
            # Iterate through files in the source subdirectory
            for filename in os.listdir(source_subdir):
                source_file = os.path.join(source_subdir, filename)
                destination_file = os.path.join(destination_subdir, filename)

                # Check if the file exists in the destination subdirectory
                if os.path.exists(destination_file):
                    # Write the source file path + filename to the output file
                    with open(output_file, 'a') as output:
                        output.write(source_file + '\n')

    print("File paths have been written to", output_file)

write_text_file('training')
write_text_file('validation')
write_text_file('testing')