from os import name
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Category(models.Model):
    name = models.CharField('Название', max_length=50, null=False, blank=False)
    def __str__(self):
        return self.name

# Create your models here.
class Content(models.Model):
    title = models.CharField("Название", max_length=100, null=False, blank=False)
    author = models.CharField("Автор", max_length=100, null=False, blank=False)
    book = models.FileField("Документы", upload_to="books/", null=True, blank=True)
    image = models.ImageField(upload_to='biblio/static/uploads/', default='biblio/static/css/painbook.png')
    bo = models.TextField("Библиографическое описание", max_length=1000, null=False, blank=True)
    razdel = models.ManyToManyField(Category)
    def __str__(self):
        return self.title


class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # favorite = models.ManyToManyField(Content, null=True, blank=True)
    favorite = models.ManyToManyField(Content, null=True, blank=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            User.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.user.save()

    def __str__(self):
        return self.user.username