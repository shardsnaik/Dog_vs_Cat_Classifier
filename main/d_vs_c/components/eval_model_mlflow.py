import os
import keras
import tensorflow
import mlflow
import dagshub
from mlflow import log_metric, log_param
from mlflow.keras import log_model
from dagshub import DAGsHubLogger
from main.d_vs_c.funtions.comon_funtn import save_json_file
from main.d_vs_c import logger

dagshub.init(repo_owner='sharadnaik001', repo_name='Dog_vs_Cat_Classifier', mlflow=True)
# dagshub.init(
#     repo_owner="sharadnaik001",
#     repo_name="Dog_vs_Cat_Classifier",
#     mlflow=True,
#     username="sharadnaik001",
#     password="f86ef673fbadc6b8a3188c34cd7218030c6b1f05"
# )

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)


class Evalution:
    
    def __init__(self, config, params) -> None:
        self.config = config
        self.params = params

    def laod_nd_eval(self):
        # checking the test data
        test_ds = keras.utils.image_dataset_from_directory(
            directory = self.config['test_dir'],
            image_size = (256, 256)
        )
        # print(test_ds.shape)
        mdl = os.path.join(self.config['trained_model_path'], self.config['model_name'])

        print(f'loading the model..{mdl}')


        self.model = tensorflow.keras.models.load_model(mdl)
        self.model.compile(optimizer = 'adam', loss = 'categorical_crossentropy')
        self.score = self.model.evaluate(test_ds)
        logger.info(f'Printing the Model Performance === > Model Accuracy =:> {self.score[1]} and Model loss =:> {self.score[0]}')
        self.save_score()

    def save_score(self):
        scores = {"loss": self.score[0], "accuracy": self.score[1]}
        save_json_file(path=Path("scores.json"), data=scores)


    def implementing_mlflow(self):
        tracking_uri = 'https://dagshub.com/sharadnaik001/Dog_vs_Cat_Classifier.mlflow/#/'

        mlflow.set_tracking_uri(tracking_uri)
        logger.info('  ======>   ML-Flow Started   <====== ')

        mlflow.set_experiment("Dog_vs_Cat_Classifier")

        
        # # Authenticate using credentials
        # import os
        # os.environ["MLFLOW_TRACKING_USERNAME"] = "<username>"
        # os.environ["MLFLOW_TRACKING_PASSWORD"] = "<token>"
        


        # Step 2: Enable DAGsHub Logger
        dagshub_logger = DAGsHubLogger(metrics_path="metrics.json", hparams_path="hparams.json")
        with mlflow.start_run():
            # logging the model parameters and configure
            log_param('model_name', self.config['model_name'])
            log_param("image_size", (256, 256))
                                             
            # Log metrics: Accuracy and Loss
            log_metric("accuracy", self.score[1])
            log_metric("loss", self.score[0])
      
            # Log the model itself (optional, if retraining)
            mdl = os.path.join(self.config['trained_model_path'], self.config['model_name'])
            self.model = tensorflow.keras.models.load_model(mdl)
            log_model(self.model, "keras_model")    

            # Save the logs to DagsHub
            dagshub_logger.log_metrics({"accuracy": self.score[1],  "loss": self.score[0]})        

