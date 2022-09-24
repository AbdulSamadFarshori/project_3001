from api.models import JWTToken

def get_access_token():
	token = JWTToken.objects.get(id=1)
	access_token = token.access_token
	return access_token