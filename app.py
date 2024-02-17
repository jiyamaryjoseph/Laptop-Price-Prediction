from flask import Flask, request, jsonify
from laptop import utils
from laptop.logger import logging
from laptop.pipeline.prediction_pipeline import CustomData
app = Flask(__name__)


@app.route('/get_all_data', methods=['GET'])
def get_all_data():
    response = jsonify(utils.get_all_data())
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/predict_laptop_price', methods=['GET', 'POST'])
def predict_laptop_price():
    try:
        logging.info('Prediction process started')

        if request.method=='GET':
            return 
        
        else:
            
            brand= request.form['brand']
            laptoptype=request.form['laptoptype'],
            ram=request.form['ram'],
            weight=request.form['weight'],
            os=request.form['os'],
            gpu=request.form['gpu'],
            touchscreen=request.form['touchscreen'],
            ips=request.form['ips'],
            harddrive=request.form['harddrive'],
            ssd=request.form['ssd'],
            screen=request.form['screen'],
            screenresolution=request.form['screenresolution'],
            processor=request.form['processor'],
            obj=CustomData(brand,laptoptype,ram,weight,os,gpu,touchscreen,ips,harddrive,ssd,screen,screenresolution,processor)
            
            
        
        
        response = jsonify({
            'estimated_price':obj.get_data_as_dataframe()
        })
        response.headers.add('Access-Control-Allow-Origin', '*')

        return response
    except Exception as e:
        logging.info('Exception Occured in prediction pipeline')
        raise CustomException(e,sys)

if __name__ == "__main__":
    print("Starting Python Flask Server For Laptop Price Prediction...")
    utils.load_saved_artifacts()
    app.run()
    