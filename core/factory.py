from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password, make_password
import logging
import re
from spellchecker import SpellChecker

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

def make_hash(strs):
	hash_key = make_password(strs)
	return hash_key

def create_user(username, email, password):
	User = get_user_model()
	user_obj = User(username=username, email=email, password=password)
	user_obj.save()
	return True

def get_client_ip(meta_data):
	ip= ""
	httpx = meta_data.get('HTTP_X_FORWARDED_FOR')
	if httpx:
		ip = httpx.split(',')[0]
	else:
		ip = meta_data.get('REMOTE_ADDR')
	return ip

def unknown_words(text):
	spell = SpellChecker()
	unknown_spelling = spell.unknown(text)
	return unknown_spelling


def clean_text(text):
	text = text.lower()
	text = re.sub(r"’", "'", text)
	text = re.sub(r"\r\n", " ", text)
	text = re.sub(r"&#39;", "'", text)
	text = re.sub(r"&#180;","'", text)
	text = re.sub(r"thru", "through", text)
	text = re.sub(r"\t i am e", "time", text)
	text = re.sub(r"t i am e", "time", text)
	text = re.sub(r"a&e", "accident and emergency", text)
	text = re.sub(r"i'm", "i am", text)
	text = re.sub(r" im ", " i am ", text)
	text = re.sub(r"he's", "he is", text)
	text = re.sub(r"hes", "he is", text)
	text = re.sub(r"she’s", "she will", text)
	text = re.sub(r"that's", "that is", text)
	text = re.sub(r"what's", "what is", text)
	text = re.sub(r"why's", "why is", text)
	text = re.sub(r"where's", "where is", text)
	text = re.sub(r"\'ll", " will ", text)
	text = re.sub(r" ill ", " i will ", text)
	text = re.sub(r"\'d", " would", text)
	text = re.sub(r" idk ", " i don not know ", text)
	text = re.sub(r" ive ", " i have ", text)
	text = re.sub(r"\'ve", " have", text)
	text = re.sub(r"\'re", " are", text)
	text = re.sub(r"haven't", "have not", text)
	text = re.sub(r"havent", "have not", text)
	text = re.sub(r"can't", "can not", text)
	text = re.sub(r"cant", "can not", text)
	text = re.sub(r"won't", "will not", text)
	text = re.sub(r"wont", "will not", text)
	text = re.sub(r"aren't", "are not", text)
	text = re.sub(r"arent", "are not", text)
	text = re.sub(r"isn't", "is not", text)
	text = re.sub(r" isnt ", "is not", text)
	text = re.sub(r"doesn't", "does not", text)
	text = re.sub(r"doesnt", "does not", text)
	text = re.sub(r"don't", "do not", text)
	text = re.sub(r"dont", "do not", text)
	text = re.sub(r"didn't", "did not", text)
	text = re.sub(r"didnt", "did not", text)
	text = re.sub(r"shouldn't", "should not", text)
	text = re.sub(r"shouldnt", "should not", text)
	text = re.sub(r"wouldn't", "would not", text)
	text = re.sub(r"wouldnt", "would not", text)
	text = re.sub(r"couldn't", "could not", text)
	text = re.sub(r"couldnt", "could not", text)
	text = re.sub(r"it's", "it is", text)
	text = re.sub(r"wasn't", "was not", text)
	text = re.sub(r" iwas ", "i was", text)
	text = re.sub(r" wasnt ", "was not", text)
	text = re.sub(r"who's", "who is", text)
	text = re.sub(r" whos ", "who is", text)
	text = re.sub(r"youso", "you so", text)
	text = re.sub(r"dr's", "doctors", text)
	text = re.sub(r" eart ", " heart ", text)
	text = re.sub(r"&quot;", "", text)
	text = re.sub(r"&#160;", "", text)
	text = re.sub(r"\r\n\r\n", " ", text)
	text = re.sub(r"\(", "", text)
	text = re.sub(r"\)", "", text)
	text = re.sub(r"\?", "", text)
	text = re.sub(r"\.", "", text)
	text = re.sub(r"\, ", " ", text)
	text = re.sub(r",", " ", text)
	text = re.sub(r"! ", "", text)
	text = re.sub(r"!", "", text)
	text = re.sub(r" ! ", " ", text)
	text = re.sub(r"\'", "", text)
	text = re.sub(r"\*", "", text)
	text = re.sub(r"  ", " ", text)
	text = re.sub(r" -- ", " ", text)
	text = re.sub(r"\-", " ", text)
	text = re.sub('"', "", text)
	text = re.sub(r'\/', "", text)
	text = re.sub(r'\xa0', "", text)
	text = re.sub(r'i;m', "i am", text)
	text = re.sub(r" <p>", " ", text)
	text = re.sub(r"<p>", " ", text)
	text = re.sub(r"<p> ", "", text)
	text = re.sub(r": ", " ", text)
	text = re.sub(r"[b]", "", text)
	text = re.sub(r"i`m", "i am", text)
	return text




