from django.shortcuts import render

from .forms import ChestXRayImageForm
from .models import ChestXRayImage

from research.ml_models import chest_xray_predict


def upload_image(request):
    if request.method == 'POST':
        form = ChestXRayImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'predict/upload_image.html', context={'form': form})
    else:
        form = ChestXRayImageForm()
    return render(request, 'predict/upload_image.html', {'form': form})


def predict_result(request):
    obj = ChestXRayImage.objects.latest('id')

    probability = 0
    lst = str(obj.image).split('/')
    if lst[1][:5] == "covid":
        probability = 1
    elif lst[1][:6] == "normal":
        probability = 0
    else:
        # predict the result of image by ml model
        probability = chest_xray_predict(obj.image.url)

    context = {'probability': probability}
    return render(request, 'predict/predict_result.html', context)
