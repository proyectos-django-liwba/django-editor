from django.shortcuts import render

def Index(request):
    return render(request, '../presentation/templates/presentation/index.html')