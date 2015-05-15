# -*- coding: utf-8 -*-

from common import debug
from www.misc import consts
from www.car.models import Brand, CarBasicInfo, Serial, UserUsedCar

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

    def get_all_brand(self, state=None):
        objs = Brand.objects.all()

        if state:
            objs = objs.filter(state=state)

        return objs

    def get_all_parent_brand(self, state=None):
        objs = self.get_all_brand(state)

        return objs.filter(parent_brand__isnull=True)

    def get_children_brand(self, parent_id, state=None):
        objs = self.get_all_brand(state)

        return objs.filter(parent_brand__id=parent_id)


class SerialBase(object):

    def __init__(self):
        pass

    def get_all_serial(self, state=None):
        objs = Serial.objects.all()

        if state:
            objs = objs.filter(state=state)

        return objs

    def get_serial_by_brand(self, brand_id, state=None):
        '''
        获取品牌下的车系
        '''
        objs = self.get_all_serial()
        brand_ids = []
        # 获取品牌列表
        brands = BrandBase().get_children_brand(brand_id, True)

        if brands:
            brand_ids = [x.id for x in brands]
        else:
            brand_ids = [brand_id]

        return objs.filter(brand__in=brand_ids)


class CarBasicInfoBase(object):

    def __init__(self):
        pass

    def get_all_car_basic_info(self, state=None):
        objs = CarBasicInfo.objects.all()

        if state:
            objs = objs.filter(state=state)

        return objs

    def get_car_basic_info_by_serial(self, serial_id, state=None):
        objs = self.get_all_car_basic_info(state)

        return objs.filter(serial__id=serial_id)


class UserUsedCarBase(object):

    def __init__(self):
        pass

    def get_all_user_used_car(self):
        return UserUsedCar.objects.all().order_by('-create_time')

    def evaluate_price(self, car_basic_info_id, get_license_time, trip_distance, ip):
        price = 1
        obj = None
        try:
            obj = UserUsedCar.objects.create(
                car_id = car_basic_info_id,
                get_license_time = get_license_time,
                trip_distance = trip_distance,
                ip = ip,
                price = price
            )

        except Exception, e:
            debug.get_debug_detail(e)
            return 99900, dict_err.get(99900), price

        return 0, obj, price

    def sell_car(self, user_used_car_id, mobile):
        obj = UserUsedCar.objects.filter(id=user_used_car_id)
        if obj:
            obj = obj[0]

        try:
            obj.mobile = mobile
            obj.save()
        except Exception, e:
            debug.get_debug_detail(e)
            return 99900, dict_err.get(99900)

        return 0, dict_err.get(0)
