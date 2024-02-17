import sys
import os
from laptop.exception import CustomException

from laptop.logger import logging
from laptop.utils import load_object
import pandas as pd
import numpy as np


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            model_path=os.path.join('artifacts','model.pkl')

            preprocessor=load_object(preprocessor_path)
            model=load_object(model_path)

            data_scaled=preprocessor.transform(features)

            pred=model.predict(data_scaled)
            return pred
            

        except Exception as e:
            logging.info("Exception occured in prediction")
            raise CustomException(e,sys)
        
class CustomData:
    def __init__(self,brand:str,laptoptype:str,ram:str,weight:str,os:str,gpu:str,touchscreen:str,ips:str,
                 harddrive:str,ssd:str,screen:str,screenresolution:str,processor:str):
               
        
        self.brand=brand
        self.laptoptype=laptoptype
        self.ram=ram
        self.weight=weight
        self.os=os
        self.gpu=gpu
        self.touchscreen = touchscreen
        self.ips = ips
        self.harddrive = harddrive
        self.ssd=ssd
        self.screen=screen
        self.screenresolution=screenresolution
        self.processor=processor
     
    def extract_value(self,cell_value):
        return cell_value[0] if isinstance(cell_value, tuple) else cell_value  
     
    def get_data_as_dataframe(self):
        try:
            
            
            custom_data_input_dict = {
                'Company':[self.brand],
                'TypeName':[self.laptoptype],
                'Ram':[self.ram],
                'Weight':[self.weight],
                'os':[self.os],
                'Gpu brand':[self.gpu],
                'Touchscreen':[self.touchscreen],
                'Ips':[self.ips],
                'HDD':[self.harddrive],
                'SSD':[self.ssd],
                'Cpu brand':[self.processor],
                'screenresolution':[self.screenresolution],
                'screen':[self.screen]
                
            }
            df = pd.DataFrame(custom_data_input_dict)
        


            # Apply the conversion function to each cell
            for col in df.columns:
                df[col] = df[col].apply(self.extract_value)
            logging.info('Dataframe Gathered')
            logging.info('transformation Intiated')
            # df.to_csv("artifacts/unittst.csv")
            df['X_res'],df['Y_res']=df['screenresolution'].str.split('x')[0][0],df['screenresolution'].str.split('x')[0][1]
            df['X_res']=df['X_res'].astype('int')
            df['Y_res']=df['Y_res'].astype('int')
            df['screen']=df['screen'].astype('float')
            df=df.replace({'Yes':1,'No':0})
            df['ppi'] = (((df['X_res']**2) + (df['Y_res']**2))**0.5/df['screen'])
            df.drop(['X_res','Y_res','screenresolution','screen'],axis=1)
            logging.info('transformation finished')
            logging.info('Prediction Intiated')
            predictionobj=PredictPipeline()
            result=predictionobj.predict(df)
                    
            logging.info('Dataframe Gathered')
            rounded_result = np.round(result, 2)
            rounded_result_list = rounded_result.tolist()
            return rounded_result_list
        except Exception as e:
            logging.info('Exception Occured in prediction pipeline')
            raise CustomException(e,sys)
        
                # Function to convert set to value
    