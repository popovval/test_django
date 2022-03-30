from django.http import JsonResponse
from .models import Mrs
import json


# Create your views here.
def check_gitlab_token(request, token):
    if request.headers.get('X-Gitlab-Token') == token:
        return True
    else:
        return False


def get_info_from_close_mr(data):
    action = data.get('object_attributes').get('action')
    if action == 'close':
        return {'pr_id': data.get('project').get('id'),
                'mr_id': data.get('object_attributes').get('iid')}


#TODO
# +1) Secret token
# 2) Проверка pr_id, mr_id, action на None
# 3) .get('object_attributes').get('action') - переделать
# 4) data.get('object_attributes') - в переменную
# 5) стандартная функция (см применимость) - чот не могу найти "стандартную"
# 6) Оставить ответ в виде json

def post_list(request):
    token = 'test_token'
    if check_gitlab_token(request, token):
        r = request.read()
        data = json.loads(r)
        resp = get_info_from_close_mr(data)
        if resp is not None:
            Mrs.objects.create(project_id=int(resp.get('pr_id')), mr_id=int(resp.get('mr_id')))
            response = 'MR will be added to database'
        else:
            response = 'This MR is not closed'
    else:
        response = 'Invalid token'

    return JsonResponse({'response': response})
