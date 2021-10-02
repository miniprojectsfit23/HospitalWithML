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

def heartdisease(request):
    if request.method == 'GET':
        return render(request, "ml_tools/heart.html", {'title':'Heart Disease Detector','resultPresent':False})
    elif request.method == 'POST':
        age=int(request.POST["age"])
        sex=int(request.POST["sex"])
        cp=int(request.POST["cp"])
        trestbps=int(request.POST["trestbps"])
        restecg=int(request.POST["restecg"])
        thalach=int(request.POST["thalach"])
        exang=int(request.POST["exang"])
        oldpeak=float(request.POST["oldpeak"])
        slope=int(request.POST["slope"])
        ca=int(request.POST["ca"])
        thal=int(request.POST["thal"])
        test=pd.DataFrame([[age,sex,cp,trestbps,restecg,thalach,exang,oldpeak,slope,ca,thal]],columns=['age', 'sex', 'cp', 'trestbps','restecg', 'thalach',
       'exang', 'oldpeak', 'slope', 'ca', 'thal'])
        model=joblib.load('model/heartdisease.pkl')
        df=pd.read_csv('model/heart.csv')
        X=df.drop(['target', 'fbs', 'chol'], axis=1)
        y=df['target']
        df=df.drop(['target','fbs', 'chol'], axis=1)
        X_train, X_test, _, _ = sklearn.model_selection.train_test_split(X, y, test_size=0.30, random_state=42)
        scaler = sklearn.preprocessing.MinMaxScaler()
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)
        test=scaler.transform(test)
        result=model.predict(test)
        print(result[0])
        return render(request, "ml_tools/heart.html", {'title':'Heart Disease Detector','resultPresent':True,'result':False if result[0]==0 else True})