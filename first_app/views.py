from django.shortcuts import render
from .models import FirstObj
import json

# Create your views here.

def post_list(request):
    r = request.read()
    data = json.loads(r)
    if data.get('test') == 'chikibamboni':
        data = 'True'
    return render(request, 'post_list.html', {'data': data})

