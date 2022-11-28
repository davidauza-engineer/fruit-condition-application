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
else:
    print("\nError: The path provided doesn't contain a valid image!\n")

