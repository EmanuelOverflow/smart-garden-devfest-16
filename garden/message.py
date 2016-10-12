from protorpc import message_types
from protorpc import messages


class WaterLevelMessage(messages.Message):
    water = messages.StringField(1)


class MoistureLevelMessage(messages.Message):
    moisture = messages.StringField(1)


class TemperatureMessage(messages.Message):
    temperature = messages.StringField(1)


class LightMessage(messages.Message):
    light = messages.StringField(1)

