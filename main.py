# This is the app's main script.

# General configuration
from sys import path
from os import getcwd
from domains.image import Image

path.append(getcwd() + "/domains")

# Application start

print('Welcome to the fruit condition application! \n\nPlease input the path of the image you want to process:\n')

image_path = input()

image = Image(path=image_path)

if image.is_valid():
    print('\nSearching for fruits in the provided image...\n')
    objects, images = image.detect_objects()
    print('\n')
    if len(objects) == 0:
        print('No objects found in the image.')
    for index, object_found in enumerate(objects):
        name = object_found['name']
        probability = object_found['percentage_probability']
        print(f'Found a/an {name} with a probability of {probability}')
        if name in ['banana', 'apple', 'orange'] and probability >= 75:
            print(f'\nGenerating color palette for object {name}...\n')
    print('\n')
else:
    print("\nError: The path provided doesn't contain a valid image!\n")
