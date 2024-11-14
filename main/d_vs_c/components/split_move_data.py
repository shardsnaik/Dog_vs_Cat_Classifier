from main.d_vs_c import logger
from sklearn.model_selection import train_test_split
import os
import shutil

class split_and_move:

    def __init__(self, config, params):
         self.config = config
         self.params = params


    def spliting_the_data(self):
        for categories in ['Cat', 'Dog']:
            dir = r'artifacts\raw_data\kagglecatsanddogs_3367a\PetImages'
            categories_path = os.path.join(dir, categories)
            images = os.listdir(categories_path)

            train_images, test_images = train_test_split(
                images,
                test_size=self.params['test_size'],
                random_state=self.params['random_state']
            )

            logger.info(f'Dividing data/Images of {categories} into train and validation set sucessfully')

            os.makedirs(os.path.join(self.config['train_dir'], categories), exist_ok=True)
            os.makedirs(os.path.join(self.config['test_dir'] ,categories), exist_ok=True)

            logger.info(f'Making folder of  {categories} categories for training and validation........')

            for img in train_images:
                shutil.copy(os.path.join(categories_path, img), os.path.join(self.config['train_dir'], categories, img))
            for img in test_images:
                shutil.copy(os.path.join(categories_path, img), os.path.join(self.config['test_dir'], categories, img))

           
            logger.info(f'Images are copied from {categories_path} to {self.config['train_dir']} successfully ....................... ')
            logger.info(f'Images are copied from {categories_path} to {self.config['test_dir']} successfully ....................... ')

    def getting_size(self):
            config = self.config
            
            logger.info(f'The number of images of Dog in the Train directory ===> {len(os.listdir(os.path.join(config['train_dir'], "Dog")))}')
            logger.info(f'The number of images of Cat in the Train directory ===> {len(os.listdir(os.path.join(config['train_dir'], "Cat")))}')
            logger.info('     ')
            logger.info(f'The number of images of Dog in the Test directory ===> {len(os.listdir(os.path.join(config['test_dir'], "Dog")))}')
            logger.info(f'The number of images of Cat in the Test directory ===> {len(os.listdir(os.path.join(config['test_dir'], "Cat")))}')

        
