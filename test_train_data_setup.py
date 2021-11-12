# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 10:49:11 2021

@author: mulla
"""

#Importing OS module to traverse the images directory.
import os

#Path of the images directory
images_path='100-dataset'

#Change the working directory to the image directory
os.chdir(images_path)

#List where all the images are stored.
images_list = []


#Traversing all the images in the directory with os.walk
for curr_dir, directory, images in os.walk('.'):
    for files in images:
        if files.endswith('.jpeg') or files.endswith('.jpg'):
                save_to_file = images_path+'/'+files
                images_list.append(save_to_file+'\n')
                
###Creating test and train data

images_test = images_list[:int(len(images_list)*0.15)]

images_train = images_list[int(len(images_list)*0.15):]


####Saving these lists to text docs.
                
with open('train_images.txt','w') as train_images:
    for images in images_train:
        train_images.write(images)
        

with open('test_images.txt','w') as test_images:
    for images in images_test:
        test_images.write(images)



