import joblib
import numpy as np
import pandas as pd

import sys
sys.path.append('notebook/')

import custom_transformer

def preprocess_input(input_data):
    """ preprocess input data """
    input_data.pop("loan_status", None)
    input_data.pop("score_proba", None)
    input_data = pd.DataFrame.from_dict(input_data, orient='index')
    return input_data


def make_predictions(input_data):
    """ function to make final prediction using pipeline """
    with open('model/PREPROCESS-CREDIT-1.0-joblib.pkl', 'rb') as f:
        fe = joblib.load(f)

    with open('model/LOGREG-CREDIT-1.0-joblib.pkl', 'rb') as f:
        model = joblib.load(f)
    input_data = preprocess_input(input_data).T.replace({
        None: np.nan,
        "null": np.nan,
        "": np.nan
        })
    
    # Feature Engineering WOE with pipeline
    input_data = fe.transform(input_data)

    # model prediction
    result = model.predict_proba(input_data)[:, 1]
    return result 