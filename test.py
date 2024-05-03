from keras.models import Sequential
from keras.layers import Dense, Flatten, Conv2D, MaxPooling2D
import os
from PIL import Image
import numpy

picture_path = r"E:\毕设\人脸数据集\LFW（Labeled Faces in the Wild）人像图像数据集\LFW（Labeled Faces in the Wild）人像图像数据集\lfw"
suffix = ".bmp"
num_people = 15
num_train = 6
num_picture_single = 11
dimension = [80, 100]
x_train = []
y_train = []
x_test = []
y_test = []
picture_file = [file for file in os.listdir(picture_path) if file.endswith(suffix)]
num_picture = len(picture_file)
for i in range(num_picture):
    picture = list(Image.open(picture_path + '\\' + picture_file[i]).getdata())
    y = [0] * num_people
    y[i // num_picture_single] = 1
    if i % num_picture_single < num_train:
        x_train.append(picture)
        y_train.append(y)
    else:
        x_test.append(picture)
        y_test.append(y)
x_train, x_test, y_train, y_test = numpy.array(x_train), numpy.array(x_test), numpy.array(y_train), numpy.array(y_test)

x_train = x_train.reshape(x_train.shape[0], dimension[0], dimension[1], 1).astype('float32') / 255
x_test = x_test.reshape(x_test.shape[0], dimension[0], dimension[1], 1).astype('float32') / 255

model = Sequential()
model.add(Conv2D(filters=4, kernel_size=(3, 3), activation='relu', input_shape=(dimension[0], dimension[1], 1)))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(num_people, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

history = model.fit(x_train, y_train, batch_size=128, epochs=20, verbose=1, validation_data=(x_test, y_test))

score = model.evaluate(x_test, y_test, verbose=0)
print('Test accuracy:', score[1])