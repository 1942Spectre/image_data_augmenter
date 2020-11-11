from PIL import Image
import numpy as np



def resize(img,size):
	## Resize the given image to the given size without cropping

    img = img.resize(size)
    return img

def horizontal_flip(img):
	## Flip the image horizontally 
    img = img.transpose(Image.FLIP_LEFT_RIGHT)
    return img

def rotate(img , degrees):

	## Rotate the image in given degrees , negative degrees for right flip
    
    img = img.rotate(degrees)
    
    return img

def grayscale(img):

	return img.convert(mode="L")