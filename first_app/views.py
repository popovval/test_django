from django.http import JsonResponse
from .models import Mrs
import json


# Create your views here.
def check_gitlab_token(request, token):
    if request.headers.get('X-Gitlab-Token') == token:
        return True
    else:
        return False


def get_mr_info(data):
    object_attributes = data.get('object_attributes', {})
    return {'pr_id': data.get('project').get('id'),
            'mr_id': object_attributes.get('iid'),
            'action': object_attributes.get('action')}


def check_mr_info(mr_info):
    if not all((mr_info.get('pr_id'), mr_info.get('mr_id'), mr_info.get('action'))):
        return 'Invalid request json'


def create_if_mr_close(mr_info):
    if mr_info.get('action') == 'close':
        Mrs.objects.create(project_id=int(mr_info.get('pr_id')), mr_id=int(mr_info.get('mr_id')))
        return 'MR will be added to database'
    else:
        return 'This MR is not closed'


#TODO
# +1) Secret token
# +2) Проверка pr_id, mr_id, action на None
# +3) .get('object_attributes').get('action') - переделать
# +4) data.get('object_attributes') - в переменную
# +-5) стандартная функция (см применимость) - чот не могу найти "стандартную"
# +6) Оставить ответ в виде json

def post_list(request):
    token = 'test_token'
    if check_gitlab_token(request, token):
        r = request.read()
        data = json.loads(r)
        mr_info = get_mr_info(data)
        error = check_mr_info(mr_info)
        if error is None:
            response = create_if_mr_close(mr_info)
        else:
            response = error
    else:
        response = 'Invalid token'

    return JsonResponse({'dds_response': response})
