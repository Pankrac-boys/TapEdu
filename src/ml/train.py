import tensorflow as tf
import model
import pipeline

classifier = model.initialize_model()

data_path = '../../data'

train, valid = pipeline.make_train_dataset(data_path)
test = pipeline.make_train_dataset(data_path)

classifier.compile(loss = "categorical_crossentropy",
                   optimizer='rmsprop',
                   metrics=['accuracy']
    )
history = model.fit(train, epochs=25, steps_per_epoch=20, validation_data = valid, verbose = 1, validation_steps=3)
model.save("models/tapedu.h5")