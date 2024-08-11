import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import keras
import sys, os


print(tf.__version__)

from keras.datasets import mnist

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# train_images의 shape를 출력합니다.
print(train_images.shape)  # (60000, 28, 28)이 출력됩니다.
# train_labels의 첫 10개를 출력합니다.
print(train_labels[:10])  # [5 0 4 1 9 2 1 3 1 4]와 같이 출력됩
