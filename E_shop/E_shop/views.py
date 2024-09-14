from django.shortcuts import render , redirect

# Create your views here.
def BASE(request):
    return render(request, 'main/base.html')


def Home(request):
    return render(request, 'main/home.html')
    # return render(request, 'main/base.html')