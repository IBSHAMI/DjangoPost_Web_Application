from rest_framework.authentication import TokenAuthentication as BaseTokenAuthentication
from djoser.serializers import UserSerializer


# Overwrite the base token authentication class
class TokenAuthentication(BaseTokenAuthentication):
    keyword = 'Bearer'
