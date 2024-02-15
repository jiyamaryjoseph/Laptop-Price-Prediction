import pickle
import json
import numpy as np
import sys
import os
from laptop.logger import logging
from laptop.exception import CustomException

__names = None
# __data_name =None
__processors=None
__data_processor =None
__oss =None
__data_os =None
__storages =None
__data_storage =None
__displays =None
__data_display =None
__rams = None
__data_ram =None

__model = None


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)

# def get_estimated_price(name,processor,ram,os,storage,display):
#     try:
#         loc_index = __data_columns.index(location.lower())
#     except:
#         loc_index = -1

#     x = np.zeros(len(__data_columns))
#     x[0] = sqft
#     x[1] = bath
#     x[2] = bhk
#     if loc_index>=0:
#         x[loc_index] = 1

#     return round(__model.predict([x])[0],2)


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __names 
    global __data_name 
    global __processors
    global __data_processor 
    global __oss 
    global __data_os 
    global __storages 
    global __data_storage 
    global __displays 
    global __data_display 
    global __rams 
    global __data_ram 


    with open("./LaptopPricePrediction/artifacts/columns.json", "r") as f:
        data=json.load(f)
        __data_name = data['data_name']
        __data_processor = data['data_processor']
        __data_os = data['data_os']
        __data_storage = data['data_storage']
        __data_display = data['data_display']
        __data_ram = data['data_ram']
        __names = __data_name
        __processors = __data_processor 
        __oss = __data_os 
        __storages = __data_storage 
        __displays = __data_display 
        __rams = __data_ram 

    global __model
    if __model is None:
        with open('./LaptopPricePrediction/artifacts/LapTopPrice.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")
    print()



def get_all_data():
    return {
        'names': __names,
        'data_name': __data_name,
        'processors': __processors,
        'data_processor': __data_processor,
        'oss': __oss,
        'data_os': __data_os,
        'storages': __storages,
        'data_storage': __data_storage,
        'rams': __rams,
        'data_ram': __data_ram,
        'displays': __displays,
        'data_display': __data_display
    }

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_all_data())
    # print(get_estimated_price('1st Phase JP Nagar',1000, 3, 3))
    # print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    # print(get_estimated_price('Kalhalli', 1000, 2, 2)) # other location
    # print(get_estimated_price('Ejipura', 1000, 2, 2))  # other location