from ..app import app, imageList, pcaObj, componentCount
from flask import request,send_file,jsonify,json,render_template
import io
import json
from ..util import getImageFromPCA

# entry point to the app
@app.route('/')
def getForm():
    return render_template('page1.html',show = app.config['PCA_SHOW'], total=componentCount())

# returns the image from an array of co-ordinates of the principal components.
# @param pca_array a stringified json array of coordinates in Principal Component Space
@app.route('/getImageFromPCA', methods=['POST'])
def serviceGetImageFromPCA():
    pca_array_str = request.form['pca_array']
    pca_array = json.loads(pca_array_str)
    png = getImageFromPCA(pcaObj(),pca_array)
    response = send_file(io.BytesIO(png),mimetype='image/png')
    return response

# returns the Principal Component coordinates of an image.
# @param imageId id of an image or null to return the PC coordinates of the average image
@app.route('/getPCAArray/<imageId>')
def serviceGetPCAArray(imageId):
    pca_coordinates = request.form['pca_coordinates']
    return jsonify({'pca_coordinates':pca_coordinates})

# returns the image for the provided image number. If null parameter then returns the average image.
@app.route('/getImage/<imageId>')
def serviceGetImage(imageId):
    imgPath = ''#PCAUtil.getImagePath(imageId)
    # response = send_file(imgPath,mimetype='image/jpeg')
    return imageId

# returns list of 100 images randomly.
@app.route('/getImageList')
def getImageList():
    return jsonify(imageList())