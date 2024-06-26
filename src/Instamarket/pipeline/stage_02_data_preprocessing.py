from instamarket.config.configuration import ConfigurationManager
from instamarket.components.data_preprocessing import DataPreprocessing

class DataPreprocessingTrainingPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_preprocessing_config = config.get_data_preprocessing_config()
        data_preprocessing = DataPreprocessing(config=data_preprocessing_config)
        data_preprocessing.start()
        