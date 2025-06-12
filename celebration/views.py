from django.shortcuts import render

def coming_soon(request):
    return render(request, 'celebration/coming_soon.html')