from django import forms
from .models import ChestXRayImage


class ChestXRayImageForm(forms.ModelForm):
    class Meta:
        model = ChestXRayImage
        fields = ('image',)
        labels = {
            "image": "",
        }
