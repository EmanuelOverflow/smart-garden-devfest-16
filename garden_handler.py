#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import json

from garden.model import *


class GardenHandler(webapp2.RequestHandler):
    def get(self):
        self.response.content_type = 'application/json'
        m = MoistureLevelModel.query().get()
        t = TemperatureModel.query().get()
        w = WaterLevelModel.query().get()
        l = LightModel.query().get()

        res = {}
        if m:
            res['moisture'] = m.moisture
        if t:
            res['temperature'] = t.temperature
        if w:
            res['water'] = w.water
        if l:
            res['light'] = l.light

        j_res = json.dumps(res)

        self.response.write(j_res)


app = webapp2.WSGIApplication([
    ('/garden/get', GardenHandler)
], debug=True)
