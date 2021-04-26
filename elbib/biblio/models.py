from django.contrib.auth.models import User 
from django.db import models


# Create your models here.
class Content(models.Model):
    title = models.CharField("Название", max_length=100, null=False, blank=False)
    author = models.CharField("Автор", max_length=100, null=False, blank=False)
    book = models.FileField("Документы", upload_to="books/", null=True, blank=True)
    image = models.ImageField(upload_to='uploads/')
    bo = models.TextField("Библиографическое описание", max_length=1000, null=False, blank=True)


