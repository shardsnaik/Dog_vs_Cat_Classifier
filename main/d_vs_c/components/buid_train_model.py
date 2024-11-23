import keras
import tensorflow as tf
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from keras import Sequential
from keras.callbacks import EarlyStopping 
from keras import regularizers
from keras.layers import Dense, Conv2D, MaxPooling2D, Flatten, BatchNormalization, Dropout
from main.d_vs_c import logger
import os

class Datasets:
    def __init__(self, config, params):
        self.config = config
        self.params = params

    def datasets_(self):
        train_ds = keras.utils.image_dataset_from_directory(
    directory = self.config['train_dir'],
    labels = 'inferred',
    label_mode = 'int',
    batch_size = self.params['batch_size'],
    seed = self.params['seed'],
    image_size = self.params['image_size']
)
        test_ds = keras.utils.image_dataset_from_directory(
    directory = self.config['test_dir'],
    labels = 'inferred',
    label_mode = 'int',
    batch_size = self.params['batch_size'],
    seed = self.params['seed'],
    image_size = self.params['image_size']
)
        return train_ds, test_ds
    

    # Normalixe the images
    @staticmethod
    def process(images, label):
        image = tf.image.resize(images, (256, 256))
        image = tf.image.convert_image_dtype(images, tf.float32)
        return images, label
    

    def model(self):
        model_3 = Sequential()
        
        model_3.add(Conv2D(self.params['conv_first_layer'], kernel_size=self.params['kernel_size'], padding='valid', activation='relu', input_shape=(self.params['input_shape'])))
        model_3.add(MaxPooling2D(pool_size=self.params['pool_size'], strides=self.params['strides'], padding='valid'))
        model_3.add(Dropout(self.params['dropout_rate']))
        
        model_3.add(Conv2D(self.params['conv_sec_layer'], kernel_size=self.params['kernel_size'], padding='valid', activation='relu'))
        model_3.add(MaxPooling2D(pool_size=self.params['pool_size'], strides=self.params['strides'], padding='valid'))
        model_3.add(Dropout(self.params['dropout_rate']))
        
        model_3.add(Conv2D(self.params['conv_third_layer'], kernel_size=self.params['kernel_size'], padding='valid', activation='relu'))
        model_3.add(MaxPooling2D(pool_size=self.params['pool_size'], strides=self.params['strides'], padding='valid'))
        model_3.add(Dropout(self.params['dropout_rate']))
        
        model_3.add(Conv2D(self.params['conv_fourth_layer'], kernel_size=self.params['kernel_size'], padding='valid', activation='relu'))
        model_3.add(MaxPooling2D(pool_size=self.params['pool_size'], strides=self.params['strides'], padding='valid'))
        model_3.add(Dropout(self.params['dropout_rate']))
        
        model_3.add(Flatten())
        
        model_3.add(Dense(self.params['dense_first_layer'], activation='relu', kernel_regularizer=regularizers.l2(self.params['l2_regularization'])))
        model_3.add(Dense(self.params['dense_second_layer'], activation='relu'))
        model_3.add(Dense(self.params['output_layer'], activation='sigmoid'))

         # Compile the model
        model_3.compile(optimizer=self.params['optimizer'], loss=self.params['loss'], metrics=['accuracy'])
        
        return model_3



    def run_model(self,model, train_ds, test_ds):
        early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)
        history_3 = model.fit(train_ds, epochs=self.params['epochs'], validation_data=test_ds, callbacks=[early_stopping])
        return history_3
    



class plot_nd_save:
    def __init__(self, config, params, history, model):
        self.config = config
        self.params = params
        self.history_3 = history
        self.model = model

    def plot_(self):
        logger.info('Plotting the graph of Loss and Val_Loss')
        plt.figure(figsize=(12, 6))
        plt.plot(self.history_3.history['loss'], label='Loss')
        plt.plot(self.history_3.history['val_loss'], label='Val Loss')
        plt.xlabel('Epochs')
        plt.ylabel('Loss')
        plt.legend()
        plt.show()

        logger.info('Plotting the graph of Accuracy and Val_Accuracy')
        plt.figure(figsize=(12, 6))
        plt.plot(self.history_3.history['accuracy'], label='Accuracy')
        plt.plot(self.history_3.history['val_accuracy'], label='Val Accuracy')
        plt.xlabel('Epochs')
        plt.ylabel('Accuracy')
        plt.legend()
        plt.show()


    def save_model(self):
        model_path = os.path.join(self.config['trained_model_path'], 'model_v-03.h5')
        self.model.save(model_path)
        logger.info(f"Model saved at {model_path}")

        
        model_weight = os.path.join(self.config['trained_model_path'], 'model_weights_v-03.weights.h5')
        self.model.save_weights(model_weight)
        logger.info(f"Model saved at {model_weight}")
        # self.model.save(os.path.join('self.config.trained_model_path','model_v-03.h5'))
