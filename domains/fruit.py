import pickle
import pandas as pd
from statistics import mode
from PIL import ImageColor
from os import getcwd

MODEL_PATH = getcwd() +'/assets/dt.pkl'

class Fruit:
    def __init__(self, name, image):
        self.name = name
        self.image = image

    def get_condition(self, data):
        loaded_model = pickle.load(open(MODEL_PATH, 'rb'))
        for i in range(0, len(data)):
            data.hex_code[i] = list(ImageColor.getcolor(data.hex_code[i], 'RGB'))
        df = pd.DataFrame(data['hex_code'].to_list(), columns=['r', 'g', 'b'])
        data = pd.concat([df, data], axis=1)
        df = data.drop('hex_code', axis=1)

        return mode(loaded_model.predict(df))
