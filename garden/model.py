from google.appengine.ext import ndb


class WaterLevelModel(ndb.Model):
    water = ndb.StringProperty()


class MoistureLevelModel(ndb.Model):
    moisture = ndb.StringProperty()


class TemperatureModel(ndb.Model):
    temperature = ndb.StringProperty()


class LightModel(ndb.Model):
    light = ndb.StringProperty()
