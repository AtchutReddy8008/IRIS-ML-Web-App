from django.shortcuts import render
import os
import pickle
from sklearn.neighbors import KNeighborsClassifier


dir=os.path.dirname(__file__)
model_path=os.path.join(dir,"model.pkl")
with open(model_path,"rb") as f:
    model=pickle.load(f)
# Create your views here.
def predict(request):
    prediction = None  # Initialize prediction
    if request.method == "POST":
        try:
            # Get data from the POST request
            sl = float(request.POST.get("sl"))
            sw = float(request.POST.get("sw"))
            pl = float(request.POST.get("pl"))
            pw = float(request.POST.get("pw"))
            
            # Prepare the data for prediction
            parameters = [[sl, sw, pl, pw]]
            
            # Make the prediction using the loaded model
            prediction = model.predict(parameters)[0]
            classes=["setosa","versicolor","verginica"]
            prediction=classes[prediction]
        except Exception as e:
            prediction = f"Error in prediction: {str(e)}"
    
    
    return render(request, "predict.html", {"prediction": prediction})