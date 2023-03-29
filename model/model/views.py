from django.http import HttpResponse
from django.shortcuts import render
import csv
import pickle


def load_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        rows = [row for row in reader]
    return rows


def home(request):
    file_path = 'static\Social_Network_Ads.csv'
    data = load_csv(file_path)
    return render(request, 'csv.html', {'data': data})


def predict(request):
    with open('static/model.pkl', 'rb') as f:
        model = pickle.load(f)
    Y_Pred = model.predict([[25, 19000]])
    return HttpResponse(Y_Pred)
