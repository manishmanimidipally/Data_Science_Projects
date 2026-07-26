# Employee Salary Prediction using Machine Learning

## 📌 Project Overview

Employee Salary Prediction is a Machine Learning project that predicts an employee's estimated salary based on their personal and professional details. This project helps demonstrate how Machine Learning can assist Human Resources (HR) teams in making salary estimations based on historical employee data.

A user-friendly **Streamlit** web application is included, allowing users to enter employee details and receive an instant salary prediction.

---

## 🚀 Features

* Predict employee salary using Machine Learning
* Interactive Streamlit web application
* Easy-to-use user interface
* Trained Random Forest Regression model
* Model saved using Joblib
* Clean and modular project structure

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Joblib
* Jupyter Notebook

---

## 📂 Project Structure

```text
Employee_Salary_Prediction/
│
├── app.py
├── train_model.ipynb
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   └── salary_data.csv
│
├── models/
│   ├── model.pkl
│   ├── gender_encoder.pkl
│   ├── education_encoder.pkl
│   └── job_encoder.pkl
│
└── screenshots/
```

---

## 📊 Dataset

The project uses an Employee Salary dataset containing features such as:

* Age
* Gender
* Education Level
* Job Title
* Years of Experience
* Salary (Target)

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/manishmanimidipally/Data_Science_Projects/tree/main/Employee_Salary_Prediction
```

### Navigate to the Project

```bash
cd Employee_Salary_Prediction
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Streamlit Application

```bash
streamlit run app.py
```

The application will start locally and open in your default web browser.

---

## 🧠 Machine Learning Workflow

1. Load Dataset
2. Data Cleaning
3. Encode Categorical Features
4. Split Data into Training and Testing Sets
5. Train the Random Forest Regression Model
6. Evaluate Model Performance
7. Save the Trained Model
8. Build the Streamlit Web Application

---

## 📸 Application Screenshots

Add your screenshots after running the application.

* Home Screen
* Salary Prediction Result

Store them inside the **screenshots/** folder.

---

## 📈 Future Improvements

* Deploy the application online
* Add more employee features
* Compare multiple regression algorithms
* Improve prediction accuracy with hyperparameter tuning
* Add interactive data visualizations

---

## 👨‍💻 Author

**Manish Mamidipally**

GitHub: https://github.com/manishmanimidipally

LinkedIn: https://www.linkedin.com/in/manish-mamidipally-334ab4313/

---

## ⭐ Support

If you found this project helpful, consider giving the repository a ⭐ on GitHub.

Thank you for visiting this project!
