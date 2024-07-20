# Food Company Predictive Marketing Data Analysis

## Project Overview

This project focuses on predicting customer responses to marketing campaigns using machine learning techniques. The dataset comprises various features related to customer demographics, purchase behaviors, and campaign responses. The primary goal is to build predictive models that can accurately classify whether a customer will respond positively to a campaign.

### Goals

* Data Cleaning and Preprocessing: Prepare the dataset for analysis by handling missing values, normalizing numerical features, and encoding categorical variables.
* Exploratory Data Analysis (EDA): Gain insights into the dataset by visualizing distributions, correlations, and relationships between variables.
* Feature Engineering: Create new features that could improve model performance.
* Model Training and Evaluation: Train multiple machine learning models, evaluate their performance using metrics such as accuracy and AUC, and select the best-performing model.
* Model Tuning and Validation: Fine-tune the selected model and validate its performance using cross-validation.

### Model Training and Evaluation

Several machine learning models were trained and evaluated, including:

- DecisionTreeClassifier
- RandomForestClassifier
- GradientBoostingClassifier
- XGBClassifier

_Model Performance_:

* Model	Training  Accuracy	Test Accuracy	Training AUC	Test AUC
* DecisionTreeClassifier	99.30%	81.17%	0.97	0.65
* RandomForestClassifier	98.80%	86.65%	0.96	0.63
* GradientBoostingClassifier	90.02%	86.79%	0.72	0.66
* **XGBClassifier**	91.42%	87.65%	0.74	0.67

_Analysis Results_

The XGBClassfier emerged as the best-performing model based on the evaluation metrics, particularly accuracy and AUC. However, it is important to note that the model's performance, especially the AUC, indicates there is room for improvement.

### Key Findings

* Data Imbalance: The dataset exhibited a significant class imbalance, with only 15% of customers responding positively to campaigns.
* Feature Importance: Features such as Total_Spent, Yearly_Income, and Customer_Tenure_In_Days were significant predictors of customer response.
* Model Performance: While the XGBClassifier performed the best, the overall predictive performance was moderate, suggesting the need for further tuning or additional data.

### Conclusion

The predictive marketing data analysis project demonstrated the feasibility of using machine learning models to predict customer responses to marketing campaigns. Despite the moderate performance, the insights gained and the best-performing model (XGBClassifier) provide a solid foundation for future improvements. Future work could focus on acquiring more data, addressing class imbalance more effectively, and exploring advanced feature engineering techniques to enhance model performance. ​
