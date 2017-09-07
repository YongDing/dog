# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from moveBrick import moveBrickInfo 
# Create your views here.


from django.http import HttpResponse


def index(request):
    return render(request, 'weAreDog.html', {})

def mvBrick(request):
    info = moveBrickInfo()
    jsonObj = {"result":info}
    jsonStr = json.dumps(jsonObj)
    return HttpResponse(jsonStr, content_type='application/json; charset=utf-8')
