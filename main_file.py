from main.d_vs_c import logger
from main.d_vs_c.pipelines.data_ingestion_pipeline import data_inges_pipeline
from main.d_vs_c.pipelines.split_and_move_pipeline import data_split_and_move
from main.d_vs_c.pipelines.data_preprocess_pipeline import preprocess_pipeline
from main.d_vs_c.pipelines.model_training_pipeline import train_save_pipeline
from main.d_vs_c.pipelines.model_evalution_pipeline import Model_evalution_pipeline

if __name__ == '__main__':
    try:
        logger.info ('>>>>>>>>>>>>>>>>  Stage Data Ingestion Process Started...')
        obj = data_inges_pipeline()
        obj.main()
        logger.info('>>>>>>>>>>>>>>>Data Ingestion Proess Completed........')
        logger.info('<<<<<<<<<<<<<<<<<<<<')
    except Exception as e:
        raise e
else:
    print('dd')



if __name__ == '__main__':
    try:
        logger.info ('>>>>>>>>>>>>>>>>  Split and Move Pipline has Started  >>>>>>>>>>>>>')
        obj = data_split_and_move()
        obj.main()
        logger.info('  <<<<<<<<<<<<<<<<<< Split and Move Pipline has Finished  <<<<<<<<<<<<<<<<<<.')
    except Exception as e:
        raise e
    
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
    

# if __name__ == '__main__':
#     try:
#         logger.info('<<<<<<<<<  The Model Evalution Pipeline Started <<<<<<<<<<<<<  ')
#         eval = Model_evalution_pipeline()
#         eval.main()
#         logger.info('>>>>>>>>>>>>   The Model Evalution Pipeline Fineshed Sucessfully......... >>>>>>>>')
#     except Exception as e:
#         raise e


# docker run -e DAGSHUB_USERNAME=sharadnaik001 -e DAGSHUB_TOKEN=f86ef673fbadc6b8a3188c34cd7218030c6b1f05 -p 8000:80 docker_container