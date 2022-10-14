from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

@app.route('/', methods = ['GET'])
def index():
    if request.method == "GET":
        postType = request.args.get('type')
        if postType == "1":
            df = pd.read_csv("data/sus_data.csv")
            data = df.to_dict()
            return jsonify(data)
        elif postType == "2":
            df = pd.read_csv("data/questions.csv")
            data = df.to_dict()
            return jsonify(data)
        return "get"