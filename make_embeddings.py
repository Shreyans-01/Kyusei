import pandas as pd
import numpy as np
import os
import string
import re

def preprocess(string_inp):
	string_inp = ''.join([i if i.isalpha() else ' ' for i in string_inp])
	string_inp = re.sub("\s\s+" , " ", string_inp)
	return string_inp.lower().strip()

def get_vocab(feature_name):
	files = ['./repositories/'+i for i in os.listdir('./repositories/')]
	vocab = None
	for file in files:
		df = pd.read_csv(file, usecols=[feature_name])
		df = df.values
		df = df.flatten()
		if vocab is None:
			vocab = df
		else:
			vocab = np.concatenate((vocab, df))
	vocab, vocab_counts = np.unique(np.array(' '.join([preprocess(i) for i in vocab]).split()), return_counts=True)
	indexes = np.argsort(vocab_counts)
	vocab = vocab[indexes]
	vocab_counts = vocab_counts[indexes]
	return [i for i in vocab], [np.sqrt(i) for i in vocab_counts]

def make_embeds_for_feature(feature_name='explanation'):
	vocab, vocab_weights = get_vocab(feature_name)
	files = [i for i in os.listdir('./repositories/')]
	for file in files:
		df = pd.read_csv('./repositories/'+file, usecols=['id', feature_name])
		df = df.values
		ids, feature_extracts = df.T[0], df.T[1]
		ids = np.array([file[:-4]+str(i) for i in ids])
		embeddings = []
		for feature in feature_extracts:
			feature = preprocess(feature)
			feature = feature.split()
			embed = np.zeros(len(vocab))
			for word in feature:
				embed[vocab.index(word)] = 1
			embeddings.append(embed)
		embeddings = np.stack(embeddings)
		embeddings = pd.DataFrame(embeddings)
		embeddings.columns = vocab
		embeddings.to_csv('./embeddings/'+feature_name+'/'+file)

def make_embeds():
	for feature_name in ['explanation', 'category_desc', 'category_name']:
		if not os.path.exists('./embeddings/'+feature_name):
			os.mkdir('./embeddings/'+feature_name)
		make_embeds_for_feature(feature_name)

if __name__ == '__main__':
	make_embeds()