import yaml

data = {
    'train': '/home/jess2/wd_speciesid/data/processed/yolo/training', 
    'val': '/home/jess2/wd_speciesid/data/processed/yolo/validation',
    'nc': 15,
    'names': '''['trial_1']'''
    }

# Write trial_1_dataset.yaml file 
with open('config/trial_1_dataset.yaml', 'w') as file:
    yaml.dump(data, file)