from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.http import HttpResponseForbidden, HttpResponseNotFound, HttpResponse
from django.views import generic

from .models import Content
from django.db.models import Q

# Create your views here.

class SignInView(View):
    def get(self, request):
        return render(request, "signin.html")

    def post(self, request):
        print
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
        
            return redirect(reverse("main")) #render(request, "page.html")
        else:
            return render(request, "signin.html")


class SignUpView(View):
    def get(self, request):
        return render(request, "signup.html")

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        pass_retry = request.POST['pass_retry']

        if pass_retry == password:
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect(reverse("main"))
        else:
            return render(request, "signup.html")

class MainView(View):
    def get(self, request):
        if request.user.is_authenticated:
            print('>>>>>>> request.GET', request.GET)
            if 'search_string' not in request.GET:
                return render(request, "main.html")
            else:
                search_string = request.GET['search_string']
                return render(request, 'page.html',)
        else:
            return redirect(reverse("signin"))

# class PageView(View):
#     def get(self, request):
#         if request.user.is_authenticated:
#             return render(request, "page.html")
#         else:
#             return redirect(reverse("signin"))


class PageView(generic.ListView):
    model = Content
    context_object_name = 'page'
    template_name = 'page.html'
    def get_queryset(self):
        query = self.request.GET.get('search_string')
        return Content.objects.filter(Q(author__icontains=query) | Q(title__icontains=query))

class SpravkaView(View):
    def get(self, request):
        return render(request, "spravka.html")

class PoiskView(View):
    def get(self, request):
        return render(request, "poisk.html")