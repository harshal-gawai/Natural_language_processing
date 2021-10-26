from util import *

# Add your import statements here
from nltk.stem import WordNetLemmatizer



class InflectionReduction:

	def reduce(self, text):
		"""
		Stemming/Lemmatization

		Parameters
		----------
		arg1 : list
			A list of lists where each sub-list a sequence of tokens
			representing a sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of
			stemmed/lemmatized tokens representing a sentence
		"""

		reducedText = None

		#Fill in code here
		lemmatizer = WordNetLemmatizer()

		reducedText = []

		for sentence in text:
			lemmatize_sentence = []
			for token in sentence:
				token_lemm = lemmatizer.lemmatize(token)
				lemmatize_sentence.append(token_lemm)

			reducedText.append(lemmatize_sentence)

		return reducedText

