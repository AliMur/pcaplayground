import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'cant_guess_this'
    IMAGE_DIR_PATH = os.environ.get('IMAGE_DIR_PATH') or './image_dir/'
    PCA_MODEL_PATH = os.environ.get('PCA_MODEL_PATH') or './models/pcatest.joblib'
    PCA_SHOW = 50