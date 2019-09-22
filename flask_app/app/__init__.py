from flask import Flask
from ..config import Config
from flask_bootstrap import Bootstrap
from sklearn.decomposition import PCA
from joblib import load
import os

pcaobj_ = None
imglist_ = None
componentcount_ = None

app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)

def pcaObj():
    global pcaobj_   # in this scope, use the global name
    if pcaobj_ is None :
       pcaobj_ = load(app.config['PCA_MODEL_PATH'])
    return pcaobj_

def imageList():
    global imglist_   # in this scope, use the global name
    if imglist_ is None :
        imglist_ = []
        for root, dirs, files in os.walk(app.config['IMAGE_DIR_PATH']):
            for f in files:
                imglist_.append(f)
        # print(img_list_)
    return imglist_

def componentCount():
    global componentcount_   # in this scope, use the global name
    if componentcount_ is None :
        componentcount_ = len(pcaObj().components_)
    return componentcount_

from ..app import routes