# -*- coding: utf-8 -*-

import urllib
import json
import datetime
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext
from django.shortcuts import render_to_response

from car.interface import BrandBase, SerialBase, CarBasicInfoBase

def car(request, template_name='pc/index.html'):
    brands = BrandBase().get_all_parent_brand(True)

    year = datetime.datetime.now().year
    years = range(year - 15, year + 1)
    years.reverse()
    months = range(1, 13)

    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

def get_serial_by_brand(request):
    data = []

    brand_id = request.REQUEST.get('brand_id')

    for x in SerialBase().get_serial_by_brand(brand_id, True):
        data.append({
            'value': x.id,
            'name': x.name,
            'group': x.brand.name
        })

    return HttpResponse(json.dumps(data))

def get_car_basic_info_by_serial(request):
    data = []

    serial_id = request.REQUEST.get('serial_id')

    for x in CarBasicInfoBase().get_car_basic_info_by_serial(serial_id, True):
        data.append({
            'value': x.id,
            'name': x.name,
            'group': x.year
        })

    return HttpResponse(json.dumps(data))
