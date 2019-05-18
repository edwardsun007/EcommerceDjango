import random
import os
from django.db import models
# Create your models here.


def get_filename_ext(filename):
    base_name = os.path.basename(filename)
    name, ext = os.path.splitext(filename)
    return name, ext

# randomize the filename and return updated upload path for image


def upload_image_path(instance, filename):
    print(instance)
    print(filename)
    new_filename = random.randint(1, 2019518888)
    name, ext = get_filename_ext(filename)  # get name and extention
    final_filename = '{new_filename}{ext}'.format(
        new_filename=new_filename, ext=ext)  # format to get new string
    return "products/{new_filename}/{final_filename}".format(new_filename=new_filename, final_filename=final_filename)


class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=19, default=39.99)
    # blank=True its not required, null=true empty value can be permited to save to databases
    # FileField will actually accept any file type thats not desired!
    image = models.FileField(
        upload_to=upload_image_path, null=True, blank=True)

    def __str__(self):
        return self.title
