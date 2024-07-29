import json
import requests

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.core import serializers
from polls.models import Poll


def get_by_id(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    poll_json = serializers.serialize('json', [poll])
    struct = json.loads(poll_json)
    data = json.dumps(struct[0])
    requests.get('https://httpbin.org/get')
    return JsonResponse({'data': data})