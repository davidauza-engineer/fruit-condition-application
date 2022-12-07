# This is the app's main script.

# General configuration
import sys
from sys import path
from os import getcwd
from domains.image import Image
from domains.fruit import Fruit
from domains.color_palette import ColorPalette
import pickle
import pandas as pd
from statistics import mode
from PIL import ImageColor

path.append(getcwd() + '/domains')
model = getcwd() +'/assets/dt.pkl'

def pix_fruit_id(data, model_path):
    # load model
    loaded_model = pickle.load(open(model_path, 'rb'))
    for i in range(0, len(data)):
        data.hex_code[i] = list(ImageColor.getcolor(data.hex_code[i], 'RGB'))
    df = pd.DataFrame(data['hex_code'].to_list(), columns=['r', 'g', 'b'])
    data = pd.concat([df, data], axis=1)
    df = data.drop('hex_code', axis=1)

    return mode(loaded_model.predict(df))

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
            print(f'\nGenerating color palette for fruit {fruit.name}...\n')
            palette = ColorPalette(image=fruit.image)
            print(palette.colors)
            pred = pix_fruit_id(palette.colors, model)
            print(pred)
    print('\n')
else:
    print("\nError: The path provided doesn't contain a valid image!\n")
