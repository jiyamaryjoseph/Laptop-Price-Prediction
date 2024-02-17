import pickle
import json
import numpy as np
import sys
import os
import pandas as pd
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from laptop.logger import logging
from laptop.exception import CustomException



__brands=None
__laptoptypes=None
__rams =None
__oss =None
__weights =None
__screenresolutions =None
__processors =None
__hdds =None
__ssds = None
__gpus =None
__screens =None
__ipss =None
__touchscreens =None


       
        
global __data_brands 
global __data_laptoptypes
global __data_rams
global __data_oss
global __data_weights 
global __data_screenresolutions 
global __data_processors 
global __data_hdds 
global __data_ssds 
global __data_gpus
global __data_screens
global __data_ipss
global __data_touchscreens

__model = None

def evaluate_model(X_train,y_train,X_test,y_test,models):
    try:
        report = {}
        for i in range(len(models)):
            model = list(models.values())[i]
            # Train model
            model.fit(X_train,y_train)

            

            # Predict Testing data
            y_test_pred =model.predict(X_test)

            # Get R2 scores for train and test data
            #train_model_score = r2_score(ytrain,y_train_pred)
            test_model_score = r2_score(y_test,y_test_pred)

            report[list(models.keys())[i]] =  test_model_score

        return report
    except Exception as e:
        logging.info('Exception occured during model training')
        raise CustomException(e,sys)

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)

def load_object(file_path):
    try:
        with open(file_path,'rb') as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        logging.info('Exception Occured in load_object function utils')
        raise CustomException(e,sys)


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __brands 
    global __laptoptypes
    global __rams
    global __weights 
    global __oss 
    global __gpus 
    global __touchscreens 
    global __ipss 
    global __hdds 
    global __ssds 
    global __screens 
    global __screenresolutions
    global __processors
    
  



    with open("artifacts/columns.json", "r") as f:
        data=json.load(f)        
       
        
        __data_brands = data['data_brand']
        __data_laptoptypes = data['data_laptoptype']
        __data_rams = data['data_ram']
        __data_oss = data['data_os']
        __data_weights = data['data_weight']        
    
        __data_hdds = data['data_hdd']
        __data_ssds = data['data_ssd']
        __data_gpus = data['data_gpus']
        __data_screens = data['data_screen']
        __data_screenresolutions = data['data_screenresolution']
        __data_processors = data['data_processor']
        __data_ipss=['Yes','No']
        __data_touchscreens=['Yes','No']
        
        
        
        __brands = __data_brands
        __laptoptypes = __data_laptoptypes 
        __rams = __data_rams
        __oss = __data_oss 
        __weights = __data_weights 
        __screenresolutions = __data_screenresolutions
        __processors = __data_processors 
        __ssds = __data_ssds
        __hdds = __data_hdds 
        __gpus = __data_gpus
        __screens=__data_screens 
        __ipss=__data_ipss
        __touchscreens=__data_touchscreens

    global __model
    if __model is None:
        with open('artifacts/model.pkl', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")
    print()



def get_all_data():
    return {

                
               
        'brands': __brands,
        'laptoptypes': __laptoptypes,
        'rams': __rams,
        'oss': __oss,
        'weights': __weights,
        'screens': __screens,
        'processors': __processors,
        'ssds': __ssds,
        'hdds': __hdds,
        'gpus': __gpus,
        'ipss':__ipss,
        'touchscreen':__touchscreens,
        'screenresolutions': __screenresolutions
        
    }
    

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_all_data())
    # print(get_estimated_price('1st Phase JP Nagar',1000, 3, 3))
    # print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    # print(get_estimated_price('Kalhalli', 1000, 2, 2)) # other location
    # print(get_estimated_price('Ejipura', 1000, 2, 2))  # other location