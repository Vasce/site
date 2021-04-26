from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.http import HttpResponseForbidden, HttpResponseNotFound, HttpResponse
from django.views import generic

from .models import Content

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
        
            return redirect(reverse("page"))


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
            return redirect(reverse("page"))
        else:
            return render(request, "signup.html")

class MainView(View):
    def get(self, request):
        return render(request, "main.html")

    def post(self, request):
        
        string = request.POST['search_string']
    
    
        queryset = Content.objects.filter(title__contains = string).values()
        # data = []
        # context = {'test': queryset}
        # print(queryset)
        for i in queryset:
            data = i
            # data.add(i)
            print(i)
        # print(context)
     
        # return HttpResponse(data, "test.html")
        return render(request, "test.html", data)

class PageView(View):
    def get(self, request):
        return render(request, "page.html")



class TestView(generic.ListView):
    template_name = 'test.html'

    def get_queryset(self):
        string = request.POST['search_string']
        # print(string)
        a = Content.objects.all()
        queryset = a.filter(title__contains = string)
        # print(queryset)
        return queryset

    def get(self, request):
        return render(request, "main.html")

    def post(self, request):
        
        string = request.POST['search_string']
        print(string)
    
        a = Content.objects.filter(title__contains = string)
        print(a)
        # queryset = a.
        # for i in queryset.values():
        #     t = i
            # print(t['title'])
     
            
        return a