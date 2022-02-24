from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings

from .forms import ChestXRayImageForm
from .models import ChestXRayImage

from research.ml_models import chest_xray_predict


def upload_image(request):
    form = ChestXRayImageForm(request.POST or None, request.FILES or None)
    if request.is_ajax():
        if form.is_valid():
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

    # predict the result of image by ml model
    probability = chest_xray_predict(obj)

    context = {'probability': probability}
    return render(request, 'predict/predict_result.html', context)
