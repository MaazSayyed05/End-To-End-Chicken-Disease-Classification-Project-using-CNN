
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

from chicken_disease_classification import logger

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename
        # name of image file given for prediction
    

    def predict(self) -> list:
        # load model
        model = load_model(os.path.join('artifacts/training','model.h5'))

        image_name = self.filename

        test_image = image.load_img(image_name, target_size=(224,224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)

        result = np.argmax(model.predict(test_image), axis=1)
        
        print(result)
        logger.info(f'Result: {result}')


        if result[0] == 0:
            prediction = 'Coccidiosis'
            logger.info(f'Predicted Class: {prediction}')
            return [{'image': prediction}]
        
        elif result[0] == 1:
            prediction = 'Healthy'
            logger.info(f'Predicted Class: {prediction}')
            return [{'image': prediction}]
        
        elif result[0] == 2:
            prediction = 'Salmo'
            logger.info(f'Predicted Class: {prediction}')
            return [{'image': prediction}]
    






