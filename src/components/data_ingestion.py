import os, sys
import pandas as pd
import numpy as np
from src.logger import logging
from src.exception import CustmeException
from dataclasses import dataclass
from sklearn.model_selection import train_test_split

@dataclass
class DataIngestionConfig:
    train_data_path = os.path.join('artifacts', 'train.csv')
    test_data_path = os.path.join('artifacts', 'test.csv')
    raw_data_path = os.path.join('artifacts', 'raw_data.csv')
   
    
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
        
    def initiate_data_ingestion(self):
        logging.info("Data ingestion started")
        try:
            logging.info("Data reading usnig pandas labrary from local sysytem started")
            # Read the dataset
            data = pd.read_csv(os.path.join("notebook/data","income_cleandata.csv"))
            logging.info("Data reading completed successfully")
            

            # Create directories if they don't exist
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)
            logging.info("Data splated into train and test started")

            # Save the raw data
            data.to_csv(self.ingestion_config.raw_data_path, index=False)

            # Split the data into train and test sets
            train_set, test_set = train_test_split(data, test_size= .30 , random_state = 42)
            
            # Save the train and test sets
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header = True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header = True)
            
            logging.info("Data ingestion completed successfully")
            
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        
        except Exception as e:
            logging.info("Error occurred during data ingestion")
            raise CustmeException(e, sys)
        
if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()        
    