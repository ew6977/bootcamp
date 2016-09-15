#Lesson 38: Introduction to image processing
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
# For image processing
import skimage.io
import skimage.exposure
import skimage.morphology
import skimage.filters

#Load images
im_phase = skimage.io.imread('../data/bsub_100x_phase.tif')
im_cfp = skimage.io.imread('../data/bsub_100x_cfp.tif')

#An 8 bit image can have 2^8 =256 (0-255)
#The photo we are working with was taken as 12 bit... but the computer
#assumes that it is either 8 bit or 16 bit... so we have to fix this

#Show the phase image (DON'T EVER USE cm.jet)
# plt.imshow(im_phase)

# plt.imshow(im_phase, cmap=plt.cm.viridis)

#Plot the histogram of the phase image
plt.close()
hist_phase, bins_phase = skimage.exposure.histogram(im_phase)
plt.plot(bins_phase, hist_phase)
plt.xlabel('pixel value')
plt.ylabel('count')
plt.show()
plt.close()

#Apply a threshold to our image
thresh = 300
im_phase_thresh = im_phase < thresh


#Seaborn getting rid of white grid lines
with sns.axes_style('dark'):
    plt.imshow(im_phase_thresh, cmap=plt.cm.Greys_r)
    plt.show()
    plt.close()

#Take a look at the fluoresence image
with sns.axes_style('dark'):
    plt.imshow(im_cfp, cmap= plt.cm.viridis)
    plt.show()
    plt.close()

#There is a bright ("hot") pixel that is actually bringing down the brigtness of the cells

#Code to pick out the bright spot
with sns.axes_style('dark'):
    plt.imshow(im_cfp[150:250, 450:550] / im_cfp.max(), cmap=plt.cm.viridis)
    plt.show()
    plt.close()

#Generate a structural element.
selem = skimage.morphology.square(3)


#Now apply to the fluoresence image
cfp_filt = skimage.filters.median(im_cfp, selem)

with sns.axes_style('dark'):
    plt.imshow(cfp_filt, cmap=plt.cm.viridis)
    plt.show()
    plt.close()

#Look at the histogram of the median filtered image
cfp_hist, cfp_bins = skimage.exposure.histogram(cfp_filt)
plt.plot(cfp_bins, cfp_hist)
plt.xlabel('pixel value')
plt.ylabel('counts')
plt.show()
plt.close()

#Threshold our fluoresence image
cfp_thresh = cfp_filt > 120
with sns.axes_style('dark'):
    plt.imshow(cfp_thresh, cmap=plt.cm.Greys_r)
    plt.show()
    plt.close()

#Apply an otsu threshold
phase_thresh = skimage.filters.threshold_otsu(im_phase)
cfp_thresh = skimage.filters.threshold_otsu(cfp_filt)
phase_otsu = im_phase < phase_thresh
cfp_otsu = cfp_filt > cfp_thresh

with sns.axes_style('dark'):
    plt.figure()
    plt.imshow(phase_otsu, cmap=plt.cm.Greys_r)
    plt.title('phase otsu')

    plt.figure()
    plt.imshow(cfp_otsu, cmap = plt.cm.Greys_r)
    plt.title ('cfp otsu')
