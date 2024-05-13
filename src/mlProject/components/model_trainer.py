import pandas as pd
import os
from mlProject import logger
import xgboost as xgb
import joblib
from sklearn.model_selection import train_test_split
from mlProject.entity.config_entity import ModelTrainerConfig

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)


        train_x = train_data.drop([self.config.target_column], axis=1)
        test_x = test_data.drop([self.config.target_column], axis=1)
        train_y = train_data[[self.config.target_column]]
        test_y = test_data[[self.config.target_column]]


        rf1 = xgb.XGBClassifier(n_estimators=100,max_depth=14)
        rf1.fit(train_x, train_y)

        joblib.dump(rf1, os.path.join(self.config.root_dir, self.config.model_name))