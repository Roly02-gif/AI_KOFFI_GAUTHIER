# 📈 Prédiction du cours du Bitcoin (BTC-EUR)

This project aims to predict the daily closing price of Bitcoin in euros using a Deep Learning model based on GRU (Gated Recurrent Units). The data is automatically fetched from Yahoo Finance through their unofficial API, then preprocessed and used to train the model.


## 📂 Repository Contents
- Projet.ipynb: Main notebook containing the entire project.

- bitcoin_historical_from_2020_to_now.csv: CSV file generated from Yahoo Finance.

- README.md: This file.

## 🚀 Features
- 📥 Automatic retrieval of BTC-EUR historical data for the last 5 years.

- 🧼 Preprocessing data.

- 🔁 Creation of time sequences for supervised learning.

- 🧠 Implementation of a GRU model with Keras.

- 🔎 Hyperparameter optimization using GridSearchCV.

- 📉 Visualization of results and model performance.

- 📅 Prediction for the next 12 months based on the trained model.

- 💰 Trading simulation using the predicted data to evaluate potential strategies.

## 📊 Data Source
Datas are collected via Yahoo Finance's API:
`https://query1.finance.yahoo.com/v8/finance/chart/BTC-EUR`
Period: from the last 5 years up to the date of execution of the script.

## 🧪 Running the Project

- Open the Projet.ipynb notebook in Jupyter Notebook, JupyterLab, or Google Colab.

- The notebook will automatically download the data and save it as a CSV.

- Train the model on the processed data.

- Visualize Bitcoin price predictions against real historical values.

- Predict Bitcoin prices for the next 12 months.

- Simulate a trading strategy based on the predicted prices.

## 🧠 GRU Model Details
- Architecture : GRU → Dropout → Dense

- Optimisation via GridSearchCV

- Loss function: mean_squared_error

## 📈 Visualization

- Valeurs réelles vs. Valeurs prédites

![Capture d’écran du 2025-04-28 21-56-43](https://github.com/user-attachments/assets/e9bd4a9b-f1c3-47b1-850c-11a02523cd18)

- 12-month forward price prediction

![Capture d’écran du 2025-04-28 22-07-13](https://github.com/user-attachments/assets/756e0f0e-2b75-46e9-aa71-f3fc30d625e8)
