from django.shortcuts import render
import tensorflow as tf 
import os,sys
import numpy as np

min_max=[(46, 94),
 (48, 95),
 (0.0, 118500.0),
 (0.0, 565.0),
 (731, 2346),
 (1.0, 5.0),
 (7.0, 93.0),
 (21.0, 96.0),
 (10.0, 94.0),
 (3.0, 96.0)]

def scaling(non_scaled):
    scaled=[]
    for i in range(len(non_scaled)):
        scaled.append((non_scaled[i]-min_max[i][0])/(min_max[i][1]-min_max[i][0]))
    return scaled

def home(request):
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
    model=tf.keras.models.load_model("/var/www/html/Project/Fifa_Site/Fifa19_Model.h5")
    non_scaled_feat=[overall,potential,value,wage,special,reputation,passing,reactions,vision,composure]
    scaled_feat=scaling(non_scaled_feat)
    feat=np.array(scaled_feat)
    feat=feat.reshape(1,10)
    bidding_value=model.predict(feat)[0][0]
    print(bidding_value,feat)
    return render(request,'index.html',{'bidding':bidding_value})


# Create your views here.
