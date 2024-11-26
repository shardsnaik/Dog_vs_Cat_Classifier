import os
import cv2
import tensorflow as tf
from main.d_vs_c import logger

class Pre_process_img:

    def __init__(self, config):
        self.config = config
        self.list = []
        self.image_categories = self.config['image_categories']


    # def check_channel(self, file_path):
    #     img = tf.io.read_file(file_path)
    #     try:
    #         img = tf.image.decode_image(img, channels=3)  # Decode with 3 channels (RGB)
    #         img = tf.image.convert_image_dtype(img, tf.float32)  # Convert to [0,1]
    #     except tf.errors.InvalidArgumentError:
    #         print(f"Skipping file {file_path} due to unexpected channels.")
    #         img_num = file_path.split('/')[-1].split('.')[0]
    #         print(f" image number:-  {img_num}" )
    #         self.list.append(img_num)
    #         return None
    #     return img

    def check_channel(self, file_path):
        # try:
        #     # Read the image
        #     img = cv2.imread(file_path)
        #     if len(img.shape) != 3 or img.shape[2] not in [1, 3, 4]:
        #         raise ValueError("Unexpected image channels")
        #     img = cv2.resize(img, (224, 224))  # Example: Resize to 224x224
        # except Exception as e:
        #     logger.warning(f"Skipping file {file_path} due to error: {e}") 
        #     img_num = os.path.splitext(os.path.basename(file_path))[0]
        #     # img_num = file_path.split('/')[-1].split('.')[0]
        #     print(f" image number:-  {img_num}" )
        #     self.list.append(img_num)
        #      # Delete the corrupt file
        #     try:
        #         os.remove(file_path)
        #         logger.info(f"Deleted corrupt file: {file_path}")
        #     except OSError as delete_error:
        #         logger.error(f"Failed to delete file {file_path}: {delete_error}")
            
        #     return None



        ###########################################

        # Load the raw data from the file as a string
        img = tf.io.read_file(file_path)
        try:
            img = tf.image.decode_image(img, channels=3)  # Decode with 3 channels (RGB)
            img = tf.image.convert_image_dtype(img, tf.float32)  # Convert to [0,1]
        except tf.errors.InvalidArgumentError:
            print(f"Skipping file {file_path} due to unexpected channels.")
            # img_num = file_path.split('/')[-1].split('.')[0]
            img_num = os.path.basename(file_path).split('.')[0]
            print(f" image number:-  {img_num}" )
            self.list.append(img_num)
            return None 
        return img


    
    def process_img(self):
        directory = self.config['datasets_dir']

        # for categories in ['train\Dog','train\Cat','test\Dog','test\Cat']:
        for categories in self.image_categories:

            directory_path = os.path.join(directory, categories)
            for filename in os.listdir(directory_path):
              file_path = os.path.join(directory_path, filename)
              # Ensure that the path is a file, not a directory
              if os.path.isfile(file_path):
                  img = self.check_channel(file_path)
                  if img is not None:
                      # You can process the img further or collect it for training
                      pass
        print(self.list)
        logger.info(f'showing the images which ishaving unexpected channel{self.list}')
        os.makedirs('artifacts', exist_ok=True)
        file = os.path.join('artifacts', 'filter_img.txt') 
        with open(file, 'w') as w:
            for item in self.list:
                w.write(f"{item}\n")
        # return self.list



    def remove_img(self):
        directory = self.config['datasets_dir']
        filter_file_path = os.path.join('artifacts', 'filter_img.txt')
    
        # Read the filtered image numbers from the file
        with open(filter_file_path, 'r') as file:
            filter_list = [line.strip() for line in file]
    
        for categories in self.image_categories:  
            directory_path = os.path.join(directory, categories)
            for filename in os.listdir(directory_path):
                file_path = os.path.join(directory_path, filename)
                # Extract the image number from the file name
                img_num = os.path.splitext(filename)[0]
                if img_num in filter_list:
                    try:
                        os.remove(file_path)
                        print(f"Removed file: {file_path}")
                    except FileNotFoundError:
                        print(f"File not found: {file_path}")
                    except OSError as e:
                        print(f"Error removing file {file_path}: {e}")
