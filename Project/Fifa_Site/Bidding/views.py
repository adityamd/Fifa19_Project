from django.shortcuts import render
import tensorflow as tf 
import os,sys
import numpy as np


def home(request):
    print(os.getcwd()+"\\Fifa19_Model")
    return render(request,'index.html',{'bidding':0})

def getBidding(request):
    overall=float(request.GET.get('Overall'))
    value=float(request.GET.get('Value'))
    special=float(request.GET.get('Special'))
    passing=float(request.GET.get('Short_Passing'))
    vision=float(request.GET.get('Vision'))
    potential=float(request.GET.get('Potential'))
    wage=float(request.GET.get('Wage'))
    reputation=float(request.GET.get('International_Reputation'))
    reactions=float(request.GET.get('Reactions'))
    composure=float(request.GET.get('Composure'))
    print(os.getcwd()+"\\Fifa19_Model")
    model=tf.keras.models.load_model(str(os.getcwd()).replace('\\','/')+"/Fifa19_Model.h5")
    feat=np.array([overall,potential,value,wage,special,reputation,passing,reactions,vision,composure])
    feat=feat.reshape(1,10)
    bidding_value=model.predict(feat)[0][0]
    return render(request,'index.html',{'bidding':bidding_value})


# Create your views here.
