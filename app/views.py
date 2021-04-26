from django.shortcuts import render
import pickle
from sklearn.preprocessing import StandardScaler

# Create your views here.


def index(request):
    if request.method == 'POST':
        age = float(request.POST['age'])
        anemia = int(request.POST['anemia'])
        creatinine_phosphokinase = int(request.POST['creatinine_phosphokinase'])
        diabetes = int(request.POST['diabetes'])
        ejection_function = int(request.POST['ejection_function'])
        high_blood_pressure = int(request.POST['high_blood_pressure'])
        platelets = float(request.POST['platelets'])
        serum_creatinine = float(request.POST['serum_creatinine'])
        serum_sodium = int(request.POST['serum_sodium'])
        sex = int(request.POST['sex'])
        smoking = int(request.POST['smoking'])
        time = int(request.POST['time'])
        data = [[age, anemia, creatinine_phosphokinase, diabetes, ejection_function, high_blood_pressure, platelets, serum_creatinine, serum_sodium, sex, smoking, time]]        
        print(data)
        svc = pickle.load(open('app/Random_Forest.sav', 'rb'))
        # sc = StandardScaler()
        # X_test = sc.fit_transform(data)
        predict = svc.predict(data)
        predict_proba = svc.predict_proba(data)
        print(predict_proba)
        # prob = svc.predict_proba(data)
        # print(prob)
        context = {
            'title': 'Heart Failure Prediction',
            'predict': predict,
            'predict_prob_yes':int(predict_proba[0][1] * 100),
            'predict_prob_no':int(predict_proba[0][0] * 100),

        }
    else:
        context = {
            'title': 'Heart Failure Prediction',
        }
        
    return render(request, 'app/index.html', context)