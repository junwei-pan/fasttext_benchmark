import csv
import string
import numpy as np
from keras.utils.np_utils import to_categorical

def delete_punctuation(s):
	out = s.lower().translate(string.maketrans("",""), string.punctuation)
	return out

def split_string(s):
	lst_word = []
	for word in delete_punctuation(s).split(" "):
		lst_word.append(word)
	return lst_word

class util:

	def __init__(self):
		self.d_word_count = {}
		self.d_word_index = {}

	def build_vocab(self, path, max_features=20000, threshold=0):
		index = 0
		for row in csv.reader(open(path)):
			title = row[1]
			description = row[2]

			for word in split_string(title):
				self.d_word_count.setdefault(word, 0)
				self.d_word_count[word] += 1

			for word in split_string(description):
				self.d_word_count.setdefault(word, 0)
				self.d_word_count[word] += 1
		self.d_word_count
		sort = sorted(self.d_word_count.iteritems(), key = lambda x:x[1], reverse = True)
		for item in sort[:max_features]:
			word = item[0]
			if not word or word == "":
				continue
			if self.d_word_count[word] >= threshold:
				self.d_word_index[word] = index
				index = index + 1

	def vectorize(self, path, _title = True, _description = True):
		'''
		Convert the text to a list of faeture and a list of label
		'''		
		lst_fea = []	
		lst_label = []
		lst_fea_raw = []
		for row in csv.reader(open(path)):
			label = int(row[0])
			lst_label.append(label)
			title = row[1]
			description = row[2]
			lst = []
			Set = set()
			lst_raw = []
			if _title:
				for word in split_string(title):
					if self.d_word_index.has_key(word):
						if not word in Set:
							lst.append(self.d_word_index[word])
							lst_raw.append(word)
							Set.add(word)
			if _description:
				for word in split_string(description):
					if self.d_word_index.has_key(word):
						if not word in Set:
							lst.append(self.d_word_index[word])
							lst_raw.append(word)
							Set.add(word)
			lst_fea.append(lst)
			lst_fea_raw.append(lst_raw)
		return np.array(lst_fea), to_categorical(np.array(lst_label)), lst_fea_raw


