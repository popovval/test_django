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

#TODO
# 1) Secret token
# 2) Проверка pr_id, mr_id, action на None
# 3) .get('object_attributes').get('action') - переделать
# 4) data.get('object_attributes') - в переменную
# 5) стандартная функция (см применимость)
# 6) Оставить ответ в виде json

def post_list(request):
    # r = request.read()
    # data = json.loads(r)
    # resp = get_info_from_close_mr(data)
    # if resp is not None:
    #     Mrs.objects.create(project_id=int(resp.get('pr_id')), mr_id=int(resp.get('mr_id')))
    #     response = 'MR will be added to database'
    # else:
    #     response = 'This MR is not closed'

    return render(request, 'post_list.html', {'response': request.headers.get('X-Gitlab-Token')})
