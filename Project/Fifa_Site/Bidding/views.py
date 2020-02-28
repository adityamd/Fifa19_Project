from django.shortcuts import render
import tensorflow as tf 
import numpy as np


def home(request):
    return render(request,'index.html',{'bidding':0})

def getBidding(request):
    print(tf.__version__)
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
    model=tf.keras.models.load_model('C:\\Users\\Aditya\\OneDrive\\Desktop\\Grras\\Practice\\fifa19\\Fifa19_Model')
    feat=np.array([overall,potential,value,wage,special,reputation,passing,reactions,vision,composure])
    print(feat)
    feat=feat.reshape(1,10)
    bidding_value=model.predict(feat)[0][0]
    print("Bidding", bidding_value)
    return render(request,'index.html',{'bidding':bidding_value})


# Create your views here.
