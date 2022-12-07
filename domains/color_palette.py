import pandas as pd
import extcolors
from colormap import rgb2hex


# This function builds the dataframe with the `hex_code` and `total_pixels` based on the image colors.
def build_colors_df(colors):
    colors_list = str(colors).replace('([(', '').split(', (')[0:-1]
    df_rgb = [i.split('), ')[0] + ')' for i in colors_list]
    df_percentage = [i.split('), ')[1].replace(')', '') for i in colors_list]
    df_hex = [rgb2hex(int(i.split(', ')[0].replace('(', '')),
                      int(i.split(', ')[1]),
                      int(i.split(', ')[2].replace(')', ''))) for i in df_rgb]
    return pd.DataFrame(zip(df_hex, df_percentage), columns=['hex_code', 'total_pixels'])


# This class represents a color palette.
class ColorPalette:
    def __init__(self, image):
        self.image = image
        colors = extcolors.extract_from_path(self.image.path, tolerance=12, limit=12)
        self.colors = build_colors_df(colors)
