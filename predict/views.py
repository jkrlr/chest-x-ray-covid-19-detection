import os
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.conf import settings

from .models import ChestXRayImage
from .forms import ChestXRayImageForm


def upload_image(request):
    form = ChestXRayImageForm(request.POST or None, request.FILES or None)
    if request.is_ajax():
        if form.is_valid():
            form.save()
            return JsonResponse({'message' : 'hell yeah'})
    context = {
        "form": form,
    }

    return render(request, 'predict/upload_image.html', context)

# def predicted_result(request):
#     pass
