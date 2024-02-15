# from flask import Flask, request, jsonify
# from src import utils
# app = Flask(__name__)


# @app.route('/get_all_data', methods=['GET'])
# def get_all_data():
#     response = jsonify(utils.get_all_data())
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     return response


 

# @app.route('/predict_laptop_price', methods=['GET', 'POST'])
# def predict_laptop_price():
  

#     response = jsonify({
#         'estimated_price': utils.get_estimated_price(location,total_sqft,bhk,bath)
#     })
#     response.headers.add('Access-Control-Allow-Origin', '*')

#     return response

# if __name__ == "__main__":
#     print("Starting Python Flask Server For Laptop Price Prediction...")
#     utils.load_saved_artifacts()
    # app.run()