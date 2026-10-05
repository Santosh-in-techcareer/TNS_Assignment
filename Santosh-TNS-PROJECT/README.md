# Group 6 Capstone Project

A machine learning capstone project consisting of two applications that demonstrate **Supervised Learning** and **Unsupervised Learning** concepts.

---

## 📌 Projects

### 1. 📧 Email Spam Detection

**Type:** Supervised Machine Learning

A machine learning application that classifies emails as:

* **Spam**
* **Not Spam (Ham)**

The model is trained using labelled email data and uses text preprocessing and feature extraction to make predictions on new emails.

### Key Concepts

* Labelled datasets
* Text preprocessing
* Feature extraction
* Train/Test Split
* Classification
* Model Evaluation
* Model Saving and Reuse
* Prediction through an application interface

---

### 2. 👥 Customer Persona Segmenter

**Type:** Unsupervised Machine Learning

A customer segmentation application that groups customers into different personas based on characteristics such as:

* Annual Income
* Spending Score

The project uses **K-Means Clustering** to identify customer groups without predefined labels.

### Key Concepts

* Unlabelled data
* Data preprocessing
* Feature scaling
* K-Means Clustering
* Cluster analysis
* Customer persona mapping
* Data visualization

---

# 🏗️ Repository Structure

```text
Group-6-Capstone-Project/
│
├── README.md
│
├── supervised/
│   └── email-spam-detection/
│       ├── README.md
│       ├── requirements.txt
│       │
│       ├── backend/
│       │   ├── train_model.py
│       │   ├── app.py
│       │   └── spam_emails.csv
│       │
│       └── frontend/
│           ├── index.html
│           ├── style.css
│           └── script.js
│
└── unsupervised/
    └── customer-persona-segmenter/
        ├── README.md
        ├── requirements.txt
        ├── dataset_unsupervised.py
        ├── train_kmeans.py
        ├── main_unsupervised.py
        └── app_unsupervised.py
```

> **Note:** Model files and generated datasets may be created automatically during the training/setup process and are not necessarily created manually.

---

# 🛠️ Technologies Used

## Machine Learning

* Python
* Pandas
* NumPy
* Scikit-learn

## Backend

* FastAPI
* Uvicorn
* Flask

## Frontend / Visualization

* HTML
* CSS
* JavaScript
* Streamlit
* Matplotlib
* Seaborn

## Development Tools

* Git
* GitHub
* Visual Studio Code

---

# 🔄 Machine Learning Workflow

## Supervised Learning

```text
Labelled Dataset
       ↓
Data Preprocessing
       ↓
Feature Extraction
       ↓
Train/Test Split
       ↓
Model Training
       ↓
Model Evaluation
       ↓
Save Model
       ↓
New Email
       ↓
Prediction
       ↓
Spam / Not Spam
```

## Unsupervised Learning

```text
Customer Dataset
       ↓
Data Preprocessing
       ↓
Feature Scaling
       ↓
K-Means Clustering
       ↓
Customer Groups
       ↓
Persona Mapping
       ↓
Visualization / Prediction
```

---

# 🎯 Objectives

* Apply machine learning concepts to practical problems.
* Understand the difference between supervised and unsupervised learning.
* Build and evaluate machine learning models.
* Integrate trained models with application backends.
* Provide simple user interfaces for interacting with the models.
* Demonstrate an end-to-end machine learning workflow.

---

# 📧 Supervised ML Project — Email Spam Detection

The **Email Spam Detection** project is divided into three development roles.

> **Important:** We have divided the project into 3 roles. Please work only on your assigned branch and **do NOT make direct changes to `main`**.

---

## 👥 Team Roles

### 1. Deepakkumar — ML Developer

**Branch:** `spam-ml`

### Responsibilities

* Dataset preparation
* Preprocessing
* TF-IDF feature extraction
* Model training
* Model evaluation
* Saving the trained model

### Main Files

```text
train_model.py
spam_emails.csv
trained model files
```

The ML Developer is responsible for preparing the email dataset, processing the text data, converting the text into numerical features using **TF-IDF**, training the machine learning model, evaluating its performance, and saving the trained model for reuse.

---

### 2. Mahalakshmi Babu — Backend Developer

**Branch:** `spam-backend`

### Responsibilities

* Work on the Flask backend and prediction API.
* Load the trained ML model.
* Create the API endpoint that receives email text.
* Return **Spam / Not Spam** prediction results.

### Main File

```text
app.py
```

The Backend Developer connects the trained machine learning model with the application through a **Flask API**.

The API receives the email text from the frontend, passes it to the trained model, obtains the prediction, and sends the result back to the frontend.

### Backend Workflow

```text
Email Text
    ↓
Flask API
    ↓
Load Trained ML Model
    ↓
Process Email
    ↓
Generate Prediction
    ↓
Spam / Not Spam
    ↓
Return Result to Frontend
```

---

### 3. V. Tejasri Kotte — Frontend Developer

**Branch:** `spam-frontend`

### Responsibilities

* Work on the user interface.
* Create the email input UI.
* Connect the frontend to the Flask backend using JavaScript.
* Display the prediction result.

### Main Files

```text
index.html
style.css
script.js
```

The Frontend Developer is responsible for creating the user interface where users can enter email content and receive the prediction from the backend.

### Frontend Workflow

```text
User enters email
        ↓
JavaScript sends request
        ↓
Flask Backend
        ↓
ML Model
        ↓
Prediction
        ↓
Spam / Not Spam
        ↓
Display Result
```

---

# 🌿 Git Branch Structure

Each team member works on a separate branch according to their assigned role.

```text
main
│
├── spam-ml
│   └── Deepakkumar
│       └── ML Development
│
├── spam-backend
│   └── Mahalakshmi Babu
│       └── Backend Development
│
└── spam-frontend
    └── V. Tejasri Kotte
        └── Frontend Development
```

## Branch Responsibilities

| Branch          | Developer        | Responsibility                                     |
| --------------- | ---------------- | -------------------------------------------------- |
| `main`          | Group 6          | Final integrated project                           |
| `spam-ml`       | Deepakkumar      | Dataset, preprocessing, TF-IDF, training and model |
| `spam-backend`  | Mahalakshmi Babu | Flask backend and prediction API                   |
| `spam-frontend` | V. Tejasri Kotte | User interface and API integration                 |

> **Important:** Team members should work only on their assigned branches and should not directly modify the `main` branch.

---

# 🔄 Email Spam Detection — Complete Workflow

The complete supervised learning application follows the workflow below:

```text
                 EMAIL SPAM DETECTION
                         │
                         ▼
                ┌─────────────────┐
                │ Email Dataset   │
                │ spam_emails.csv │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Preprocessing   │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │     TF-IDF      │
                │Feature Extraction│
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Train/Test Split│
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Model Training  │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Model Evaluation│
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │   Save Model    │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │   User enters   │
                │      email      │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Flask Backend   │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │  ML Prediction  │
                └────────┬────────┘
                         │
                    ┌────┴────┐
                    ▼         ▼
                  SPAM     NOT SPAM
```

---

# 🔗 How the Three Roles Work Together

The three components of the Email Spam Detection project work together as follows:

```text
        ML Developer
             │
             ▼
      Trained ML Model
             │
             ▼
      Backend Developer
             │
             ▼
        Flask API
             │
             ▼
      Frontend Developer
             │
             ▼
       User Interface
             │
             ▼
       User enters email
             │
             ▼
        Flask Backend
             │
             ▼
        ML Prediction
             │
             ▼
      Spam / Not Spam
```

### ML Developer

Creates and saves the machine learning model.

### Backend Developer

Loads the trained model and provides an API for prediction.

### Frontend Developer

Creates the interface and communicates with the backend API.

---

# 👥 Team

**Group 6 — Capstone Project**

This repository contains the collaborative work of the Group 6 team.

---

# 📂 Project Documentation

Detailed setup instructions, implementation details, and usage instructions are available in the individual project README files.

## Supervised Learning

```text
supervised/email-spam-detection/README.md
```

## Unsupervised Learning

```text
unsupervised/customer-persona-segmenter/README.md
```

---

# 📌 Note

This repository is developed as part of the **Capstone Project** to demonstrate practical implementation of machine learning concepts using Python and related technologies.

The project demonstrates both **Supervised Machine Learning** and **Unsupervised Machine Learning** through practical applications:

* **Email Spam Detection** — Supervised Learning
* **Customer Persona Segmenter** — Unsupervised Learning

The project follows an end-to-end machine learning workflow involving **data preparation, preprocessing, model training, evaluation, model reuse, backend integration, and user interaction**.
