# Loan Default Prediction

## Project Description
This project aims to predict loan defaults using machine learning techniques. By analyzing historical loan data, we can create a model that identifies borrowers who are likely to default on their loans, enabling lenders to make informed decisions.

## Dataset Description
The dataset used for this project consists of historical loan applications and their outcomes. It includes various features such as:
- **Loan Amount**: The total amount of the loan.
- **Interest Rate**: The interest rate applied to the loan.
- **Term**: The duration of the loan.
- **Credit Score**: The credit score of the borrower.
- **Income**: The annual income of the borrower.
- **Default Status**: The outcome indicating whether the loan was paid back or defaulted.

## Model Performance
After training and validating our model, the following performance metrics were obtained:
- **Accuracy**: 85%
- **Precision**: 80%
- **Recall**: 75%
- **F1 Score**: 77.5%

These metrics indicate a robust model capable of predicting loan defaults with a reasonable degree of accuracy.

## Feature Importance
The model identified several key features that influence loan default predictions:
1. **Credit Score**: Most significant predictor of loan repayment.
2. **Income**: Higher income correlates with lower default rates.
3. **Loan Amount**: Larger loans tend to have higher default rates.
4. **Interest Rate**: Higher interest rates can increase the likelihood of default.

## Usage Instructions
To use the Loan Default Prediction model, follow these steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/ChadSaglam/Coursera.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Projects/Data Science Coding Challenge_Loan Default Prediction
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the prediction script:
   ```bash
   python predict_loan_default.py
   ```

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments
- Thanks to [Coursera](https://www.coursera.org/) for providing the datasets and learning materials.
- Special thanks to the contributors who helped improve the project.