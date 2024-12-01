import os
import numpy
import tensorflow
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

class Prediction:
    def __init__(self, image):
        self.image = image 


    def predict(self):
        img = self.image

        model = load_model("C:\\Users\\Admin\\Downloads\\model_v-03.h5")
        # preprocessing the image before feed into model

        preprocessed_image = image.load_img(img, target_size = (256, 256))
        preprocessed_image = image.img_to_array(preprocessed_image)
        # print(preprocessed_image)
        pre_img = numpy.expand_dims(preprocessed_image, axis= 0)
        # print(pre_img)
        # prediction = numpy.argmax(model.predict(pre_img), axis=1)
        prediction =model.predict(pre_img)
        print(prediction)
        predicted_class = 'Cat' if prediction[0][0] < 0.5 else 'Dog'
        print(predicted_class)
        # if prediction == 0:
        #     print('The Image Contain Cat')
            
        # else: print('The Image Contain Dog')

obj = Prediction("C:\\Users\\Admin\\Downloads\\c.jpg")
obj.predict()
