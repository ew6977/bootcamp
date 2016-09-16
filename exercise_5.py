#Exercise 5

import numpy as np
# Our image processing tools
import skimage.filters
import skimage.io
import skimage.measure
import skimage.morphology
import skimage.segmentation
import segmentation_function as sf
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('dark')
from PIL import Image
import glob

#### 5.1 Growth curves from a movie

#load in the series of image_sub
filenames = glob.glob('data/bacterial_growth/*.tif')

image_list = []
for filename in filenames:
    im= skimage.io.imread(filename)
    image_list.append(im)

images_segmented=[]

for image in image_list:
    images_segmented.append(sf.image_segmentation(image, microscopy='fluoresence', blur_radius=50.0 , shape_pixels=3, image_distance= 0.0645, cutoff= 300))

#plot one representative to show that it worked

# Build RGB image by stacking grayscale images
image_0_rgb= np.dstack(3 * [image_list[0] / image_list[0].max()])

# Saturate red channel wherever there are white pixels in thresh image
image_0_rgb[images_segmented[0], 1] = 1.0

# Show the result
with sns.axes_style('dark'):
    plt.imshow(image_0_rgb)
