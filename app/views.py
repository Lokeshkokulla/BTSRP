from django.shortcuts import render

# Create your views here.
def cdn1(request):
    return render(request,'cdn1.html')

def cdn2(request):
    return render(request,'cdn2.html')    

def cdn3(request):
    return render(request,'cdn3.html')        