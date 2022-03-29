from django.shortcuts import render
from .models import Mrs
import json


# Create your views here.
def get_info_from_close_mr(data):
    action = data.get('object_attributes').get('action')
    if action == 'close':
        return {'pr_id': data.get('project').get('id'),
                'mr_id': data.get('object_attributes').get('iid'),
                'action': data.get('object_attributes').get('action')}


def post_list(request):
    r = request.read()
    data = json.loads(r)
    resp = get_info_from_close_mr(data)
    Mrs.objects.create(project_id=int(resp.get('pr_id')), mr_id=int(resp.get('mr_id')))
    return render(request, 'post_list.html', {'data': resp})
