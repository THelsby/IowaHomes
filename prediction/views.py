from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import predictionForm


# TODO use above package to require login to veiw homes @login_required


# Create your views here.
def home(request):
    return render(request, 'prediction/home.html')


def prediction(request):
    if request.method == 'POST':
        predForm = predictionForm(request.POST)
        print("Entered POST")
        if predForm.is_valid():
            predForm.save()
            return redirect('home')
        else:
            return render(request, 'prediction/prediction.html', {'form': predForm})
    else:
        predForm = predictionForm()
        return render(request, 'prediction/prediction.html', {'form': predForm})
