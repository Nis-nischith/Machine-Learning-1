import pandas as pd
import numpy as np
import tensorflow as tf
import keras
from keras.models import Model
from keras.layers import Input
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers import Conv2D
from keras.layers import MaxPooling2D, ReLU, Dropout
from keras.optimizers.legacy import Adam
from keras.preprocessing.image import ImageDataGenerator


batch_size = 32
EPOCHS = 10
NUM_CLASSES = 26
image_size = (28, 28, 1)
droupout_rate = 0.2

# building model
inputs = Input(shape= image_size)
conv1 = Conv2D(filters=32, kernel_size=(3, 3), strides=1)(inputs)
relu1 = ReLU()(conv1)
conv2 = Conv2D(filters=64, kernel_size=(3, 3), strides=1)(relu1)
relu2 = ReLU()(conv2)
mxpool = MaxPooling2D(pool_size=(2, 2))(relu2)
flatten = Flatten()(mxpool)
dense = Dense(128, activation='relu')(flatten)
dropout = Dropout(droupout_rate)(dense)
outputs = Dense(NUM_CLASSES, activation='softmax')(dropout)
model = Model(inputs=inputs, outputs=outputs)

# defining dataset size
dataset = 27455
# defining the dataset split
train_ratio = 0.7
test_ratio = 0.3

# reading csv file
data = pd.read_csv('path/to/your/csv/file.csv')

# extracting pixel values and class number
pixels = data.iloc[ 1:, -784: ].values
class_numbers = data.iloc[ 1:, 0].values

# converting pixel values to numpy array and reshaping
pixels = np.array(pixels, dtype='float32').reshape(-1, 28, 28, 1)

# converting class numbers to one-hot encoded labels
class_labels = keras.utils.to_categorical(class_numbers, NUM_CLASSES)

# creating train and validation data
train_data = pixels[: int(train_ratio * dataset)]
train_labels = class_labels[: int(train_ratio * dataset)]
val_data = pixels[int(train_ratio * dataset): ]
val_labels = class_labels[int(train_ratio * dataset): ]

# creating train generator
train_datagen = ImageDataGenerator(rescale=1./255)
train_generator = train_datagen.flow(
    x=train_data,
    y=train_labels,
    batch_size=batch_size)

# creating validation generator
val_datagen = ImageDataGenerator(rescale=1./255)
test_data = val_datagen.flow(
    x=val_data,
    y=val_labels,
    batch_size=batch_size)

# compiling model
opt = Adam(learning_rate=0.001)
model.compile( optimizer=opt, loss="categorical_crossentropy", metrics=['accuracy'])
model.fit(
    train_generator,
    epochs= EPOCHS,
    validation_data=test_data)
