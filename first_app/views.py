from django.shortcuts import render
from .models import FirstObj
from rest_framework import viewsets
from .serializers import FirstObjSerializer


# Create your views here.

def post_list(request):
    data = FirstObj.objects.order_by('column_num')
    return render(request, 'post_list.html', {'data': data})


class FirstObjViewSet(viewsets.ModelViewSet):
    queryset = FirstObj.objects.all()
    serializer_class = FirstObjSerializer
