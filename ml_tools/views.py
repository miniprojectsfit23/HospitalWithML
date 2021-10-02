from django.shortcuts import render
from django.shortcuts import redirect
import joblib
import pandas as pd
import sklearn
# Create your views here.
def list_all(request):
    if request.user.is_authenticated:
        if request.user.isDoctor:
            return render(request, "ml_tools/list_all.html", {'title':"ML Tools"})
        else:
            return redirect("/")
    else:
        return redirect("/")

model=joblib.load('model/heartdisease.pkl')

def heartdisease(request):
    print(model.predict(pd.DataFrame([[0.6875,0.,0.,0.28301887,0.5,0.702290080,0.,0.,1.,0.,0.66666667]])))
    return redirect("/")