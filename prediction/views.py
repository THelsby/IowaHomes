from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from .forms import predictionForm
import os, sys

PROJECT_DIRECTORY = os.path.dirname(__file__)
sys.path.append(os.path.join(PROJECT_DIRECTORY, "pricePrediction"))

from housePrediction import trainModel, predictPrice

# TODO use above package to require login to veiw homes @login_required

trainModel()


def home(request):
    return render(request, 'prediction/home.html')


def prediction(request):
    if request.method == 'POST':
        predForm = predictionForm(request.POST)
        print("Entered POST")
        if predForm.is_valid():
            print("FORM VALID")
            predFormData = predForm.cleaned_data
            print(predFormData)
            # del predFormData['csrfmiddlewaretoken']
            modelPrediction = predictPrice(predFormData)
            predForm.save()
            return render(request, 'prediction/prediction.html', {'form': predForm, "prediction": modelPrediction})
        else:
            print("FORM NOT VALID")
            return render(request, 'prediction/prediction.html', {'form': predForm})
    else:
        predForm = predictionForm()
        return render(request, 'prediction/prediction.html', {'form': predForm})
