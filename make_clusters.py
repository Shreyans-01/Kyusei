import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN

def pull_repo_key(repos):
	arr = []
	for file in [i for i in repos]:
		df = pd.read_csv('./repositories/'+file+'_response.csv', usecols=['id'])
		df = df.values
		df = df.flatten()
		df = [[file, i] for i in df]
		arr += df
	return np.array(arr)

def get_embeddings(feature_name, repos):
	embeds = None
	for file in ['./embeddings/'+feature_name+'/'+name+'_response.csv' for name in repos]:
		df = pd.read_csv(file)
		df = df.values
		if embeds is None:
			embeds = df
		else:
			embeds = np.concatenate((embeds, df), 0)
	return embeds

def compute_distance_matric(embeds):
	distance_matrix = np.zeros((embeds.shape[0], embeds.shape[0]))
	for i, embed_i in enumerate(embeds):
		for j, embed_j in enumerate(embeds):
			distance_matrix[i][j] = np.dot(embed_i, embed_j)/(np.linalg.norm(embed_i)*np.linalg.norm(embed_j))
	return distance_matrix

def pull_repos(repos):
	repo_keys = pull_repo_key(repos)
	distance_matrix = np.zeros((len(repo_keys), len(repo_keys)))
	for feature_name, weight in zip(['explanation', 'category_desc', 'category_name'], [0.2, 0.4, 0.4]):
		embeds = get_embeddings(feature_name, repos)
		distance_matrix_embed = compute_distance_matric(embeds)
		distance_matrix += distance_matrix_embed*weight
	return repo_keys, distance_matrix

def compute_clusters(repos):
	repo_keys, distance_matrix = pull_repos(repos)
	clustering = DBSCAN(eps=0.075, metric='precomputed')
	clustering.fit(distance_matrix)
	results = np.concatenate((repo_keys.T, [clustering.labels_]), 0)
	return results

if __name__ == '__main__':
	repos = ['bokeh', 'dash', 'rich', 'tqdm']
	print(compute_clusters(repos))