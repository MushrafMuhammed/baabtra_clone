from django.shortcuts import render

def indexfun(request):
    return render(request, 'home/index.html')

# Create your views here.
