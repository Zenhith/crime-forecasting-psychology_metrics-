ECHO is on.
# UK Crime Forecasting Using Police and NHS Data

This project aims to analyze and predict crime trends across the UK using historical data from the police and the NHS (National Health Service). By utilizing various machine learning models, the project seeks to understand the relationship between crime rates and mental health statistics, providing an analytical view of how these factors interplay over time.

## Project Overview

The dataset includes:
- **Police Data**: Crime statistics from UK police departments, detailing the number of offenses by category and year.
- **NHS Data**: Mental health data, aggregated by year, showing total counts and crude rates of mental health indicators that may be relevant to crime patterns.

The goal is to merge these datasets and create a forecasting model that helps to predict future crime trends based on past behavior and psychological metrics.

## Data Description

The project uses two primary data files, located in the `data/` directory:

1. **`2020-2023_CO.xlsx`**: 
   - An Excel file containing UK police data on crime outcomes.
   - The file includes columns such as:
     - `Financial Year`: The fiscal year for which the data is recorded (e.g., 2020/21).
     - `Offense Group`: The category or type of crime (e.g., theft, violence).
     - `Number of Offenses`: The total count of offenses for that category within the given year.

2. **`2021-2024_MHA.csv`**: 
   - A CSV file containing NHS mental health data.
   - The file includes:
     - `Year`: The calendar year corresponding to the mental health data.
     - `Total_Count`: The total count of relevant mental health cases for that year.
     - `CrudeRate`: The average rate of these cases per population.

The data spans several years to provide a longitudinal view of how crime and mental health trends change over time.

## Methodology and Models Used

### Data Preprocessing
- The data from the police and NHS sources are merged based on the `Year`.
- Relevant features are extracted and cleaned to remove any missing or irrelevant values.
- The dataset is then prepared to be fed into the machine learning models.

### Models Used for Forecasting
The project uses three machine learning models to predict crime trends:

1. **Linear Regression**: 
   - A baseline model that uses a straight-line relationship to predict the number of offenses.
   - Provides interpretability by indicating how much crime counts change with respect to mental health indicators.

2. **Decision Tree Regressor**:
   - A non-linear model that creates a tree-like structure to make predictions based on feature splits.
   - Captures complex relationships in the data but may be prone to overfitting if not tuned properly.

3. **Random Forest Regressor**:
   - An ensemble model that builds multiple decision trees and averages their predictions to improve accuracy and robustness.
   - This model generally provides the best performance and is more resistant to overfitting compared to a single decision tree.

### Evaluation Metrics
The models are evaluated using the following metrics:
- **Mean Absolute Error (MAE)**: The average absolute difference between predicted and actual values.
- **Root Mean Squared Error (RMSE)**: A measure that penalizes larger errors more than MAE.

The model with the best balance of MAE and RMSE is selected as the final model for predicting crime trends.

## How to Use This Project

### Prerequisites
- **Python 3.x**
- **Pandas** and **scikit-learn** for data processing and modeling.

### Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/Zenhith/crime-forecasting-psychology_metrics-.git
   cd crime-forecasting-psychology_metrics-


### Running the Model
Prepare Data:
Ensure 2020-2023_CO.xlsx and 2021-2024_MHA.csv are located in the data/ directory.
Run the Python Script:
Execute the main Python script to process the data, train the models, and make predictions:
python crime_forecast_script.py
View Results:
The script will output the model performance (MAE and RMSE) and show predictions for future crime trends.

### Directory Structure

crime-forecasting-psychology_metrics-/
│
├── data/
│   ├── 2020-2023_CO.xlsx          # UK Police crime data
│   ├── 2021-2024_MHA.csv          # NHS mental health data
│
├── crime_forecast_script.py       # Main script for processing and model training
├── README.md                      # Project overview and usage guide
├── requirements.txt               # Dependencies for the project
├── .gitignore                     # Ignored files and folders
### License
This project is open-source and available for use under the MIT License. Contributions are welcome!

### Acknowledgments
UK Police: For providing crime data that forms the backbone of this project.
NHS: For providing mental health data, allowing a better understanding of the relationship between mental health and crime trends.