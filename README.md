# Food Company Predictive Marketing Data Analysis

** German Below 

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


# # Lebensmittelunternehmen: Prädiktive Marketing-Datenanalyse

## Projektübersicht

Dieses Projekt konzentriert sich auf die Vorhersage von Kundenreaktionen auf Marketingkampagnen mithilfe von maschinellen Lerntechniken. Der Datensatz umfasst verschiedene Merkmale im Zusammenhang mit Kundendemografie, Kaufverhalten und Kampagnenreaktionen. Das Hauptziel besteht darin, prädiktive Modelle zu erstellen, die genau klassifizieren können, ob ein Kunde positiv auf eine Kampagne reagieren wird.

### Ziele

* Datenbereinigung und -vorverarbeitung: Vorbereitung des Datensatzes für die Analyse durch Umgang mit fehlenden Werten, Normalisierung numerischer Merkmale und Kodierung kategorialer Variablen.
* Explorative Datenanalyse (EDA): Gewinnung von Einblicken in den Datensatz durch Visualisierung von Verteilungen, Korrelationen und Beziehungen zwischen Variablen.
* Feature Engineering: Erstellung neuer Merkmale, die die Modellleistung verbessern könnten.
* Modelltraining und -bewertung: Training mehrerer maschineller Lernmodelle, Bewertung ihrer Leistung anhand von Metriken wie Genauigkeit und AUC und Auswahl des am besten performenden Modells.
* Modellabstimmung und -validierung: Feinabstimmung des ausgewählten Modells und Validierung seiner Leistung mithilfe von Kreuzvalidierung.

### Modelltraining und -bewertung

Mehrere maschinelle Lernmodelle wurden trainiert und bewertet, darunter:

* DecisionTreeClassifier
* RandomForestClassifier
* GradientBoostingClassifier
* XGBClassifier

*Modellleistung*:

* Modell Trainingsgenauigkeit Testgenauigkeit Trainings-AUC Test-AUC
* DecisionTreeClassifier 99,30% 81,17% 0,97 0,65
* RandomForestClassifier 98,80% 86,65% 0,96 0,63
* GradientBoostingClassifier 90,02% 86,79% 0,72 0,66
* XGBClassifier 91,42% 87,65% 0,74 0,67

*Analyseergebnisse*

Der XGBClassifier erwies sich als das am besten performende Modell basierend auf den Bewertungsmetriken, insbesondere Genauigkeit und AUC. Es ist jedoch wichtig zu beachten, dass die Leistung des Modells, insbesondere die AUC, darauf hinweist, dass noch Verbesserungspotenzial besteht.

### Wichtige Erkenntnisse

* Datenungleichgewicht: Der Datensatz wies ein erhebliches Klassenungleichgewicht auf, wobei nur 15% der Kunden positiv auf Kampagnen reagierten.
* Feature-Wichtigkeit: Merkmale wie Total_Spent, Yearly_Income und Customer_Tenure_In_Days waren signifikante Prädiktoren für die Kundenreaktion.
* Modellleistung: Obwohl der XGBClassifier am besten abschnitt, war die Gesamtvorhersageleistung moderat, was auf die Notwendigkeit weiterer Abstimmungen oder zusätzlicher Daten hinweist.

### Fazit

Das prädiktive Marketing-Datenanalyseprojekt zeigte die Machbarkeit der Verwendung von maschinellen Lernmodellen zur Vorhersage von Kundenreaktionen auf Marketingkampagnen. Trotz der moderaten Leistung bieten die gewonnenen Erkenntnisse und das am besten performende Modell (XGBClassifier) eine solide Grundlage für zukünftige Verbesserungen. Zukünftige Arbeiten könnten sich auf die Beschaffung weiterer Daten, die effektivere Bewältigung des Klassenungleichgewichts und die Erforschung fortschrittlicher Feature-Engineering-Techniken zur Verbesserung der Modellleistung konzentrieren.
