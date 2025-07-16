from flask import Flask, request, jsonify 
from flask_cors import CORS
import util

app = Flask(__name__)
CORS(app)

@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price', methods=['POST'])

def predict_home_price():
    data = request.get_json()  # ✅ Get JSON body

    total_sqft = float(data['total_sqft'])
    bhk = int(data['bhk'])
    bath = int(data['bath'])
    location = data['location']

    estimated_price = util.predict_price(location, total_sqft, bath, bhk)
    return jsonify({'estimated_price': estimated_price})


if __name__ == '__main__':
    util.load_saved_artifacts()
    app.run(debug=True)