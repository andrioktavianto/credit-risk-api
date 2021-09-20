# Credit Risk API

This API can be used to predict probability of loan default using Logistic Regression and Weight of Evidence (WOE). Made using Flask and Python. 

## Running API

```bash
python app.py
```

## URL Params

Fields | Description | Data Type | Example Value | Null Allowed
------|-------------|-------|---------|---------
age | Age | Integer | 22 | Yes
income | Annual Income | Integer | 6000 | Yes 
home_ownership | Home ownership | Categorical | 'MORTGAGE', 'OTHER', 'OWN', or 'RENT' | No
employment_length | Employment length (in years) | Integer | 5 | Yes
loan_intent | Loan intention | Categorical | 'DEBTCONSOLIDATION', 'EDUCATION', 'HOMEIMPROVEMENT', 'MEDICAL', 'PERSONAL', or 'VENTURE' | No
loan_grade | Loan grade | Categorical | 'A', 'B', 'C, 'D', 'E', 'F', or 'G' | No
loan_amount | Loan amount | Integer | 1000 | Yes
loan_interest_rate | Loan interest rate | Float | 5.7 | Yes
loan_percent_income | Loan percentage to income | Float | 0.15 | Yes
default_file | Has this specific person has been default on loan before? | Categorical | 'Y', or 'N' | No
credit_history_length | Credit history length | Integer | 3 | Yes

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