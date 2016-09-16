
#Lesson 40: Write your own segmentation functions
import numpy as np
# Our image processing tools
import skimage.filters
import skimage.io
import skimage.measure
import skimage.morphology
import skimage.segmentation
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('dark')


def hotpixel_begone(image, shape_pixels):
    """
    Correct for "hot" or "bad" pixels in an image
    """
    #Generate a structural element.
    selem = skimage.morphology.square(shape_pixels)
    #Now apply to the image
    image_filt = skimage.filters.median(image, selem)
    return image_filt

def uneven_illumination(image_filt, image, blur_radius):
    """
    Blurs an image to be subtracted from original image to remove uneven illumination
    """
    #Blur the image
    im_blur = skimage.filters.gaussian(image_filt, blur_radius)
    #Convert the original phase contrast image to a float
    phase_float = skimage.img_as_float(image)
    #Subtract the blurred image from the original image to correct for uneven illumination
    image_sub = phase_float - im_blur
    return image_sub

def otsu_threshold(image_sub, microscopy='phase'):
        """
        Apply otsu thresholding
        """
        thresh = skimage.filters.threshold_otsu(image_sub)
        if microscopy is 'phase':
            seg = image_sub < thresh
        else:
            seg = image_sub > thresh
        return seg

def quant_segmented_regions(seg, image_distance, cutoff):
    #Label cells
    seg_lab, num_cells = skimage.measure.label(seg, return_num=True, background=0)

    #Compute the region properties and extract area of each object
    im_dist = image_distance #µm per pixel
    props = skimage.measure.regionprops(seg_lab)
    #Get the areas as an array
    areas = np.array([prop.area for prop in props])

    #make a copy of the labels segmentation mask and made it binary
    im_cells = np.copy(seg_lab) > 0

    for i, _ in enumerate(areas):
        if areas[i] < cutoff:
            im_cells[seg_lab == props[i].label] = 0

    area_filt_lab = skimage.measure.label(im_cells)
    return area_filt_lab

def image_segmentation(image,  blur_radius=50.0 , shape_pixels=3, microscopy='phase', image_distance= 0.063, cutoff= 300):

    """
    image segmentation(image_name, blur_radius=50, shape_pixels=3, image_distance= 0.063, cutoff= 300):

    Corrects for "hot" or "bad" pixels in an image.
    Corrects for uneven illumination.
    Performs a thresholding operation.
    Removes bacteria or objects near/touching the image border.
    Removes objects that are too large (or too small) to be bacteria. Think carefully! For a multipurpose function, would you always want the same area cutoff?
    Removes improperly segmented cells.
    Returns a labeled segmentation mask.

    """
    #Correct for "hot" or "bad" pixels in an image
    image_filt = hotpixel_begone(image, shape_pixels)

    #Correct for uneven illumniation
    image_sub = uneven_illumination(image, image_filt, blur_radius)

    #Apply otsu thresholding
    seg = otsu_threshold(image_sub)

    #segment
    area_filt_lab=quant_segmented_regions(seg, image_distance, cutoff)

    return area_filt_lab
