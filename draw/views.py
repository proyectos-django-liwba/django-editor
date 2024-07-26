from datetime import datetime
from django.shortcuts import render

def index(request):
    year_current = datetime.now().year
    return render(request, 'draw/index.html', {'year_current': year_current})

