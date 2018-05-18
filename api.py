import pickle
import numpy as np

xgboost = pickle.load(open('./xgboost.pkl', 'rb'))
scaler  = pickle.load(open('./scaler.pkl', 'rb'))


def transform_input(input):
	return scaler.transform([input])

def make_hard_prediction(input):
    return xgboost.predict(transform_input(input))

def make_soft_prediction(input):
    return xgboost.predict_proba(transform_input(input))[0,1]
