import re
from rake_nltk import Rake
import nltk
nltk.download('stopwords')
nltk.download('punkt')



class TextToSentence(object):

	def __init__(self, text):
		self.text = text

	def model(self):
		
		Model = Rake()
		
		return Model

	def remove_stops(self):
		words = []
		for st in self.text:
			word = st
			stops = 0
			for ex_st in st:
				if ex_st == ".":
					stops += 1
			if stops > 1:
				word = '. '
			words.append(word)
		text = " ".join(words)
		return text

	def text_to_sentence_list(self):
		
		output = self.model()._tokenize_text_to_sentences(self.remove_stops)

		return output

