# Linear Regression Predictor (From Scratch)

This project implements a **Linear Regression Model from scratch** (without using Scikit-Learn) in **Flask** and deploys it on **Render**. The application allows users to input a value for `X` and receive a predicted output based on a manually implemented regression algorithm.

## Features 🚀

- **Pure Python Linear Regression Implementation** (No external ML libraries like Scikit-Learn)
- **Web Interface with Flask**
- **Stylish Retro UI** (Black and Creme theme)
- **Deployment on Render**

## Tech Stack 🛠️

- **Backend:** Flask (Minimal API for Model Prediction)
- **Frontend:** HTML, CSS (Retro-styled UI)
- **Deployment:** Render (for hosting the web application)

---

## Installation 📥

To run this project locally, follow these steps:

### **1. Clone the Repository**

```sh
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### **2. Set Up a Virtual Environment**

```sh
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### **3. Install Dependencies**

```sh
pip install -r requirements.txt
```

### **4. Run the Application**

```sh
python app.py
```

The application will be available at `http://127.0.0.1:5000/`

---

## Project Structure 📂

```
│── app.py             # Main Flask app with Linear Regression logic
│── model.py           # Linear Regression Model (Implemented from Scratch)
│── templates/
│   ├── index.html     # HTML template with input field & styling
│── static/
│   ├── styles.css     # CSS for UI design
│── requirements.txt   # Dependencies
│── README.md          # Project documentation
```

---

## How It Works ⚙️

This project implements **Simple Linear Regression** using only NumPy and basic Python functions.

1. **Training**: The model calculates the best-fit line using the formula:

   **y = mX + c** (where `m` is slope and `c` is intercept)
2. **Prediction**: The user inputs `X`, and the application computes `y` using the trained parameters.
3. **Web UI**: The user interacts via a Flask-based form.

---

## Deployment on Render 🌍

To deploy on **Render**, follow these steps:

1. **Push your code to GitHub**
2. **Link your repository to Render**
3. **Set the Start Command to:**
   ```sh
   gunicorn app:app
   ```
4. **Deploy and test your application**

---

## Requirements 📋

- Python 3.x
- Flask
- NumPy
- Gunicorn

---

## License 📜

This project is **open-source**. Feel free to use and modify it! 😊

---

🚀 **Happy Coding!** 🚀

