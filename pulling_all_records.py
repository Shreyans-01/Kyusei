import pandas as pd
import numpy as np
import os
import requests
from tqdm import tqdm

URL = ""

def get_response(url="https://dev-api.metabob.com/repository/88/analysis?include=problems%2Cstats"):
	response = requests.get(url)
	a = response.json()
	return a

def get_all_repos(url="https://dev-api.metabob.com/repositories/?current_page=0&page_size=100"):
	repos = get_response(url)
	keys_arr = list(repos[0].keys())
	df = {key:[] for key in keys_arr}
	for repo in repos:
		for key, item in repo.items():
			df[key].append(item)
	df = pd.DataFrame(df)
	df.to_csv("respositories.csv", index=False)

def record_repositories():
	if not os.path.exists('./repositories/'):
		os.mkdir('./repositories/')
	df = pd.read_csv("respositories.csv", usecols=['id', 'name'])
	df = df.values
	for index, (id_item, name_item) in tqdm(enumerate(zip(df.T[0], df.T[1])), total=len(df.T[0]), desc='Scraping'):
		if not os.path.exists('./repositories/'+name_item+'_response.csv'):
			try:
				repo_response = get_response("https://dev-api.metabob.com/repository/"+str(id_item)+"/analysis?include=problems%2Cstats")
				problems = repo_response['problems']
				problems_arr = []
				for problem in problems:
					problems_arr.append({'id': problem['id'], 'location': problem['location'], 'lineno': problem['lineno'], 'end_lineno': problem['end_lineno'], 'category_id': problem['category']['id'], 'category_name': problem['category']['name'], 'category_desc': problem['category']['description'], 'explanation': problem['explanation']})
			except:
				pass
			problems_df = {key:[] for key in list(problems_arr[0].keys())}
			for problem in problems_arr:
				for key in list(problems_arr[0].keys()):
					problems_df[key].append(problem[key])
			problems_df = pd.DataFrame(problems_df)
			problems_df.to_csv('./repositories/'+name_item+'_response.csv', index=False)

if __name__ == '__main__':
	if not os.path.exists('./repositories.csv'):
		get_all_repos()
	record_repositories()