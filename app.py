from flask import Flask, request, render_template, jsonify
from flask_cors import CORS, cross_origin
from plantDiseaseDetection.utils import decodeImage
from plantDiseaseDetection.pipeline.prediction_pipeline import PlantDisease
from plantDiseaseDetection.constants import *
from plantDiseaseDetection.utils import read_yaml, create_directories
import os


os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')


@app.route('/train', methods=['GET'])
@cross_origin()
def trainRoute():
    os.system('python main.py')
    return 'Training done successfully'


@app.route('/predict', methods=['POST'])
@cross_origin()
def predictRoute():
    config = read_yaml(CONFIG_FILE_PATH)
    prediction_config = config.prediction
    create_directories([prediction_config.root_dir])

    file_name = os.path.join(prediction_config.root_dir, 'inputImage.jpg')
    plant_disease_classifier = PlantDisease(file_name)

    image = request.json['image']
    decodeImage(image, file_name)
    result = plant_disease_classifier.predict()
    return jsonify(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)