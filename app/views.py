from django.shortcuts import render

# Create your views here.

def fun(request):
    return render(request,'index.html')
def loc(request):
    return render(request,'index2.html')
