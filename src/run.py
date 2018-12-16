from constants import *
from basic_model import BasicModel
from vgg_model_v2 import VGGModel2
from vgg_model import VGGModel
from yann_model import YannModel
from vgg_model_Benno import VGGModel_Benno
from preprocessing_helper import *
from postprocessing_helper import *

import os
import sys

# Set Train data Directory
data_dir = '../dataset/training/'

# Option 1: Load entire images

image_dir = data_dir + "images/"
files = os.listdir(image_dir)
n = len(files)
print("Loading " + str(n) + " images")
imgs = [load_image(image_dir + files[i]) for i in range(n)]
print(imgs[0][2])

gt_dir = data_dir + "groundtruth/"
print("Loading " + str(n) + " images")
gt_imgs = [load_image(gt_dir + files[i]) for i in range(n)]
print(files[0])

# Choose model
# model = YannModel()
#model = VGGModel2()
model = VGGModel_Benno()
# model = BasicModel()
# model = CNNModel()
# model = TeslaModelS()

# Option 2: Model loads files itself
model.load_data(image_dir, gt_dir, constants.TRAINING_SIZE)

# Train model
model.train(epochs=120, validation_split=0.1)

# Create Training set images
# Set directory to save images
prediction_training_dir = "predictions_training/"
model.generate_images(prediction_training_dir, image_dir)

# Predict Test Set -> Create submission and save Images
model.generate_submission()

# Save model
model.save()