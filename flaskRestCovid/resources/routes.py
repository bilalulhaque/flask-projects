from .apis import CountryData, CountryDataDate
from .auth import SignInApi


def initialize_routes(restServer):
    restServer.add_resource(SignInApi, '/api/v1.0/auth/signin')

    restServer.add_resource(CountryData, '/api/v1.0/country/<string:iso_code>')

    restServer.add_resource(CountryDataDate, '/api/v1.0/country/<string:iso_code>/<string:date>')
