from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, "AppGames/index.html")

def about(request):
    return render(request, "AppGames/about_me.html")