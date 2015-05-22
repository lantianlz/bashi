# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic.simple import direct_to_template


urlpatterns = patterns('',
                       url(r'^login$', 'www.account.views.login_weixin'),
                       url(r'^login_w$', 'www.account.views.login'),
                       url(r'^get_weixin_login_state$', 'www.account.views.get_weixin_login_state'),
                       url(r'^logout$', 'www.account.views.logout'),
                       # url(r'^regist$', 'www.account.views.regist'),
                       # url(r'^forget_password$', 'www.account.views.forget_password'),
                       url(r'^qiniu_img_return$', 'www.misc.views.qiniu_img_return'),
                       url(r'^save_img$', 'www.misc.views.save_img'),
                       url(r'^crop_img$', 'www.misc.views.crop_img'),
                       # url(r'^n/(?P<nick>.*)$', 'www.account.views.get_user_by_nick'),
                       # url(r'^p/(?P<user_id>\w+)?$', 'www.account.views.user_journey'),
                       # url(r'^p/(?P<user_id>\w+)/user_answer$', 'www.account.views.user_answer'),

                       url(r'^$', 'www.car.views.car'),
                       url(r'^car/', include('www.car.urls')),
                       # url(r'^car/get_serial_by_brand$', 'www.car.views.get_serial_by_brand'),
                       # url(r'^car/get_car_basic_info_by_serial$', 'www.car.views.get_car_basic_info_by_serial'),
                       # url(r'^car/evaluate_price$', 'www.car.views.evaluate_price'),
                       # url(r'^car/sell_car$', 'www.car.views.sell_car'),
                       url(r'^car_list$', 'www.account.views.car_list'),
                       url(r'^admin/', include('www.admin.urls')),
                       url(r'^account/', include('www.account.urls')),
                       url(r'^weixin/', include('www.weixin.urls')),

                       url(r'^(?P<txt_file_name>\w+)\.txt$', 'www.misc.views.txt_view'),
                       url(r'^s/(?P<template_name>.*)$', 'www.misc.views.static_view'),
                       url(r'^500$', 'www.misc.views.test500'),
                       url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': False}),
                       url(r'^crossdomain.xml$', direct_to_template, {'template': 'crossdomain.xml'}),
                       )

urlpatterns += patterns('misc.views_paycallback',
                        (r'^alipaycallback_m$', 'alipaycallback_m'),
                        (r'^alipaynotify_m$', 'alipaynotify_m'),
                        (r'^weixinnotify$', 'weixinnotify'),
                        (r'^weixin_success_info$', 'weixin_success_info'),
                        (r'^weixinwarning$', 'weixinwarning'),

                        (r'^test_paycallback$', 'test_paycallback'),
                        )
