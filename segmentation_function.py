#Lesson 40: Write your own segmentation functions

def image_segmentation(image, blur_radius=50.0, shape, shape_pixels=3):
    """
    image segmentation(image_name, blur_radius=50, ):

    Corrects for uneven illumination.
    Corrects for "hot" or "bad" pixels in an image.
    Performs a thresholding operation.
    Removes bacteria or objects near/touching the image border.
    Removes objects that are too large (or too small) to be bacteria. Think carefully! For a multipurpose function, would you always want the same area cutoff?
    Removes improperly segmented cells.
    Returns a labeled segmentation mask.

    """

    #Correct for uneven illumniation
    #Blur the image
    im_blur = skimage.filters.gaussian(image, blur_radius)
    #Convert the original phase contrast image to a float
    phase_float = skimage.img_as_float(image)
    #Subtract the blurred image from the original image to correct for uneven illumination
    phase_sub = phase_float - im_blur

    #Correct for "hot" or "bad" pixels in an image
    #Generate a structural element.
    selem = skimage.morphology.shape(shape_pixels)


    #Now apply to the fluoresence image
    cfp_filt = skimage.filters.median(im_cfp, selem)




    #Apply otsu thresholding
    thresh = skimage.filters.threshold_otsu(phase_sub)
    seg = phase_sub < thresh
