import os
import sys
from laptop.logger import logging
from laptop.exception import CustomException
import pandas as pd

from laptop.components.data_ingestion import DataIngestion
from laptop.components.data_transformation import DataTransformation
from laptop.components.model_trainer import ModelTrainer


if __name__=='__main__':
    obj=DataIngestion()
    train_data_path,test_data_path=obj.initiate_data_ingestion()
    