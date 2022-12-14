import numpy as np
import os
import PIL
import PIL.Image
import pathlib
import tensorflow as tf
import tensorflow_datasets as tfds
from keras.utils.vis_utils import plot_model
from matplotlib import pyplot as plt

credits = "https://www.tensorflow.org/api_docs/python/tf/keras/utils/plot_model" 
#for skeleton code and base algorithm

#print(tf.__version__)
dataset_url = "https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz"
data_dir = tf.keras.utils.get_file(origin=dataset_url,
                                   fname='flower_photos',
                                   untar=True)
data_dir = pathlib.Path(data_dir)

#some parameters for the loader
batch_size = 32
img_height = 180
img_width = 180

iteration_count = 3




def obtain_image_count(flower_name):
    image_count = len(list(data_dir.glob(flower_name+'/*.jpg')))
    return image_count

def display_image(flower_name):
    #error check flower_name input
    #valid flowers are: 
        #
    if (flower_name == 'roses' or flower_name == 'tulips' or flower_name == 'daisy' or flower_name == 'dandelion' or flower_name == 'sunflowers'):
        print("obtaining {} images\n".format(flower_name))
        flower = list(data_dir.glob(flower_name+'/*'))
        image = PIL.Image.open(str(flower[0]))
        image.show()
        image = PIL.Image.open(str(flower[1]))
        image.show()
    else:
        print("invalid flower name, please try again")
    return

def data_set_training():
    #using 80% of images for data 
    train_ds = tf.keras.utils.image_dataset_from_directory(
    data_dir,
    validation_split=0.2,
    subset="training",
    seed=123,
    image_size=(img_height, img_width),
    batch_size=batch_size)
    return train_ds

def data_set_validation():
    #using 20% of images for validation
    val_ds = tf.keras.utils.image_dataset_from_directory(
    data_dir,
    validation_split=0.2,
    subset="validation",
    seed=123,
    image_size=(img_height, img_width),
    batch_size=batch_size)
    return val_ds

def class_names(train_ds):
    class_names = train_ds.class_names
    print(class_names)
    return class_names

def vizualize_data(history):

    plt.plot(history.history['acc'])
    plt.plot(history.history['val_acc'])
    plt.title('model accuracy')
    plt.ylabel('accuracy')
    plt.xlabel('epoch')
    plt.legend(['train', 'val'], loc='upper left')
    plt.show()

    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('model loss')
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend(['train', 'val'], loc='upper left')
    plt.show()

def training_the_model(train_ds, val_ds):
    normalization_layer = tf.keras.layers.Rescaling(1./255)
    normalized_ds = train_ds.map(lambda x, y: (normalization_layer(x), y))
    image_batch, labels_batch = next(iter(normalized_ds))
    first_image = image_batch[0]
    # Notice the pixel values are now in `[0,1]`.
    print(np.min(first_image), np.max(first_image)) 

    AUTOTUNE = tf.data.AUTOTUNE

    train_ds = train_ds.cache().prefetch(buffer_size=AUTOTUNE)
    val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)

    #training the model
    num_classes = 5

    #Visual info
    model = tf.keras.Sequential([
    tf.keras.layers.Rescaling(1./255),
    tf.keras.layers.Conv2D(32, 3, activation='relu'),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Conv2D(32, 3, activation='relu'),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Conv2D(32, 3, activation='relu'),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(num_classes)
    ])

    #compile the data to analyze the loss to success rate of image validation
    model.compile(
        optimizer='adam',
        loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
        metrics=['accuracy'])

    #fit it to a standardized model
    data = model.fit(
        train_ds,
        validation_data=val_ds,
        epochs=iteration_count
        )

    #plot_model(model, to_file='model_plot.png', show_shapes=True, show_layer_names=True)

    return data


flower = input("what flower would you like to find?: ")
iteration_count = (int)(input("How many iterations for learning algorithm?: "))

count = obtain_image_count(flower)
display_image(flower)

print("There are {} {} images".format(count, flower))

training_set = data_set_training()
validation_set = data_set_validation()
classnames = class_names(training_set)
#vizualize_data(classnames, training_set, validation_set)
returned_data = training_the_model(training_set, validation_set)
vizualize_data(returned_data)