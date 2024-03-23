import pandas as pd
from sklearn.model_selection import train_test_split




def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

def split_data(data):
    # Split data code if necessary, otherwise just return the original data

    return data  # Or return split datasets

