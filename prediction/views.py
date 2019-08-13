from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import predictionForm


# TODO use above package to require login to veiw homes @login_required


# Create your views here.
def home(request):
    return render(request, 'prediction/home.html')


def prediction(request):
    predForm = predictionForm()
    return render(request, 'prediction/prediction.html', {'form': predForm})
