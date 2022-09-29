from rake_nltk import Rake
import nltk
nltk.download('stopword')
 nltk.download('punkt')

class TextToSentence(object):

	def __init__(self, text):

		self.text = text

	def model(self):
		
		Model = Rake()
		
		return Model

	def text_to_sentence_list(self):
		
		output = self.model()._tokenize_text_to_sentences(self.text)

		return output
