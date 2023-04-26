import pandas as pd
import numpy as np


def get_steam_data():
    steam_data = pd.read_csv('steam.csv')
    return steam_data
