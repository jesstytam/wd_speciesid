def update_text_file(dataset):

    # Define the input text file and output text file
    input_file = '/home/jess2/wd_speciesid/data/processed/yolo/' + dataset + '/' + dataset + '_list.txt'
    output_file = '/home/jess2/wd_speciesid/data/processed/yolo/' + dataset + '/' + dataset + '_list_jpg.txt'

    # Open the input file for reading
    with open(input_file, 'r') as input_f:
        # Read the content of the input file line by line
        lines = input_f.readlines()

    # Modify the lines to replace 'labels' with 'images' and '.txt' with '.jpg'
    modified_lines = []
    for line in lines:
        # Replace 'labels' with 'images' and '.txt' with '.jpg'
        modified_line = line.replace('labels', 'images').replace('.txt', '.JPG')
        modified_line = modified_line.split('Beyond the Fence- Tagged/')[1]
        modified_lines.append(modified_line)

    # Open the output file for writing and write the modified lines
    with open(output_file, 'w') as output_f:
        output_f.writelines(modified_lines)

    print("Text file has been modified and saved to", output_file)

update_text_file('training')
update_text_file('validation')
update_text_file('testing')