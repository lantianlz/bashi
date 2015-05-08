# -*- coding: utf-8 -*-

from common import debug
from www.misc import consts
from www.car.models import Brand, CarBasicInfo, Serial

dict_err = {
    20100: u'',
}
dict_err.update(consts.G_DICT_ERROR)


class BrandBase(object):

    def __init__(self):
        pass

    def get_city_by_id(self, city_id):
        if city_id:
            citys = self.get_all_citys().filter(id=city_id)
            if citys:
                return citys[0]

    def get_city_by_name(self, city_name):
        objs = self.get_all_citys().filter(city=city_name)
        if objs:
            return objs[0]
        return None
