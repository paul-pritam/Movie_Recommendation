import cv2
from tqdm import tqdm
import os
import shutil
from PIL import Image
# PycharmProjects/pythonProject1/extracted_images_mtcnn_pytorch/image_1024
dir_path = 'extracted_images_mtcnn_pytorch'
# dir = 'C:\Users\prita\PycharmProjects\pythonProject1\extracted_images_mtcnn_pytorch\'
# dir=''
new_dir = 'blurred'
for images in os.listdir(dir_path):
    # print(images)
    # img = Image.open(images)
    abs_path = os.path.abspath(images) 
    # img_path = os.path.join(abs_path, images)
    print(abs_path)
#     img = cv2.imread(abs_path)
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     fm = cv2.Laplacian(gray, cv2.CV_64F).var()
#     text = 'Not Blurry'
           
#     threshold = 100

#     if fm < threshold:
#             text = 'Blurry'
#             old_dir = dir + '_{}'.format(images)
#             shutil.move(old_dir,new_dir)
    