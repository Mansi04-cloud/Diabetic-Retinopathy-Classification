# 🩺 Diabetic Retinopathy Classification Web Application

## Project Overview
The Diabetic Retinopathy Classification Web Application is a deep learning-based medical image classification system developed using Flask and TensorFlow/Keras.
This project aims to assist in the early detection of Diabetic Retinopathy (DR) by analyzing retinal fundus images and classifying them into different severity stages using a trained Convolutional Neural Network (CNN) model.
The system provides a user-friendly web interface for image upload, prediction display, and secure access.
________________________________________
Problem Statement
Diabetic Retinopathy is a serious diabetes-related eye disease that can lead to vision impairment and blindness if not detected early. Manual screening of retinal images is time-consuming and requires medical expertise.
The objective of this project is to develop an AI-powered system capable of automatically classifying retinal images into various stages of Diabetic Retinopathy, thereby supporting faster and more efficient medical diagnosis.
________________________________________
Objectives
•	Develop a deep learning model for DR classification
•	Build a Flask-based web application interface
•	Enable secure user authentication (Login & Registration)
•	Allow users to upload retinal images
•	Display accurate prediction results
•	Ensure structured and maintainable project architecture
________________________________________
Classification Categories
The model classifies retinal images into the following five stages:
•	No DR
•	Mild
•	Moderate
•	Severe
•	Proliferative DR
________________________________________
Features
•	User Registration and Login System
•	Retinal Image Upload Functionality
•	AI-Based Prediction using CNN Model
•	Result Display Interface
•	Clean and Responsive UI using Flask Templates
•	Secure File Handling
•	Model Saved in .h5 Format
________________________________________
Technologies Used
•	Python 3.x
•	TensorFlow / Keras
•	Flask
•	HTML
•	CSS
•	NumPy
•	OpenCV
•	SQLite (User Authentication Database)
________________________________________
Installation and Setup
Using Python Virtual Environment (Recommended)
Create a virtual environment:
python -m venv dr_env
Activate the environment:
On Windows:
dr_env\Scripts\activate
On macOS/Linux:
source dr_env/bin/activate
Install required dependencies:
pip install -r requirements.txt
________________________________________
Running the Application
Start the Flask application:
python app.py
Open your browser and go to:
http://127.0.0.1:5000/
________________________________________
Project Structure
Diabetic-Retinopathy-Classification/
│
├── static/
│   ├── uploads/                # Uploaded retinal images
│   └── style.css               # Styling files
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── prediction.html
│   └── result.html
│
├── app.py                      # Main Flask application
├── train_model.py              # Model training script
├── dr_model.h5                 # Trained deep learning model
├── requirements.txt            # Project dependencies
└── README.md                   # Project documentation
________________________________________
Model Architecture
The classification model is built using Convolutional Neural Networks (CNN) implemented in TensorFlow/Keras.
The trained model is stored as:
dr_model.h5
The model processes retinal images and predicts the severity level of Diabetic Retinopathy based on extracted visual features.
________________________________________
Dataset
The dataset consists of labeled retinal fundus images categorized into five severity levels of Diabetic Retinopathy.
Images were preprocessed (resizing, normalization) before being used for model training and validation.
________________________________________
Future Enhancements
•	Improve model accuracy using larger datasets
•	Deploy the application on cloud platforms (AWS/Azure)
•	Add a doctor dashboard
•	Integrate Grad-CAM for visual explanation
•	Add patient report generation
________________________________________
Project Type
Final Year Mini Project
Deep Learning Based Medical Image Classification System
________________________________________
Developed By
Mansi Sudhakar Patil
B.Tech Student | AI & ML Enthusiast
GitHub: https://github.com/Mansi04-cloud
________________________________________
Conclusion
This project demonstrates the practical application of deep learning in the healthcare domain. By integrating a CNN-based classification model with a Flask web interface, the system provides an accessible and efficient tool for automated Diabetic Retinopathy screening.




