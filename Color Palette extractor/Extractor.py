from PIL import Image
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt


def extractor(image_path, num_colors=5):
    image = Image.open(image_path)
    image = image.resize((100, 100))  
    pixels = np.array(image).reshape(-1, 3)
    kmeans = KMeans(n_clusters=num_colors)
    kmeans.fit(pixels)
    palette = kmeans.cluster_centers_.astype(int)
    return palette


def display(palette):
    fig, ax = plt.subplots(1, len(palette), figsize=(12, 4), subplot_kw=dict(xticks=[], yticks=[]))
    for sp, color in zip(ax, palette):
        sp.imshow([[color / 255.0]])  
        sp.set_title(f'RGB: {color}', fontsize=10)
    plt.show()


path = input("Enter the path to the image file: ").strip()
count = int(input("Enter the number of colors to extract (e.g., 5): ").strip())    
palette = extractor(path, count)

print("Extracted Palette RGB Values:")
for color in palette:
    print(color)
    
display(palette)
