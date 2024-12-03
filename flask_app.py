# from flask import Flask, request, jsonify
# import numpy
# from PIL import Image
# from tensorflow.keras.preprocessing import image
# import tensorflow
# import os
# import io
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)

# model = tensorflow.keras.models.load_model(os.path.join('artifacts\\trained_model','model_v-03.h5'))


# @app.route('/predict', methods=['POST'])
# def pred():
#     if 'image' not in request.files:
#         return jsonify({'error': 'NO FILES PROVIDED'}), 400
    
#     file = request.files['image']

#     try:
#            # Read the image file as bytes
#         img_bytes = file.read()  # Raw bytes from the file
#         img = Image.open(io.BytesIO(img_bytes))  # Convert bytes to PIL image


#         # preprocessed_image = image.load_img(img, target_size = (256, 256))
#         # preprocessed_image = image.img_to_array(preprocessed_image)
#         # # print(preprocessed_image)
#         # img_array = numpy.expand_dims(preprocessed_image, axis= 0)

#         # prediction = model.predict(img_array)
#         # pred = 'Cat' if prediction[0] < 0.5 else 'Dog'
#         # print(pred)

#         prediction = "cat"
#         # return jsonify({'class': pred, 'confidence': float(prediction[0][0])})
#         return jsonify({"class": prediction}), 200




#     except Exception as e:
#         return jsonify({'error' : str(e)}, 500)    
    


# if __name__ == '__main__':
#     app.run(host= '0.0.0.0', port= 5000)
## ============= Code for testing using Postman

# ================== react code 

from flask import Flask, request, jsonify
from flask_cors import CORS
import tensorflow
import os
import numpy as np
from tensorflow.keras.preprocessing import image

from PIL import Image
import io

app = Flask(__name__)
CORS(app)

# Load your trained model
# model = tensorflow.keras.models.load_model(os.path.join('artifacts\\trained_model','model_v-03.h5'))
model = tensorflow.keras.models.load_model("artifacts\\trained_model\\model_v-03_cpy.h5")

@app.route('/predict', methods=['POST'])
def pred():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']

    try:
        # Process the image
        image = Image.open(file.stream).convert('RGB')
        image = image.resize((256, 256))  # Resize to match your model's input shape
        # image_array = np.array(image) / 255.0  # Normalize the image
        image_array = np.array(image) # no need to normalize 
        # if do normalize he output will different
        image_array = np.expand_dims(image_array, axis=0)  # Add batch dimension

        # Make prediction
        prediction = model.predict(image_array)
        print(prediction)
        print()
        print(prediction[0][0])
        # prediction output 2 dimension array [[0.5134971]]
        predicted_class = 'Cat' if prediction[0][0] < 0.5 else 'Dog'
        print(f"Predicted class: {predicted_class}")

        return jsonify({'class': predicted_class}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
