from django.db import models
# import os
# import uuid


# def chest_x_ray_image_upload_handler(instance, filename):
#     lst = filename.split('.') 
#     print(lst)
#     new_filename = lst[0]+str(uuid.uuid1())  # uuid1 -> uuid + timestamp
#     upload_to = 'chest_x_ray'
#     filename = '{}.{}'.format(new_filename, lst[1])
#     print(filename,new_filename)
#     return os.path.join(upload_to, filename)


class ChestXRayImage(models.Model):
    image = models.ImageField(upload_to='chest_x_ray')

    def __str__(self):
        return str(self.pk)
