import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

batch_size = 32
img_size = (224, 224)


def make_train_dataset(path):
    train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        validation_split=0.1  # 10% for valid
    )

    train_generator = train_datagen.flow_from_directory(
        os.path.join(path, 'train'),
        target_size=img_size,
        batch_size=batch_size,
        class_mode='categorical',
        subset='training'
    )

    validation_generator = train_datagen.flow_from_directory(
        os.path.join(path, 'train'),
        target_size=img_size,
        batch_size=batch_size,
        class_mode='categorical',
        subset='validation'
    )

    return train_generator, validation_generator

def make_test_dataset(path):
    test_datagen = ImageDataGenerator(rescale=1./255)

    return test_datagen.flow_from_directory(
        os.path.join(path, 'test'),
        target_size=img_size,
        batch_size=batch_size,
        class_mode='categorical'
    )