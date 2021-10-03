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
        test=pd.DataFrame([[int(request.POST["age"]),int(request.POST["sex"]),int(request.POST["cp"]),int(request.POST["trestbps"]),int(request.POST["restecg"]),int(request.POST["thalach"])
        ,int(request.POST["exang"]),float(request.POST["oldpeak"]),int(request.POST["slope"]),int(request.POST["ca"])
        ,int(request.POST["thal"])]],columns=['age', 'sex', 'cp', 'trestbps','restecg', 'thalach',
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

def breastcancer(request):
    if request.method == 'GET':
        return render(request, "ml_tools/breastcancer.html", {'title':'Heart Disease Detector','resultPresent':False})
    elif request.method == 'POST':
        test=pd.DataFrame([[float(request.POST['texture_mean']), float(request.POST['perimeter_mean']), float(request.POST['smoothness_mean']), float(request.POST['compactness_mean']),
        float(request.POST['concavity_mean']), float(request.POST['concave points_mean']), float(request.POST['symmetry_mean']), float(request.POST['radius_se']),
        float(request.POST['compactness_se']), float(request.POST['concavity_se']), float(request.POST['concave points_se']), float(request.POST['texture_worst']),
        float(request.POST['smoothness_worst']), float(request.POST['compactness_worst']), float(request.POST['concavity_worst']),
        float(request.POST['concave points_worst']), float(request.POST['symmetry_worst']), float(request.POST['fractal_dimension_worst'])]],columns=['texture_mean', 'perimeter_mean', 'smoothness_mean', 'compactness_mean',
       'concavity_mean', 'concave points_mean', 'symmetry_mean', 'radius_se',
       'compactness_se', 'concavity_se', 'concave points_se', 'texture_worst',
       'smoothness_worst', 'compactness_worst', 'concavity_worst',
       'concave points_worst', 'symmetry_worst', 'fractal_dimension_worst'])
        model=joblib.load('model/breastcancer.pkl')
        result=model.predict(test)
        return render(request, "ml_tools/breastcancer.html", {'title':'Heart Disease Detector','resultPresent':True,'result':False if result[0]==0 else True
        })