import endpoints

from garden import api as ga

application = endpoints.api_server([ga.GardenApi])
