import re
from rake_nltk import Rake
import nltk
import logging
# nltk.download('stopwords')
# nltk.download('punkt')


class TextToSentence(object):

	def __init__(self, text):
		self.text = re.sub(r"\.\.", ". ", text)
		logging.error(f"text --> {self.text}")

	def model(self):
		
		Model = Rake()
		
		return Model

	def text_to_sentence_list(self):
		output = self.model()._tokenize_text_to_sentences(self.text)
		return output



