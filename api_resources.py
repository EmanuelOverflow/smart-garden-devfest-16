import endpoints

WEB_CLIENT_ID = '203983721431-vhuroiei82e7gq2dbt2at1g89nccppnh.apps.googleusercontent.com'

api_name = endpoints.api(name='smartgarden', version='v0.1',
                         # allowed_client_ids=[endpoints.API_EXPLORER_CLIENT_ID],
                         auth_level=endpoints.AUTH_LEVEL.NONE,
                         description='Smart Gardening',
                         allowed_client_ids=[WEB_CLIENT_ID, endpoints.API_EXPLORER_CLIENT_ID],
                         scopes=[endpoints.EMAIL_SCOPE])