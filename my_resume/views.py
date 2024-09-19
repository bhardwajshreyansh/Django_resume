from django.shortcuts import render

# # # Create your views here.

# from django.shortcuts import render
# from .models import Resume

def resume_view(request):
    return render(request, 'resume.html')


# from django.http import HttpResponse


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")