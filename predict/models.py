from django.db import models
import os
import uuid


def chest_x_ray_image_upload_handler(instance, filename):
    new_filename = str(uuid.uuid1())  # uuid1 -> uuid + timestamp
    upload_to = 'chest_x_ray'
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(new_filename, ext)
    return os.path.join(upload_to, filename)


class ChestXRayImage(models.Model):
    image = models.ImageField(
        upload_to=chest_x_ray_image_upload_handler, default='chest_x_ray/None/no_img.jpg')

    def __str__(self):
        return str(self.pk)
