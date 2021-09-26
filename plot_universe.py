import matplotlib.pyplot as plt
import numpy as np
import cv2

def generate_galaxies(results_clusters):
	print(results_clusters)

if __name__ == '__main__':
	from make_clusters import compute_clusters
	results_clusters = compute_clusters(['bokeh', 'dash', 'rich', 'tqdm'])
	generate_galaxies(results_clusters)