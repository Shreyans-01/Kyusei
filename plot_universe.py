import matplotlib.pyplot as plt
import numpy as np
import cv2
import seaborn as sns
import matplotlib.patches as mpatches

def generate_galaxies(results_clusters, base_angle=True, seed=0):
	np.random.seed(seed)
	labels = np.array([int(i) for i in results_clusters.T[-1]])
	cluster_labels, counts = np.unique(labels, return_counts=True)
	indexes = np.argsort(counts)[::-1]
	counts = counts[indexes]
	cluster_labels = cluster_labels[indexes]
	points_arr = []
	centroid_arr = []
	keys_arr = []
	if base_angle==True:
		base_angle = np.pi*np.random.random()
	for i_enum, label in enumerate(cluster_labels):
		indexes = np.argwhere(labels==label).flatten()
		keys = results_clusters[indexes]
		points = np.random.normal(loc=0.0, scale=np.random.random()*0.08+0.07, size=(len(indexes), 2))
		for i in range(len(points)):
			for j in range(len(points[0])):
				if points[i][j] > 0.2:
					points[i][j] = 0.2+np.random.random()*0.04
				elif points[i][j] < -0.2:
					points[i][j] = -0.2-np.random.random()*0.04
		if i_enum!=0:
			angle = (i_enum-1)*2*np.pi/(len(cluster_labels)-1)+base_angle
			centroid = [np.sin(angle), np.cos(angle)]
			points = points + centroid
		else:
			centroid = [0, 0]
		centroid_arr.append(centroid)
		points_arr.append(points)
		keys_arr.append(keys)
	return points_arr, centroid_arr, keys_arr

def scale_img(img, scale_percent=0.5):
	width = int(img.shape[1] * scale_percent)
	height = int(img.shape[0] * scale_percent)
	dim = (width, height)
	return cv2.resize(img, dim)

def change_brightness(img, value=30):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    v = cv2.add(v,value)
    v[v > 255] = 255
    v[v < 0] = 0
    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img

def plot_stars(points_arr, centroid_arr, keys_arr, repos, N=6):
	clrs = sns.color_palette('husl', n_colors=len(repos))
	plt.rcParams["figure.autolayout"] = True
	plt.rcParams["figure.figsize"] = (11,11)
	im = plt.imread("galaxy.png")
	fig, ax = plt.subplots()
	im = ax.imshow(im, extent=[0, 515, 0, 389])
	for points, keys in zip(points_arr, keys_arr):
		points.T[0] = points.T[0]*int(515*0.4)+515//2
		points.T[1] = points.T[1]*int(389*0.4)+389//2
		for key, point_x, point_y in zip(keys.T[0], points.T[0], points.T[1]):
			ax.scatter(point_x, point_y, color=clrs[repos.index(key)], marker=(5, 1))
	ax.axis('off')
	labels = [mpatches.Patch(color=clrs[repos.index(key)], label=key) for key in repos]
	plt.legend(handles=labels)
	plt.savefig('stars.png', bbox_inches='tight')


if __name__ == '__main__':
	from make_clusters import compute_clusters
	repos = ['bokeh', 'dash', 'rich', 'tqdm']
	results_clusters = compute_clusters(repos)
	points_arr, centroid_arr, keys_arr = generate_galaxies(results_clusters)
	plot_stars(points_arr, centroid_arr, keys_arr, repos)