import joblib
import pandas as pd
import sklearn
model=joblib.load('heartdisease.pkl')
print(model.predict(pd.DataFrame([[0.6875,0.,0.,0.28301887,0.5,0.702290080,0.,0.,1.,0.,0.66666667]])))