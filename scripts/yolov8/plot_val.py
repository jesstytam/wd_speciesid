labels = {
    0: {'label': 'Red Kangaroo', 'colour': '#C04346'},
    1: {'label': 'Kangaroo', 'colour': '#E85155'},
    2: {'label': 'Dingo', 'colour': '#FF595E'},
    3: {'label': 'Rabbit', 'colour': '#FF924C'},
    4: {'label': 'Cat', 'colour': '#FFCA3A'},
    5: {'label': 'Emu', 'colour': '#C5CA30'},
    6: {'label': 'Bird', 'colour': '#8AC926'},
    7: {'label': 'Pig', 'colour': '#52A675'},
    8: {'label': 'Euro', 'colour': '#1982C4'},
    9: {'label': 'Fox', 'colour': '#4267AC'},
    10: {'label': 'Echidna', 'colour': '#6A4C93'},
    11: {'label': 'Western Grey Kangaroo', 'colour': '#785C9D'},
    12: {'label': 'Small mammal', 'colour': '#A64692'},
    13: {'label': 'Other', 'colour': '#D43087'},
    14: {'label': 'Goat', 'colour': '#E067A7'}
    }

cameras = [
    'PCAM01',
    'PCAM02',
    'PCAM03',
    'PCAM04',
    'PCAM05',
    'PCAM06',
    'PCAM07',
    'PCAM08',
    'PCAM09',
    'PCAM10',
    'PCAM12',
    'PCAM13',
    'PCAM14',
    'PCAM15',
    'WCAM01',
    'WCAM02',
    'WCAM03',
    'WCAM04',
    'WCAM05',
    'WCAM06',
    'WCAM07',
    'WCAM08',
    'WCAM09',
    'WCAM10',
    'WCAM12',
    'WCAM13',
    'WCAM14',
    'WCAM15'
]

from PIL import Image, ImageDraw, ImageFont
import json
import os
from pathlib import Path

# Path to your predictions JSON file
predictions_path = '/home/jess2/wd_speciesid/scripts/yolov8/runs/detect/val2/predictions.json'

# Load the JSON data
with open(predictions_path, 'r') as predictions_file:
    predictions_data = json.load(predictions_file)

# Specify the root folder where your images are located
image_root_folder = '/home/jess2/data/wild_deserts/Beyond the Fence- Tagged/images/'

# Create a reverse mapping from label to category_id
label_to_category = {v['label']: k for k, v in labels.items()}

# Iterate through the predictions data
for prediction in predictions_data:
    image_id = prediction['image_id']
    category_id = prediction['category_id']
    bbox = prediction['bbox']
    score = prediction['score']

    # Get full image path
    for camera in cameras:
        if Path(os.path.join(image_root_folder, camera, image_id)).is_file:
            image_path = os.path.join(image_root_folder, camera, image_id + '.JPG')
            break

    # Load the image
    image = Image.open(image_path)

    # Create a drawing object
    draw = ImageDraw.Draw(image)

    # Use the outline color based on the category ID
    label = labels.get(category_id, {'label': 'Unknown', 'colour': '#FFFFFF'})
    outline_colour = tuple(int(label['colour'][i:i + 2], 16) for i in (1, 3, 5))  # Convert hex to RGB

    # Draw a rectangle on the image
    x, y, width, height = bbox
    draw.rectangle([x, y, x + width, y + height], outline=outline_colour, width=6)

    # Get the label text from the reverse mapping
    label_id = label_to_category.get(label['label'], 'Unknown')
    label_text = f'{label["label"]} ({score})'  # Label with category label and score
    text_color = (255, 255, 255)  # RGB color

    # Load a built-in font with the specified size
    font = ImageFont.truetype('/home/jess2/wd_speciesid/fonts/FiraMono-Bold.ttf', size=28)

    # Calculate text position
    text_x = x
    text_y = y - 36  # Adjust this value to set the text above the bounding box

    # Draw the label text on the image
    draw.text((text_x, text_y), label_text, fill=text_color, font=font)

    # Save or display the image
    # image.show()

    # If you want to save the images, uncomment the following line:
    path_to_save = f'/home/jess2/data/wild_deserts/outputs/{image_id}_output.jpg'
    image.save(path_to_save)
    print('Image saved to ' + path_to_save)