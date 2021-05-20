from django.contrib import admin
from biblio.models import Content, Category, User
# Register your models here.
admin.site.register(Content)
admin.site.register(Category)
admin.site.register(User)