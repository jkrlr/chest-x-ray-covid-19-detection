from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings

from .forms import ChestXRayImageForm
from .models import ChestXRayImage


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
    img_url = settings.MEDIA_URL + str(obj.image)

    context = {'img_url': img_url}
    return render(request, 'predict/predict_result.html', context)
