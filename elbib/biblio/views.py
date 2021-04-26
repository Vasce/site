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
        if request.user.is_authenticated:
            return render(request, "page.html")
        else:
            return redirect(reverse("signin"))


class TestView(generic.ListView):
    model = Content
    context_object_name = 'test'
    # queryset = Content.objects.filter(author='Светлана')
    template_name = 'test.html'

    def get(self, request):
        string = request.GET['search_string']

        print(string)
        a = Content.objects.all()
        queryset = Content.objects.filter(Q(author__icontains=string) | Q(title__icontains=string))
        # queryset = queryset1 + queryset2
        print('>>>>>>>>>>', queryset)
        return render (request, "test.html", {'object_list': queryset})
    
    def post(self, request):

        string = request.POST['search_string']
        print(string)
    
        a = self.get_queryset(request)
        return a

    def get_queryset(self, request,  *args, **kwargs):
        string = request.GET['search_string']
        print('imhe')
        a = Content.objects.all()
        queryset = Content.objects.filter(author=string)
        return queryset
    
    # def post(self, request):

    #     string = request.POST['search_string']
    #     print(string)
    
    #     a = Content.objects.filter(title__contains = string)
    #     print(a)
    #     # queryset = a.
    #     # for i in queryset.values():
    #     #     t = i
    #         # print(t['title'])     
    #     return a

    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super().get_context_data(**kwargs)
    #     # Add in a QuerySet of all the books
    #     context['content_list'] = Content.objects.all()
    #     return context

# class TestView(generic.ListView):
#     template_name = 'test.html'

    # def get_queryset(self, request):
    #     string = request.POST['search_string']
    #     # print(string)
    #     a = Content.objects.all()
    #     queryset = a.filter(title__contains = string)
    #     # print(queryset)
    #     return queryset

#     def get(self, request):
#         return render(request, "main.html")

#     def post(self, request):
        
#         string = request.POST['search_string']
#         print(string)
    
#         a = Content.objects.filter(title__contains = string)
#         print(a)
#         # queryset = a.
#         # for i in queryset.values():
#         #     t = i
#             # print(t['title'])     
#         return a