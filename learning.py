from PIL import Image
import os, glob
import numpy as np
# from sklearn import cross_validation
from sklearn import model_selection

classes = ["Japanese_castle","Europe_castle","Chinese_castle"]
num_classes = len(classes)
image_size = 50

# 画像の読み込み
X = []
Y = []
for index, classlabel in enumerate(classes):
    photos_dir = "castle/{}".format(classlabel)+"_images"
    files = glob.glob(photos_dir + "/*.jpg")
    for i, file in enumerate(files):
        if i >= 1000: break
        image = Image.open(file)
        image = image.convert("RGBA")
        image = image.resize((image_size, image_size))
        data = np.asarray(image)
        X.append(data)
        Y.append(index)

X = np.array(X)
Y = np.array(Y)

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, Y)
xy = (X_train, X_test, y_train, y_test)
np.save("./castle.npy", xy)