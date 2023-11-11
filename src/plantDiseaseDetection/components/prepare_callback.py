import time
import os
from plantDiseaseDetection.entity import PrepareCallbacksConfig
import tensorflow as tf



class PrepareCallback:
    def __init__(self, config=PrepareCallbacksConfig):
        self.config = config

    # Tensorboard Callback
    @property
    def _create_tb_callback(self):
        timestamp = time.strftime("%Y-%m-%d-%H:%M:%S")
        tb_running_log_dir = os.path.join(
            self.config.tensorboard_root_log_dir,
            f'tb_logs_at_{timestamp}'
        )
        return tf.keras.callbacks.TensorBoard(log_dir=tb_running_log_dir)
    
    # ModelCheckpoint Callback
    @property
    def _create_ckpt_callback(self):
        return tf.keras.callbacks.ModelCheckpoint(
            filepath=self.config.checkpoint_model_filepath,
            save_best_only=True
        )
    
    # EarlyStopping Callback
    @property
    def _create_estp_callback(self):
        return tf.keras.callbacks.EarlyStopping(
            monitor="val_loss",
            patience=3,
            mode="auto"
        )

    def get_tb_ckpt_callback(self):
        return [
            self._create_tb_callback,
            self._create_ckpt_callback,
            self._create_estp_callback
        ]