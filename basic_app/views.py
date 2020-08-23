from django.shortcuts import render



def index(request):
    return render(request,'basic_app/index.html')


def others(request):
    return render(request,'basic_app/others.html')

def relative(request):
    return render(request,'basic_app/relative_url_templates.html')
# Create your views here.
