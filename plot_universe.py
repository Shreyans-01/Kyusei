import matplotlib.pyplot as plt
import numpy as np
import cv2

def generate_galaxies(results_clusters):
	labels = np.array([int(i) for i in results_clusters.T[-1]])
	cluster_labels, counts = np.unique(labels, return_counts=True)
	indexes = np.argsort(counts)[::-1]
	counts = counts[indexes]
	cluster_labels = cluster_labels[indexes]
	points_arr = []
	base_angle = np.pi*np.random.random()
	centroid_arr = []
	for i_enum, label in enumerate(cluster_labels):
		indexes = np.argwhere(labels==label).flatten()
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
	return points_arr, centroid_arr

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

def plot_stars(points_arr, centroid_arr, N=6):
	# plt.axis('off')
	# for points in points_arr:
	# 	plt.scatter(points.T[0], points.T[1], color='black', marker=(5, 1))
	# plt.savefig('stars.png', bbox_inches='tight')
	# image = cv2.imread('stars.png')
	# image_blur = cv2.blur(image, (7, 7))
	# image = 255 - image
	# image_blur = 255 - image_blur
	# image = image + image_blur
	# background = cv2.imread("galaxy.jpg")
	# background = cv2.resize(background, (image.shape[1], image.shape[0]))
	# background = change_brightness(background, -50)
	# #background += image
	# cv2.imwrite('stars.png', background)
	plt.rcParams["figure.autolayout"] = True
	im = plt.imread("galaxy.png")
	fig, ax = plt.subplots()
	im = ax.imshow(im, extent=[0, 515, 0, 389])
	for points in points_arr:
		ax.scatter(points.T[0]*int(515*0.4)+515//2, points.T[1]*int(389*0.4)+389//2, color='white', marker=(5, 1))
	ax.axis('off')
	plt.savefig('stars.png', bbox_inches='tight')


if __name__ == '__main__':
	from make_clusters import compute_clusters
	results_clusters = compute_clusters(['bokeh', 'dash', 'rich', 'tqdm'])
	points_arr, centroid_arr = generate_galaxies(results_clusters)
	plot_stars(points_arr, centroid_arr)