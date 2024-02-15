import os
import sys
from laptop.logger import logging
from laptop.exception import CustomException
from laptop.components.data_ingestion import DataIngestion



from laptop.components.data_transformation import DataTransformation

# from laptop.components.model_trainer import ModelTrainer


if __name__=='__main__':
    
    logging.info('Data pipeline methods Starts')
    try:
    
        obj=DataIngestion()
        train_data_path,test_data_path=obj.initiate_data_ingestion()
        data_transformation = DataTransformation()
        train_arr,test_arr,_=data_transformation.initaite_data_transformation(train_data_path,test_data_path)
    except Exception as e:
        logging.info("Exception occured in the pipeline")
        raise CustomException(e,sys)