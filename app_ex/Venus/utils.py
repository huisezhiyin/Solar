from rest_framework.authentication import BasicAuthentication, SessionAuthentication


class SolarSessionAuthentication(SessionAuthentication):
    pass


class SolarTokenAuthentication(BasicAuthentication):
    pass
