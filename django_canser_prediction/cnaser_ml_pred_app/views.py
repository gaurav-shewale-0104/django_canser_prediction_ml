from django.shortcuts import render
import pickle
# Create your views here.
model = pickle.load(open("./model.pkl", "rb"))

def welcome(request):
    return render(request, "index.html")

def predict(request):
    if request.method == "POST":
        age = int(request.POST["age"])
        bmi = float(request.POST["bmi"])
        glucose = float(request.POST["glucose"])
        insuline = float(request.POST["insuline"])
        homa = float(request.POST["homa"])
        leptin = float(request.POST["leptin"])
        adiponectin = float(request.POST["adiponectin"])
        resistin = float(request.POST["resistin"])
        mcp_1 = float(request.POST["mcp_1"])


        result = model.predict([[age, bmi, glucose, insuline, homa, leptin, adiponectin, resistin, mcp_1]])
        patient = "Sorry to say, you're suffering from Breast Canser"
        success = "You're luck. You don't seem to have Canser. Enjoy!!"

        if result == 2:
            return render(request, "index.html", {'p':patient})
        elif result == 1:
            return render(request, "index.html", {'s':success})

        # return render(request, "index.html", {"prediction": result})

    return render(request, "index.html")
