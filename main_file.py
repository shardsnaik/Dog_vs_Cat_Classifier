from main.d_vs_c import logger
from main.d_vs_c.pipelines.data_ingestion_pipeline import data_inges_pipeline
from main.d_vs_c.pipelines.split_and_move_pipeline import data_split_and_move
from main.d_vs_c.pipelines.data_preprocess_pipeline import preprocess_pipeline
from main.d_vs_c.pipelines.model_training_pipeline import train_save_pipeline


# if __name__ == '__main__':
#     try:
#         logger.info ('>>>>>>>>>>>>>>>>  Stage Data Ingestion Process Started...')
#         obj = data_inges_pipeline()
#         obj.main()
#         logger.info('>>>>>>>>>>>>>>>Data Ingestion Proess Completed........')
#         logger.info('<<<<<<<<<<<<<<<<<<<<')
#     except Exception as e:
#         raise e
# else:
#     print('dd')



# if __name__ == '__main__':
#     try:
#         logger.info ('>>>>>>>>>>>>>>>>  Split and Move Pipline has Started  >>>>>>>>>>>>>')
#         obj = data_split_and_move()
#         obj.main()
#         logger.info('  <<<<<<<<<<<<<<<<<< Split and Move Pipline has Finished  <<<<<<<<<<<<<<<<<<.')
#     except Exception as e:
#         raise e
    
if __name__ == '__main__':
    try:
        logger.info ('>>>>>>>>>>>>>>>>  Images Preprocess Pipline has Started  >>>>>>>>>>>>>')
        obj = preprocess_pipeline()
        obj.main()
        logger.info('  <<<<<<<<<<<<<<<<<< Images Preprocess Pipline has Finished  <<<<<<<<<<<<<<<<<<.')
    except Exception as e:
        raise e



if __name__ == '__main__':
    try:
        logger.info('<<<<<<<<<  The Model Training Pipeline Started >>>>>>>>')
        obj = train_save_pipeline()
        obj.main()
        logger.info('<<<<<<<<<  The Model Training Pipeline Finished >>>>>>>>')
    except Exception as e:
        raise e
    

# 622/622 ━━━━━━━━━━━━━━━━━━━━ 1692s 3s/step - accuracy: 0.5057 - loss: 15.1780 - val_accuracy: 0.5022 - val_loss: 1.7222
# app-1  | [2024-11-21 16:53:13,430: INFO: buid_train_model: Plotting the graph of Loss and Val_Loss]
# app-1  | [2024-11-21 16:53:13,555: INFO: buid_train_model: Plotting the graph of Accuracy and Val_Accuracy]                                                                        
# app-1  | Traceback (most recent call last):
# app-1  |   File "/app/main_file.py", line 49, in <module>
# app-1  |     raise e
# app-1  |   File "/app/main_file.py", line 46, in <module>
# app-1  |     obj.main()                                                                                                                                                            
# app-1  |   File "/app/main/d_vs_c/pipelines/model_training_pipeline.py", line 24, in main
# app-1  |     obj2.save_model()
# app-1  |   File "/app/main/d_vs_c/components/buid_train_model.py", line 114, in save_model
# app-1  |     model_path = os.path.join(self.config['trained_model_path'], 'model_v-03.h5')                                                                                         
# app-1  | KeyError: 'trained_model_path'
# app-1 exited with code 1
