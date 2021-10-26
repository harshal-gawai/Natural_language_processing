from util import *

# Add your import statements here
from nltk.corpus import stopwords




class StopwordRemoval():

	def fromList(self, text):
		"""
		Sentence Segmentation using the Punkt Tokenizer

		Parameters
		----------
		arg1 : list
			A list of lists where each sub-list is a sequence of tokens
			representing a sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
			representing a sentence with stopwords removed
		"""

		stopwordRemovedText = None

		#Fill in code here
		stopwords_ = set(stopwords.words('english'))

		stopwordRemovedText = []

		for sentence in text:
			reduced = []
			for token in sentence:
				if not token in stopwords_:
					reduced.append(token)

			stopwordRemovedText.append(reduced)


		return stopwordRemovedText


