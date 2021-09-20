import pandas as pd
import numpy as np

from sklearn.base import BaseEstimator, TransformerMixin

# Add WOE for categorical features
class cat_woe_feature(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        # Home Ownership
        X['person_home_ownership_WOE'] = np.where(X['person_home_ownership'].isin(['MORTGAGE']), -0.091939, 
              np.where(X['person_home_ownership'].isin(['OTHER']), 0.177484,
              np.where(X['person_home_ownership'].isin(['OWN']), 0.036089,
              np.where(X['person_home_ownership'].isin(['RENT']), 0.066049, 0))))

        X['loan_intent_WOE'] = np.where(X['loan_intent'].isin(['DEBTCONSOLIDATION']), -0.037885, 
              np.where(X['loan_intent'].isin(['EDUCATION']), 0.012740,
              np.where(X['loan_intent'].isin(['HOMEIMPROVEMENT']), -0.137180,
              np.where(X['loan_intent'].isin(['MEDICAL']), 0.020559,
              np.where(X['loan_intent'].isin(['PERSONAL']), 0.024653, 
              np.where(X['loan_intent'].isin(['VENTURE']), 0.053819, 0))))))

        X['loan_grade_WOE'] = np.where(X['loan_grade'].isin(['A']), -0.047721, 
              np.where(X['loan_grade'].isin(['B']), 0.016784,
              np.where(X['loan_grade'].isin(['C']), 0.028512,
              np.where(X['loan_grade'].isin(['D']), 0.016817,
              np.where(X['loan_grade'].isin(['E']), 0.026253, 
              np.where(X['loan_grade'].isin(['F']), -0.091660,
              np.where(X['loan_grade'].isin(['G']), 1.000829, 0)))))))

        X['cb_person_default_on_file_WOE'] = np.where(X['cb_person_default_on_file'].isin(['N']), -0.002563, 
              np.where(X['cb_person_default_on_file'].isin(['Y']), 0.012214, 0))
        
        return X

# Add WOE for numerical features
class num_woe_feature(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        binning = [-float("inf"), 21, float("inf")]

        X['person_age_WOE'] = pd.cut(X['person_age'], bins=binning, labels=[0.393821, -0.016746])
        X['person_age_WOE'] = X['person_age_WOE'].values.add_categories('Nan').fillna('Nan') 
        X['person_age_WOE'] = X['person_age_WOE'].replace('Nan', 0)
        X['person_age_WOE'] = X['person_age_WOE'].astype(float)

        binning=[-float("inf"), 10000, 20000, 30000, 50000, 60000, 80000, float("inf")]

        X['person_income_WOE'] = pd.cut(X['person_income'], bins=binning, labels=[3.042597, 2.286484, 0.625786, 0.188507, -0.123278, -0.373376, -0.940719])
        X['person_income_WOE'] = X['person_income_WOE'].values.add_categories('Nan').fillna('Nan') 
        X['person_income_WOE'] = X['person_income_WOE'].replace('Nan', 0)
        X['person_income_WOE'] = X['person_income_WOE'].astype(float)

        # Person Employee Length - NaN detected
        binning=[-float("inf"), 1, float("inf")]

        X['person_emp_length_WOE'] = pd.cut(X['person_emp_length'], bins=binning, labels=[0.337525, -0.128373])
        X['person_emp_length_WOE'] = X['person_emp_length_WOE'].values.add_categories('Nan').fillna('Nan') 
        X['person_emp_length_WOE'] = X['person_emp_length_WOE'].replace('Nan', 0.476018)
        X['person_emp_length_WOE'] = X['person_emp_length_WOE'].astype(float)

        # Loan Amount
        binning=[-float("inf"), 10000, 15000, float("inf")]

        X['loan_amnt_WOE'] = pd.cut(X['loan_amnt'], bins=binning, labels=[-0.180622, 0.078035, 0.574856])
        X['loan_amnt_WOE'] = X['loan_amnt_WOE'].values.add_categories('Nan').fillna('Nan') 
        X['loan_amnt_WOE'] = X['loan_amnt_WOE'].replace('Nan', 0)
        X['loan_amnt_WOE'] = X['loan_amnt_WOE'].astype(float)

        # Loan Interest Rate - NaN detected
        binning=[-float("inf"), 15, float("inf")]

        X['loan_int_rate_WOE'] = pd.cut(X['loan_int_rate'], bins=binning, labels=[-0.304678, 1.614017])
        X['loan_int_rate_WOE'] = X['loan_int_rate_WOE'].values.add_categories('Nan').fillna('Nan') 
        X['loan_int_rate_WOE'] = X['loan_int_rate_WOE'].replace('Nan', -0.02675)
        X['loan_int_rate_WOE'] = X['loan_int_rate_WOE'].astype(float)

        # Loan Percent Income
        binning=[-float("inf"), 0.2, 0.3, float("inf")]

        X['loan_percent_income_WOE'] = pd.cut(X['loan_percent_income'], bins=binning, labels=[-0.584552, 0.052303, 2.151275])
        X['loan_percent_income_WOE'] = X['loan_percent_income_WOE'].values.add_categories('Nan').fillna('Nan') 
        X['loan_percent_income_WOE'] = X['loan_percent_income_WOE'].replace('Nan', 0)
        X['loan_percent_income_WOE'] = X['loan_percent_income_WOE'].astype(float)

        # Credit History
        binning=[-float("inf"), 5, 10, float("inf")]

        X['cb_person_cred_hist_length_WOE'] = pd.cut(X['cb_person_cred_hist_length'], bins=binning, labels=[0.049544, -0.075536, -0.083649])
        X['cb_person_cred_hist_length_WOE'] = X['cb_person_cred_hist_length_WOE'].values.add_categories('Nan').fillna('Nan') 
        X['cb_person_cred_hist_length_WOE'] = X['cb_person_cred_hist_length_WOE'].replace('Nan', 0)
        X['cb_person_cred_hist_length_WOE'] = X['cb_person_cred_hist_length_WOE'].astype(float)

        X = X.drop(columns=['person_age', 'person_income', 'person_emp_length', 'loan_amnt', 'loan_int_rate', 'loan_percent_income', 'cb_person_cred_hist_length'])
        return X