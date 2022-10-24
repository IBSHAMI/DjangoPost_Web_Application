from rest_framework.authentication import TokenAuthentication as BaseTokenAuthentication


# Overwrite the base token authentication class
class TokenAuthentication(BaseTokenAuthentication):
    keyword = 'Bearer'
