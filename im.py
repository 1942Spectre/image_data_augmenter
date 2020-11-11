import os
import random
import shutil as shell
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import image_toolkit



def train_test_split_from_dir(res_dir , target_dir , test_size ):
    
    ## Reads the directory and creates another directory that consists of train-test splitted classes.
    ## Test size must be a float and refers to the percentage of test samples. 
    ## Example train_test_split_from_dir(dir , target_dir , 0.1) splits the 10% of the data as test.
    
    
    
    
    if not res_dir.endswith("/"):
        res_dir = res_dir + "/"
        
    
    if not target_dir.endswith("/"):
        target_dir = target_dir + "/"
        
        
    os.mkdir(target_dir)
    
    
    train_dir = target_dir + "Train/" # Creating The Train Directory
    
    
    test_dir = target_dir + "Test/" # Creating The Test Directory
    
    os.mkdir(train_dir)
    
    os.mkdir(test_dir)
    
    
    classes = os.listdir(res_dir) ## Get The Classes
    
    
    for c in classes:
        
        
        
        
        
        train_dir = target_dir + "Train/" + c + "/" 
        
        test_dir = target_dir + "Test/" + c + "/"
        
        
        
        class_dir = res_dir + c + "/"
        
        
        os.mkdir(train_dir)
        
        os.mkdir(test_dir)
        
         
            
        resources = os.listdir(class_dir) # Get The Resource Names in Particular Class
        
        
        
          ### Get the exact number of test samples  
            
            
        if test_size is int:
            
            test_amount = test_size / len(classes)
          
        else:
            
            test_amount = int(test_size * len(resources)) # Get The number of resources for test
        
        
        
        ## Split the Data
        
        random.shuffle(resources)
        
        
        test = resources[:test_amount]
        
        train = resources[test_amount:]
        
        
        for resource in test:
            
            shell.copy(class_dir + resource , test_dir + resource)
            
        for resource in train:
            
            shell.copy(class_dir + resource , train_dir + resource)
        
        
        
        
        
def data_reader_from_dir(target_dir , target_shape , horizontal_flip = False ):
    
    ## Read image data from directory , returns x_train and y_train. Reads all the class folders automatically. 
    ## If the target_shape is two dimensional , reads the image as grayscale
    ## If the target_shape is three dimensional , reads it as rgb
    
    classes = os.listdir(target_dir)
    
    if len(target_shape) == 2:
        grayscale = True
    
    elif len(target_shape) == 3:
        grayscale = False
        
    else:
        raise(ValueError("Target Shape must have three or two dims."))
    
    
    data = []
    
    labels = []
    
    if not target_dir.endswith("/"):
        
        target_dir = target_dir + "/"
        
    for c in classes:
        
        class_dir = target_dir + "/" + c + "/"
        
        class_resources = os.listdir(class_dir)
        
        for resource in class_resources:
            
           
            x = Image.open(class_dir + resource)


            x = image_toolkit.resize(x , (target_shape[0],target_shape[1])) 

            if grayscale:

                x = (np.asarray(image_toolkit.grayscale(x)).reshape((target_shape[0],target_shape[1],1))) 
                
                if horizontal_flip == True:
                    
                    x = Image.fromarray(x)
                    
                    data.append((np.asarray(image_toolkit.horizontal_flip(x))))
                    labels.append(classes.index(c))
                
                
                data.append((np.asarray(x)* 1/255))
                labels.append(classes.index(c))
            
            else:
                
                x = (np.asarray(x).reshape(target_shape[0],target_shape[1],target_shape[2]))

                if horizontal_flip == True:
                    
                    x = Image.fromarray(x)

                    data.append((np.asarray(image_toolkit.horizontal_flip(x))))
            
                    labels.append(classes.index(c))

                data.append((np.asarray(x)))
                labels.append(classes.index(c))

            
    
    
    temp_list =  [i for i in range(len(labels))]
    
    random.shuffle(temp_list)
    
    new_labels , new_data = [] , []
    
    for i in temp_list:
        
        new_labels.append(labels[i])
        new_data.append(data[i])
        
    new_data = np.array(new_data)
    new_labels = np.array(new_labels)

        
    return (new_data , new_labels)