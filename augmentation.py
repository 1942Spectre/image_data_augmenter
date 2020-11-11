from PIL import Image
import numpy as np
from PIL import ImageFilter
import random
import skimage


def augment_horizontal_flip(imdata , labels):
    
    new_imdata = []
    new_labels = []
    
    for i in range(len(labels)):

        new_imdata.append(imdata[i]) ## Save the old image to the new set
        new_labels.append(labels[i])  ## Save the old label to the new set
        
        a = Image.fromarray(imdata[i])
        a = a.transpose(Image.FLIP_LEFT_RIGHT)
        a = np.asarray(a)
        

        new_imdata.append(a)
        new_labels.append(labels[i])


    new_imdata = np.array(new_imdata)
    new_labels = np.array(new_labels )
    return (new_imdata , new_labels)


def augment_blur(imdata , labels , radius = 2):
    ### Applies gaussian blur to an image and adds it to the dataset.

    new_imdata = []
    new_labels = []

    for i in range(len(labels)):

        new_imdata.append(imdata[i]) ## Save the old image to the new dataset
        new_labels.append(labels[i])

        a = Image.fromarray(imdata[i])
        a = a.filter(ImageFilter.GaussianBlur(radius = radius))
        a = np.asarray(a)

        new_imdata.append(a) ## Save the blurred image to the new dataset
        new_labels.append(labels[i]) ## Save the same label to the new dataset

    new_imdata = np.array(new_imdata)
    new_labels = np.array(new_labels)

    return (new_imdata , new_labels)


def augment_distort_color(imdata , labels , color_range , factor):

    ### augments new images by recoloring them within the color range.
    ### imdata is the image data numpy array
    ### labels is the labels of those images
    ### color range is a range like range(-20,20). applies a random choice from that range to every channel
    ### factor is the amount of augmented data. factor == 5 means you get 6 images for 1 image including the original image.

    new_imdata = []
    new_labels = []

    for i in range(len(imdata)):
        
        new_imdata.append(imdata[i]) ## Save the old image to the new dataset
        new_labels.append(labels[i])


            
        for x in range(factor):
            
            
            r = random.choice(color_range)
            g = random.choice(color_range)
            b = random.choice(color_range)

            new_img = imdata[i]

            if r >= 0:
                new_img[:,:,0] += r

            else:
                new_img[:,:,0] -= np.abs(r)

            if g >= 0:
                new_img[:,:,1] += g
            
            else:
                new_img[:,:,1] -= np.abs(g)

            if b>= 0:
                new_img[:,:,2] += b

            else:
                new_img[:,:,1] -= np.abs(b)

            new_imdata.append(new_img)
            new_labels.append(labels[i])
                

    new_imdata = np.array(new_imdata, dtype = "float32")
    new_labels = np.array(new_labels)

    return (new_imdata , new_labels)









