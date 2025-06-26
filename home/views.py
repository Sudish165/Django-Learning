from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hyy, Its me Sudish Karki")

def about(request):
    return HttpResponse("Inaruwa-2, Sunsari")

def services(request):
    return HttpResponse("k xa timro khabar")

def contact(request):
    return HttpResponse("9820305703")