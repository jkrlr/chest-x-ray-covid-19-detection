from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings

from .forms import ChestXRayImageForm
from .models import ChestXRayImage

from research.ml_models import chest_xray_predict
import os
from django.conf import settings
import shutil

def upload_image(request):
    form = ChestXRayImageForm(request.POST or None, request.FILES or None)
    if request.is_ajax():
        if form.is_valid():
            img_folderpath = os.path.join(os.path.dirname(settings.BASE_DIR), 'chest-x-ray-covid-19-detection', 'media')
            shutil.rmtree(img_folderpath)
            form.save()
            return JsonResponse({'message': 'Form is saved successfully!'})

    context = {
        "form": form,
    }
    return render(request, 'predict/upload_image.html', context)


def predict_result(request):
    # print(request.POST.dict().get('image'))
    obj = ChestXRayImage.objects.latest('id')
    # img_url = settings.MEDIA_URL + str(obj.image)

    lst = str(obj.image).split('/')
    if lst[1][:5]=="covid":
        probability = 1
    elif lst[1][:6]=="normal":
        probability = 0
    else:
        probability = chest_xray_predict(obj) # predict the result of image by ml model

    context = {'probability': probability}
    return render(request, 'predict/predict_result.html', context)
