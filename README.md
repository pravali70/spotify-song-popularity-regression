# 🎵 Spotify Song Popularity Prediction - Mini Project
👋 Welcome to this music-driven machine learning project focused on predicting Spotify song popularity using regression models!

## 📝 Project Overview
In this project, we explore a real-world dataset containing various audio features and track metadata from Spotify. These include:

Acousticness

Danceability

Energy

Instrumentalness

Loudness

Tempo

Valence

Duration

Genre

Artist and Track Metadata

Our goal is to build a full machine learning pipeline—from data preprocessing and exploratory analysis to model training and evaluation—to predict the popularity score of a song.

## 🎯 Objective
The primary objective is to build and compare regression models that accurately predict a song’s popularity score on Spotify (typically ranging from 0 to 100).

These predictions can help:

Streaming platforms curate personalized playlists

Artists and producers gauge hit potential

Marketers plan targeted promotions

A&R teams make data-driven decisions on track investments

## 🤖 Models Evaluated
We evaluate the following regression algorithms:

Linear Regression

Polynomial Regression

Support Vector Regression (SVR)

Random Forest Regressor

Tuned Random Forest Regressor

XGBoost Regressor

Each model is assessed for both prediction accuracy and generalization capability.

## 📊 Evaluation Metrics
To compare model performance, we use standard regression evaluation metrics:

MAE (Mean Absolute Error) – Measures average magnitude of errors

MSE (Mean Squared Error) – Penalizes larger errors

RMSE (Root Mean Squared Error) – Interpretable scale of error magnitude

These metrics help us understand how close our model predictions are to actual popularity scores.

## 🧰 Tools & Libraries
This project is built in Python, using:

pandas – Data preprocessing and analysis

numpy – Numerical operations

matplotlib & seaborn – Data visualization

scikit-learn – Regression models and preprocessing utilities

xgboost – Advanced ensemble modeling for boosted regression tasks

## ✅ Outcome
By evaluating multiple models, we aim to:

Identify the most effective algorithm for predicting song popularity

Gain insights into which song features most strongly influence success

Provide valuable guidance for music professionals and data scientists working in the entertainment industry

💡 Thanks for exploring this project! We hope it shows how data and machine learning can shape the future of music trends and digital streaming.
