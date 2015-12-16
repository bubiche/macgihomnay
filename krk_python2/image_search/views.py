from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.core.files.base import ContentFile
from django.http import HttpResponseRedirect, HttpResponseBadRequest

from image_search.forms import ImageUploadForm
from image_search.models import RequestImage

import requests
import json
import urlparse

# Create your views here.
API_KEY = 'bbzL7Oh6D2L1krnQZ5OfKg'

def _request_url():
    return 'https://api.cloudsightapi.com/image_requests'


def _response_url(token):
    return 'https://api.cloudsightapi.com/image_responses/{}'.format(token)


def search(request):
    if request.POST:
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = RequestImage.objects.create(content=request.FILES['image'])
            headers = {
                'Authorization': 'CloudSight {}'.format(API_KEY)
            }
            data = {
                'image_request[locale]': 'en-US'
            }
            files = {
                'image_request[image]': open(image.content.path, 'rb'),
            }
            response = requests.post(_request_url(), data=data, files=files, headers=headers)
            response_data = json.loads(response.content)
            token = response_data['token']

            while True:
                response = requests.get(_response_url(token), headers=headers)
                response_data = json.loads(response.content)
                if response_data['status'] == u'completed':
                    return HttpResponseRedirect('{}?q={}'.format(reverse('search:search'), response_data['name']))
        else:
            return HttpResponseBadRequest()
    else:
        return HttpResponseBadRequest()