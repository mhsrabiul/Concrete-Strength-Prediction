# Hybrid Fiber Reinforced Recycled Aggregate Concrete's Compressive Strength Prediction using Machine Learning

This repository contains code and resources for predicting the compressive strength of fiber reinforeced recycled aggregate concrete using various machine learning models. The project involves building models to predict concrete compressive strength based on multiple features, such as water-to-binder ratio, aggregate content, and fiber type.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Usage](#usage)
- [Models Used](#models-used)
- [Dataset](#dataset)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Project Overview
Concrete strength prediction is essential in construction projects to ensure the material meets safety and performance standards. This project uses machine learning techniques to predict concrete compressive strength based on data from concrete mix design and material properties extracted from peer reviewed literatures.

The project leverages different machine learning models, evaluates their performance, and compares the results to select the best model for the task.

## Features
- Predict compressive strength based on concrete mix design features
- Models include basic models, tree based models and ensemble models
- Model comparison based on performance metrics such as R-squared, Adjusted R-squared Mean Squared Error (MSE), Mean Absolute Error and Root Mean Squared Error (RMSE)
- Hyperparameter tuning using GridSearchCV with 5-fold cross validation
- Visualizations for feature importance and model performance

## Usage
1. **Data Preprocessing**: The dataset is preprocessed, with missing values handled and features standardized.
2. **Model Training**: Different machine learning models are trained on the preprocessed data.
3. **Evaluation**: Models are evaluated using metrics like R-squared, MSE, MAE and RMSE.
4. **Prediction**: The trained models are used to predict the compressive strength of new concrete mixes.

## Models Used
- Linear Regression
- Ridge and Lasso Regression
- Decision Trees
- Random Forest
- Support Vector Machines
- K-Nearest Neighbors
- AdaBoost
- XGBoost
- LGBM
- CatBoost

## Dataset
The dataset used in this project includes features related to the concrete mix design and fiber types. The key features include:
- Water-to-binder ratio
- Coarse and fine aggregate ratios
- Recycled aggregate replacement rate
- Curing age
- Fiber types (Steel, Nylon, Polypropylene, etc.)
- Water absorption of recycled aggregate
- Compressive strength

## Results
- The best performing model in this study was LGBM, achieving an R-squared score of **0.969** and RMSE of **3.75**.
- CatBoost and XGB also performed well, demonstrating the strength of ensemble learning methods.

## Contribution
This prediction model was my undergraduate thesis project. I'm grateful to my supervisor- *Asst. Professor Mehedi Hasan*, Department of Building Engineering & Construction Management, Rajshahi University of Engineering & Technology- RUET.

I also acknowledge that this project were compled with the assistance and cordial support of-
*Ehasnul Bashar Pranto*, Undergrad Student, Department of Statistics, University of Rajshahi.


## License
This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

