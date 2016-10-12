import logging
import urllib2
import urlparse

from protorpc import remote
from protorpc import message_types

from api_resources import *
from message import *
from model import *


@api_name.api_class(resource_name='gardenApi', path='garden')
class GardenApi(remote.Service):
    @endpoints.method(WaterLevelMessage, message_types.VoidMessage, name="water_level",
                      http_method='POST', path="water_level")
    def water_level(self, request):
        m = WaterLevelModel.query().get()
        if not m:
            m = WaterLevelModel()
        m.water = request.water
        m.put()
        return message_types.VoidMessage()

    @endpoints.method(MoistureLevelMessage, message_types.VoidMessage, name="moisture_level",
                      http_method='POST', path="moisture_level")
    def moisture_level(self, request):
        m = MoistureLevelModel.query().get()
        if not m:
            m = MoistureLevelModel()
        m.moisture = request.moisture
        m.put()
        return message_types.VoidMessage()

    @endpoints.method(TemperatureMessage, message_types.VoidMessage, name="temperature_level",
                      http_method='POST', path="temperature_level")
    def temperature_level(self, request):
        m = TemperatureModel.query().get()
        if not m:
            m = TemperatureModel()
        m.temperature = request.temperature
        m.put()
        return message_types.VoidMessage()

    @endpoints.method(LightMessage, message_types.VoidMessage, name="light_level",
                      http_method='POST', path="light_level")
    def light_level(self, request):
        m = LightModel.query().get()
        if not m:
            m = LightModel()
        m.light = request.light
        m.put()
        return message_types.VoidMessage()
