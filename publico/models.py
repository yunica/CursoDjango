from django.db import models
from tinymce.models import HTMLField
# Create your models here.

class MyModel(models.Model):
    content = HTMLField()
    