from flask import Flask, request, render_template
import numpy as np
import pickle

app = Flask(__name__)

# Load trained model parameters
with open(r"model.pkl", "rb") as file:
    model_params = pickle.load(file)
    w_final = model_params["w"]
    b_final = model_params["b"]

def predict(X):
    return X * w_final + b_final

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    if request.method == "POST":
        try:
            X_value = float(request.form["X"])
            prediction = predict(X_value)
        except ValueError:
            prediction = "Invalid input! Please enter a number."
    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
