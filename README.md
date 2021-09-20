# Credit Risk API

This API can be used to predict probability of loan default. Made using Flask and Python. 

## Running API

```bash
python app.py
```

## API Usage

`POST /predict`

Function: Getting probability of loan default

Example URL: http://127.0.0.1:5000/predict

Example request body using JSON
```json
{
 "data":
 {
     "age": 24,
     "income": 10980,
     "home_ownership": "OWN",
     "employment_length": 0,
     "loan_intent": "PERSONAL",
     "loan_grade": "A",
     "loan_amount": 1500,
     "loan_interest_rate": 7.29,
     "loan_percent_income": 0.14,
     "default_file": "N",
     "credit_history_length": 3
 }   
}
```

Response body
```json
{
    "api_version": "v1",
    "model_version": "credit_risk_1.0.0",
    "result": "0.046"
}
```
Notes: All columns can accept null value except for categorical column, such as `home_ownership`, `loan_intent`, `loan_grade`, `default_file`

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.