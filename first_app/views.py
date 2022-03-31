from django.http import JsonResponse
from .models import Change
import json


# Create your views here.
def check_gitlab_token(request, token):
    if request.headers.get('X-Gitlab-Token') == token:
        return True
    else:
        return False


def get_mr_info(data):
    object_attributes = data.get('object_attributes', {})
    return {'pr_id': data.get('project', {}).get('id'),
            'mr_id': object_attributes.get('iid'),
            'action': object_attributes.get('action')}


def check_mr_info(mr_info):
    if not all((mr_info.get('pr_id'), mr_info.get('mr_id'), mr_info.get('action'))):
        return 'Invalid request json'


def update_if_mr_close(mr_info):
    if mr_info.get('action') == 'close':
        return update_change(mr_info.get('pr_id'), mr_info.get('mr_id'))
    else:
        return 'This MR is not closed'


def update_change(pr_id, mr_id):
    change_to_update = Change.objects.filter(uniq_source_change_id=f'gitlab:prod_id:{pr_id}:mr:{mr_id}')
    if len(change_to_update) == 1:
        change_to_update[0].is_deleted = True
        change_to_update[0].save()
        return 'Change updated'
    else:
        return f'Error in database: object with pr_id:{pr_id} mr_id:{mr_id} not unique'


def post_list(request):
    token = 'test_token'
    if check_gitlab_token(request, token):
        r = request.read()
        data = json.loads(r)
        mr_info = get_mr_info(data)
        error = check_mr_info(mr_info)
        if error is None:
            response = update_if_mr_close(mr_info)
        else:
            response = error
    else:
        response = 'Invalid token'

    return JsonResponse({'dds_response': response})
