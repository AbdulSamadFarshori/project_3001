from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password, make_password



def authenticated(username, password):
	User = get_user_model()
	get_user = User.objects.filter(username=username).first()
	if get_user:
		user_password = get_user.password
		if check_password(password, user_password):
			return True

	return False

def user_is_valid(username):
	User = get_user_model()
	get_user = User.objects.filter(username=username).first()
	if get_user:
		return True

	return False

def create_hash_key():
	strs = "23345"
	hash_key = make_password(strs)
	return hash_key

def make_hash(str):
	hash_key = make_password(strs)
	return hash_key

def create_user(username, email, password):
	User = get_user_model()
	user_obj = User(username=username, email=email, password=password)
	user_obj.save()
	return True



