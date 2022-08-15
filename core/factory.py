from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password



def authenticated(username, password):
	User = get_user_model()
	get_user = User.objects.filter(username=username).first()
	if get_user:
		user_password = get_user.password
		if check_password(password, user_password):
			return True

	return False

