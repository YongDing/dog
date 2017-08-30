# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
# Create your views here.


from django.http import HttpResponse


def index(request):
    return render(request, 'weAreDog.html', {})
