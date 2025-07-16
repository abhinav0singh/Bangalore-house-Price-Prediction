import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None



def get_location_names():
    return __locations

def load_saved_artifacts():
    print("loading saved artifacts....start")
    global __data_columns
    global __locations
    global __model

    with open('./server/artifacts/columns.json', 'r') as f:
        __data_columns = json.load(f)["data_columns"]
        __locations = __data_columns[3:]
    with open('./server/artifacts/Banglore_home_price_model.pickle', 'rb') as f:
        __model = pickle.load(f)

    print("loading saved artiifacts....done")

def predict_price(location, sqft, bath, bhk):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = [0] * len(__data_columns)
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)

if __name__ == "__main__":
    load_saved_artifacts()
    print("get_location_names function()")
    print(get_location_names())

    