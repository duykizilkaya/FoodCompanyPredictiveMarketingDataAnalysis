# -*- coding: utf-8 -*-
"""marketing data -training predictive models

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LdxHRk_iAUapZHnOQde6uDhHmb3lu8Ab
"""

from google.colab import drive

drive.mount("/content/MyDrive")

# Merge two dataset (food_data1 & food_data2)
# Convert object type to date_time in the first dataset


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import scipy as sp
from scipy.stats import chi2_contingency
from scipy import stats
import datetime
import matplotlib.ticker as mtick

food_data1 = pd.read_csv("/content/MyDrive/MyDrive/food_data1.csv")

food_data2 = pd.read_excel("/content/MyDrive/MyDrive/food_data2.xlsx")

food_data1['Dt_Customer'] = pd.to_datetime(food_data1['Dt_Customer'])

df = food_data1.merge(food_data2, how = 'outer')

# There were two different datasets for a food company. They were merged.
# The data includes customer information (their birth year, income,
# kids and teenagers at home, education level, enrollment date to the company
# as a customer,), their amount spent for the different products in the
# last two years, number of days since their last purchase,
# if they complain in the last two years, their answer to the different campaigns
# and to the last campaign. In addition, the customer enrollment data was
# converted to datetime to analyze the data easier.

# Rename few columns to make the data more understandable.
# Show the name and the type of the columns

df = df.rename(columns={"Year_Birth": "Birth_Year", "Income" : "Yearly_Income", "Kidhome": "Kid_at_Home", "Teenhome": "Teen_at_Home",
                        "Dt_Customer" : "Customer_Enrollment_Date","Recency" : "Days_Since_Last_Purchase",
                        "MntWines": "Spent_for_Wines", "MntFruits" : "Spent_for_Fruits", "MntMeatProducts" : "Spent_for_Meat",
                        "MntFishProducts" : "Spent_for_Fish", "MntSweetProducts" : "Spent_for_Sweet",
                        "MntGoldProds" : "Spent_for_Gold", "Complain": "Complaint_Last_Two_Years"})

df.dtypes

# Some of the columns were renamed to make them more understable for the readers.

# Delete any space in colunms name (Income has space)

df.columns = df.columns.str.replace(' ', '')

# The name of " Income" columns had space in the beginning, therefore
# the space was deleted as part of data cleaning.

# Get the age of the customer from their year of birth

current_year = df.Customer_Enrollment_Date.max().year

df['Age'] = current_year - df['Birth_Year']

# Age column was created from customers' year of birth in order to
# use the infomation as part of descriptive and explorative data analysis.

# Get the tenurity of the customer from their year of enrollment

current_date = pd.to_datetime(df['Customer_Enrollment_Date']).max()

df['Customer_Tenure_In_Days'] = (current_date - pd.to_datetime(df['Customer_Enrollment_Date'])).dt.days


# Customer tenurity was calculated from enrollment year and a column was created
# to use the infomation as part of descriptive and explorative data analysis.

# Get the total acceptance rate of the campaigns

campaign_columns = ['AcceptedCmp1', 'AcceptedCmp2', 'AcceptedCmp3',
                    'AcceptedCmp4', 'AcceptedCmp5', 'Response']

df['Total_Acceptance'] = df[campaign_columns].sum(axis=1)

# Total acceptance rate of the campaigns was calculated an a column was created
# in order to use the infomation as part of descriptive and explorative data analysis.

# Add to data an index column

column_index = range(0,2240)

df['Index'] = column_index[:len(df)]

df = df[['Index'] + [col for col in df.columns if col != 'Index']]

df.shape

# An index column for customers was created in order to make the data more structured.

# Identify and drop outliers in the Age column

df = df.drop(df[df['Birth_Year'] < 1900].index)

df.shape

# Outliers in the age column was identified and dropped as part of data
# cleaning in order to get more reliable results

# Identify number of null rows for each column


df.isnull().sum().sort_values(ascending=False)

# Number of null rows for each column were identified
# to handle null data.

# Drop rows containing null data

df = df.dropna()

# The null rows were dropped from the data
# to get more reliable results in the desciptive and
# explorative analysis.

# Drop duplicated rows if there are

df = df.drop_duplicates()

# The duplicated rows were dropped from the data
# to get more reliable results in the desciptive and
# explorative analysis.

# Normalize Yearly Income by using Z-score

df['z_score'] = (df.Yearly_Income - df.Yearly_Income.mean()) / df.Yearly_Income.std()

df_no_outliers =df[np.abs(df['z_score']) <= 3]
df_no_outliers = df_no_outliers.drop(columns=['z_score'])
df = df_no_outliers

# Yearly income was normalized with Z-Score and drop the outliers
# to get more reliable results in the desciptive and
# explorative analysis.

# Create Income Interval Column

income_column = []

for row in df.Yearly_Income:
  if 0 < row <= 10000:
    income_column.append("0-10000")
  elif 10000 <= row < 20000:
    income_column.append("10000-20000")
  elif 20000 <= row < 30000:
    income_column.append("20000-30000")
  elif 30000 <= row < 40000:
    income_column.append("30000-40000")
  elif 40000 <= row < 50000:
    income_column.append("40000-50000")
  elif 50000 <= row < 60000:
    income_column.append("50000 60000")
  elif 60000 <= row < 70000:
    income_column.append("60000-70000")
  elif 70000 <= row < 80000:
    income_column.append("70000-80000")
  elif 80000 <= row < 90000:
    income_column.append("80000-90000")
  elif 90000 <= row < 100000:
    income_column.append("90000-100000")
  else:
    income_column.append("More than 100000")

income_column.sort()

df['Income_Intervals'] = income_column

# Income Interval Column for customers were created to make the analyses easier.

# Identify the number of rows and columns

df.shape

# The number of rows and columns were identified as part of
# descriptive analysis.Now there is 2206 rows and 32 columns
# in the data.

# Identify columns - updated version

df.columns

# The columns were identified as part of
# descrpitive analysis.

# Get important statistics from the data

df.describe()

# The statisctics of columns (count, mean, min number, max number, %25, %50, %75,
# standard deviation) were gathered as part of descrptive analysis.

# Get the name of the columns, total non-null values in these columns and the type of the columns

df.info()

# The name of the columns, total non-null values in these columns and the type of the columns were
# gathered as part of descriptive analysis. Now, there is no null data and we have 27 integer
# 1 float, 3 object and 1 date type column.

# Identify number of unique values in the columns

df.nunique()

# # The number of unique values in the columns were identified
# as part of descriptive analysis. The categories of education level, and the marital
# status can be explored further.

# Idetify unique values in Education and Marital Status

print(df['Education'].unique())
print(df["Marital_Status"].unique())

# The unique values in Education and Marital Status were identified
# as part of descriptive anaylsis.

# Replace "Alone" and "Yolo(You Live Only Once)" with "Single" in Marital Status

df["Marital_Status"] = df["Marital_Status"].str.replace('Alone','Single')
df["Marital_Status"] = df["Marital_Status"].str.replace('YOLO','Single')

print(df["Marital_Status"].unique())

# Rows including "Alone" and "Yolo" were replaced with "Single" in Marital Status
# since they have the same meaning in the data.

# Remove the rows contain Absurd in Marital Status

mask = df['Marital_Status'] == 'Absurd'

df = df.drop(df[df["Marital_Status"]== "Absurd"].index)

# The rows contain "Absurd" in Marital Status were
# deleted as part of data cleaning.

# Create a Correlation Map with Heatmap

corr = df.corr(numeric_only=True)

plt.figure(figsize=(12,9))
sns.heatmap(corr, cmap='RdBu')

plt.show()

# a Correlation Map with Heatmap was created to understand the
# correlation between columns.

# After completing data-cleaning and descriptive analysis, our next goal was to
# implement a predictive analysis with using machine learning. We wanted to
# predict response of the customers to our last campaingn by providing customer information.
# Our inputs were customer demographics (education, marital status, age, income etc.)
# and their spending habits (purchases and spend amounts). Our output was response column.

# Create One Hot Vectors for Marital Status

one_hot_marital_status = pd.get_dummies(df['Marital_Status'])*1

print(one_hot_marital_status.shape)

# Add to data an index column

column_index_marital_status = range(0,2204)

one_hot_marital_status['Index'] = df['Index'].copy()

print(one_hot_marital_status.shape)

df = pd.merge(df, one_hot_marital_status, how = "inner")

df.shape

# One Hot vectors for marital status were created as part of data preperation before conducting prediction analysis.
# These vectors were created because marital status was categorical data.

# Create One Hot Vectors for Education

one_hot_education_status = pd.get_dummies(df['Education'])*1

print(one_hot_education_status.shape)
print(type(one_hot_education_status))

# Add to data an index column

# column_index_education_status = range(0,2204)

one_hot_education_status['Index'] = df['Index'].copy()
print(df.shape)
df = pd.merge(df, one_hot_education_status, how = "inner")
print(df.shape)

# One Hot vectors for education were created as part of data preperation before conducting prediction analysis.
# These vectors were created because education was categorical data.

# Drop columns that won't be used in the prediction analysis with machine learning models

df = df.drop(['ID', 'Income_Intervals','Index', 'Birth_Year', 'Days_Since_Last_Purchase', 'Complaint_Last_Two_Years', 'Total_Acceptance', 'Customer_Enrollment_Date'], axis=1)

# The columns that won't be used in the prediction analysis with machine learning models were dropped.
# These columns were ID, Income_Intervals, Index, Birth_Year, Days_Since_Last_Purchase, Complaint_Last_Two_Years, Total_Acceptance and Customer_Enrollment_Date.

# Sum the spending on different products in one column

total_spent_columns = ['Spent_for_Wines', 'Spent_for_Fruits',
'Spent_for_Fish', "Spent_for_Meat", 'Spent_for_Sweet', 'Spent_for_Gold']

df["Total_Spent"] = df[total_spent_columns].sum(axis = 1)

# Spending on different products in one column were summed as part of data preperation before conducting prediction analysis.

# Drop the spent columns after calculating the total

df = df.drop(['Spent_for_Wines', 'Spent_for_Fruits',
'Spent_for_Fish', "Spent_for_Meat", 'Spent_for_Sweet', 'Spent_for_Gold'] , axis=1)

# Spent_for_Wines, Spent_for_Fruits, Spent_for_Fish, Spent_for_Meat, Spent_for_Sweet, Spent_for_Gold
# columns were dropped after calculating the total in a new column.

# Sum total purchase in a column (only purchases with similar correlations with the other columns are shown.)

total_purchase_columns = ['NumWebPurchases', 'NumCatalogPurchases', 'NumStorePurchases']

df["Total_Purchase"] = df[total_purchase_columns].sum(axis = 1)

# Purchases with similar correlations with the other columns were summed in a column.

# # Drop the purchase columns after calculating the total

df = df.drop(['NumWebPurchases', 'NumCatalogPurchases', 'NumStorePurchases'] , axis =1)

# Drop the categorical data after creating one hot vectors.

df = df.drop(['Education', "Marital_Status"] , axis =1)

df.columns

# Education and Marital Status were dropped after creating one hot vectors.

# Scale continous data with using sklearn

from sklearn.preprocessing import StandardScaler

scaled_columns = ['Age', 'Yearly_Income', 'Customer_Tenure_In_Days', 'Total_Spent','Total_Purchase','NumDealsPurchases','NumWebVisitsMonth']

scaler = StandardScaler()

scaler.fit(df[scaled_columns])

df[scaled_columns] = scaler.transform(df[scaled_columns])

# Columns containing continous data (Age, Yearly_Income, Customer_Tenure_In_Days, Total_Spent,
#Total_Purchase,NumDealsPurchases,NumWebVisitsMonth columns) were fit and tranformed by using sklearn and
# StandardScaler Class.

# Observe the mean and variance of the scaled columns

scaler.mean_, scaler.var_

# Mean and variance of the scaled columns were gathered.

# Get the head rows of new and updated columns.
df.head()

# The information from new and updated columns were gathered
# by inferred head rows from the dataframe.

df.shape

# Implement several machine learning models after splitting the data to 5 as train and test data (4 train, 1 test data)

from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
# from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, roc_auc_score

scaled_columns = ['Age', 'Yearly_Income', 'Customer_Tenure_In_Days', 'Total_Spent','Total_Purchase','NumDealsPurchases','NumWebVisitsMonth']

kf = KFold(n_splits=5)
print(kf.get_n_splits(df))

for i, (train_index, test_index) in enumerate(kf.split(df)):
    #print(f" Train:index={train_index}")
    #print(f" Test: index={test_index}")
    training_df = df.iloc[train_index]
    test_df = df.iloc[test_index]

    scaler = StandardScaler()
    scaler.fit(training_df[scaled_columns])

    training_df.loc[:, scaled_columns] = scaler.transform(training_df[scaled_columns])
    test_df.loc[:, scaled_columns] = scaler.transform(test_df[scaled_columns])


    y_train = training_df['Response']
    X_train = training_df.drop(["Response"], axis = 1)

    y_test = test_df['Response']
    X_test = test_df.drop(['Response'], axis=1)

    # clf = DecisionTreeClassifier(criterion='gini')
    # clf = RandomForestClassifier(n_estimators=16)
    # clf = GradientBoostingClassifier(n_estimators=100, learning_rate=1.0, max_depth=1, random_state=0)
    clf = XGBClassifier(n_estimators=80, max_depth=2, tree_method="hist")
    clf.fit(X_train, y_train)

    y_train_pred = clf.predict(X_train)
    y_test_pred = clf.predict(X_test)

    train_accuracy = accuracy_score(y_train, y_train_pred)
    test_accuracy = accuracy_score(y_test, y_test_pred)

    train_auc = roc_auc_score(y_train, y_train_pred)
    test_auc = roc_auc_score(y_test, y_test_pred)

    print(f"Trial {i}, Training accuracy: {train_accuracy}, Test accuracy: {test_accuracy}")
    print(f"Trial {i}, Training AUC: {train_auc}, Test AUC: {test_auc}")
    print("-"*12)

    # The dataframe was splitted into 5 parts for K-fold cross validation. 4 of them were identified
    # as training data and 1 was identified as test data. Within different machine learning models,
    # DecisionTreeClassifier,RandomForestClassifier, GradientBoostingClassifier and XGBClassifier were used and tested.
    # Since there was a data imbalance (only 15% of customers responded positively to the campaigns. So, in the Response
    # column,only %15 of the values are coded as 1 and the rest as 0.
    # It can be conluded that, XGBClassifier was the most suitable machine learning model for our data.
    # Yet, the prediction of the model was not very succesful and especially AUC was not very high, it is
    # still in the acceptable rate. As a future work, these models can be tested in a larger dataset,
    # since we only have 2204 rows and these models generally work better in the larger datasets.