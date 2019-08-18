from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from prediction.models import PredictionLog
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
    """Serves the prediction html depending on the method the user is using. If a user is posting then the form data
    will be sent to the prediction model.

    Parameters:
    request (request): holds the information about the web page.

    Returns:
    render : django shortcut to allow you to pass request data, html page and data.

   """
    if request.method == 'POST':
        predForm = predictionForm(request.POST)
        print("Entered POST")
        if predForm.is_valid():
            print("FORM VALID")
            predFormData = predForm.cleaned_data
            print(predFormData)
            if request.user.is_authenticated:
                savedform = predForm.save()
                print("user id ", request.user.id)
                print("auto id ", int(savedform.id))
                predLog = PredictionLog(userId=request.user, housePredId=savedform)
                predLog.save()
            else:
                predForm.save()
            modelPrediction = predictPrice(predFormData)
            return render(request, 'prediction/prediction.html', {'form': predForm, "prediction": modelPrediction})
        else:
            print("FORM NOT VALID")
            return render(request, 'prediction/prediction.html', {'form': predForm})
    else:
        predForm = predictionForm()
        return render(request, 'prediction/prediction.html', {'form': predForm})
