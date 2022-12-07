# This is the app's main script.

# General configuration.
import sys
from sys import path
from os import getcwd
from domains.image import Image
from domains.fruit import Fruit
from domains.color_palette import ColorPalette

path.append(getcwd() + '/domains')

# Application start

print('Welcome to the fruit condition application! \n\nPlease input the path of the image you want to process:\n')

image_path = input()

image = Image(path=image_path)

if image.is_valid():
    print('\nSearching for fruits in the provided image...\n')
    objects, images = image.detect_objects()
    print('\n')
    if len(objects) == 0:
        sys.exit('No objects found in the image.')
    fruits = []
    for index, object_found in enumerate(objects):
        name = object_found['name']
        probability = object_found['percentage_probability']
        print(f'Found a/an {name} with a probability of {probability}')
        if name in ['banana', 'apple', 'orange'] and probability >= 70:
            fruits.append(Fruit(name=name, image=Image(path=images[index])))
    if len(fruits) == 0:
        sys.exit('\nNo fruits detected in the image.')
    else:
        for fruit in fruits:
            print('\n=================================================================================================')
            print(f'Generating color palette for fruit {fruit.name}...')
            print('=================================================================================================\n')
            palette = ColorPalette(image=fruit.image)
            print(palette.colors)
            print('\n')
            fruit_condition = fruit.get_condition(palette.colors)
            print('\n***************************************************************************')
            print(f'The condition for the {fruit.name} is {fruit_condition}.')
            print('***************************************************************************\n')
    print('\n')
else:
    print("\nError: The path provided doesn't contain a valid image!\n")
