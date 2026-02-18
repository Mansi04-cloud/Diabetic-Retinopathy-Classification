import os
import numpy as np
from flask import Flask, render_template, request, redirect, url_for, session
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

app = Flask(__name__)
app.secret_key = "dr_secret_key"

app.config['UPLOAD_FOLDER'] = 'static/uploads'

model = load_model("dr_model.h5")

classes = ["No_DR", "Mild", "Moderate", "Severe", "Proliferative_DR"]


# ---------------- HOME ----------------
@app.route('/')
def home():
    return render_template("index.html")


# ---------------- LOGIN ----------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Password must be exactly 4 digits
        if len(password) == 4 and password.isdigit():
            session['user'] = email
            return redirect(url_for('prediction_page'))
        else:
            return render_template("login.html", error="Password must be exactly 4 digits")

    return render_template("login.html")


# ---------------- REGISTER ----------------
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']

        if len(password) == 4 and password.isdigit():
            session['user'] = name
            return redirect(url_for('prediction_page'))
        else:
            return render_template("register.html", error="Password must be exactly 4 digits")

    return render_template("register.html")


# ---------------- LOGOUT ----------------
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))


# ---------------- PREDICTION PAGE ----------------
@app.route('/prediction')
def prediction_page():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template("prediction.html")


# ---------------- PREDICT ----------------
@app.route('/predict', methods=['POST'])
def predict():

    if 'user' not in session:
        return redirect(url_for('login'))

    file = request.files['file']
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    img = image.load_img(filepath, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0

    prediction = model.predict(img_array)
    class_index = np.argmax(prediction)
    confidence = float(np.max(prediction)) * 100
    result = classes[class_index]

    return render_template(
        "result.html",
        prediction=result,
        confidence=round(confidence, 2),
        filename=file.filename
    )


if __name__ == '__main__':
    app.run(debug=True)
