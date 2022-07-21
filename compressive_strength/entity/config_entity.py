from collections import namedtuple

DataIngestionConfig=namedtuple("DataIngestionConfig",
["dataset_download_url", "tgz_download_dir","raw_data_dir","ingested_train_dir","ingested_test_dir"])


DataValidationConfig=namedtuple("DataValidationConfig",["Schema_file_path"])

DataTransformationConfig=namedtuple("DataTransformationConfig",["cement",
                                                                "blast_furnace_slag",
                                                                "fly_ash",
                                                                "water",
                                                                "superplasticizer",
                                                                "coarse_aggregate",
                                                                "fine_aggregate" ,
                                                                "age",
                                                                "concrete_compressive_strength"])

ModelTrainerConfig = namedtuple("ModelTrainerConfig",["Trained_model_file_path","base_accuracy"])

ModelEvaluationConfig = namedtuple("ModelEvaluationConfig",["model_evaluation_file_path","timestamp"])

ModelPusherConfig = namedtuple("ModelPusherConfig",["export_dir_path"])



