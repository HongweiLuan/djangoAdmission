
import urllib2, urllib, json, traceback
from collections import defaultdict
from datetime import date, datetime
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.core.mail import EmailMessage
from models import Prediction
from predictions.models import Prediction
from forms import AddPredictionForm
from django.db import models
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
import pandas as pd
import numpy as np
import sklearn
import scipy
import re
from numpy._distributor_init import NUMPY_MKL
import pandas_ml as pdml
from imblearn.over_sampling import SMOTE
from sklearn import preprocessing
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
import os
os.getcwd()


def manage(request):
   user_id = None
   if request.user.is_authenticated():
       user_id = request.user.id
   else:
       return HttpResponseRedirect("/admin/login/")
   if request.method == 'POST':
       post_form = AddPredictionForm(request.POST)
       if post_form.is_valid():
           GPA = post_form.cleaned_data['GPA']
           TOFEL = post_form.cleaned_data['TOFEL']
           SATI = post_form.cleaned_data['SATI']
           SchoolRankGroup = post_form.cleaned_data['SchoolRankGroup']
           Admission = post_form.cleaned_data['Admission']
           Predict = get_Predict(GPA, TOFEL, SATI, SchoolRankGroup)
           Prediction.objects.create(user=request.user, GPA = GPA, TOFEL = TOFEL, SATI = SATI, SchoolRankGroup = SchoolRankGroup, Admission = Admission, Predict = Predict)
   predictions = Prediction.objects.filter(user_id=user_id)
   form = AddPredictionForm()
   return render(request, 'manage.html', {'form': form, 'predictions': predictions, 'logged_in': True})


def del_prediction(request):
   if not request.user.is_authenticated():
       return HttpResponseRedirect("/admin/login/")
   try:
       prediction_id = int(request.GET.get('id', ''))
       p = Prediction.objects.get(id=int(prediction_id))
       p.delete()
   except:
       pass
   return HttpResponseRedirect("/")

def get_Predict(GPA, TOFEL, SATI, SchoolRankGroup):
    pDF = pd.read_csv('cleaned_nomissing_data.csv', index_col=0)
    sampled_train, sampled_test = train_test_split(pDF.as_matrix(), test_size=0.2, random_state=42)
    # convert back to pandas dataframe from array.
    trainDF1 = pd.DataFrame(sampled_train, columns=pDF.columns.values)
    testDF1 = pd.DataFrame(sampled_test, columns=pDF.columns.values)
    # split target column from data
    trainDF1target = trainDF1['result']
    trainDF1features = trainDF1.drop('result', axis=1)
    testDF1target = testDF1['result']
    testDF1features = testDF1.drop('result', axis=1)
    GBboosting = sklearn.ensemble.GradientBoostingClassifier()
    GBboosting.fit(trainDF1features, trainDF1target)
    d = trainDF1features.loc[[0]]
    d['GPA_NO'] = GPA
    d['TOFEL'] = TOFEL
    d['SATI'] = SATI
    d['RankGroup'] = SchoolRankGroup
    a = GBboosting.predict_proba(d)[0][1] * 100
    return '%.2f' % a





