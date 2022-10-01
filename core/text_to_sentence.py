import re
from rake_nltk import Rake
import nltk
nltk.download('stopwords')
nltk.download('punkt')



class TextToSentence(object):

	def __init__(self, text):
		text = re.sub(r"..", ".", text)
		text = re.sub(r"...", ".", text)
		text = re.sub(r"....", ".", text)
		text = re.sub(r".....", ".", text)
		self.text = text

	def model(self):
		
		Model = Rake()
		
		return Model

	def text_to_sentence_list(self):
		
		output = self.model()._tokenize_text_to_sentences(self.text)

		return output

