
import os
import pandas as pd
from sklearn.metrics import accuracy_score,precision_score,recall_score
from urllib.parse import urlparse
import numpy as np
import joblib
from mlProject.entity.config_entity import ModelEvaluationConfig
from pathlib import Path
from mlProject.utils.common import save_json

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def eval_metrics(self,actual, pred):
        accuracy = round(accuracy_score(actual, pred), 3)
        precision = round(precision_score(actual, pred), 3)
        recall = round(recall_score(actual, pred), 3)
        return accuracy, precision, recall

    
    def save_results(self):

        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[[self.config.target_column]]
        
        predicted_qualities = model.predict(test_x)

        (accuracy, precision, recall) = self.eval_metrics(test_y, predicted_qualities)
        
        # Saving metrics as local
        scores = {"A": accuracy, "P": precision, "R": recall}
        save_json(path=Path(self.config.metric_file_name), data=scores)