from logging import debug
from flask import Flask, request, jsonify, render_template
#from flask_cors import CORS # library for handling cross origin resources sharing.
from predict import make_predictions, preprocess_input

app = Flask(__name__)
#CORS(app)

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        data_input = request.get_json()["data"]
        data = {}

        data["person_age"] = data_input.get("age")
        data["person_income"] = data_input.get("income")
        data["person_home_ownership"] = data_input.get("home_ownership")
        data["person_emp_length"] = data_input.get("employment_length")
        data["loan_intent"] = data_input.get("loan_intent")
        data["loan_grade"] = data_input.get("loan_grade")
        data["loan_amnt"] = data_input.get("loan_amount")
        data["loan_int_rate"] = data_input.get("loan_interest_rate")
        data["loan_percent_income"] = data_input.get("loan_percent_income")
        data["cb_person_default_on_file"] = data_input.get("default_file") # if he/she has been default before
        data["cb_person_cred_hist_length"] = data_input.get("credit_history_length")


        result = make_predictions(data)
        
        result = {
            "model_version": "credit_risk_1.0.0",
            "api_version": "v1",
            "result": str(round(list(result)[0], 3))
        }
        
    return jsonify(result)

if __name__ == '__main__':
	app.run(port=5000, debug=True)