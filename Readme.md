# Customer Churn Predictor
A machine learning based web application that predicts whether a customer is likely to churn based on input features such as tenure, monthly charges, and total charges.

The system helps businesses take proactive actions (e.g., discounts or retention offers) to reduce customer churn.

# Features
- Interactive UI built with Streamlit for user input and predictions
- FastAPI backend for model inference.
- Predicts customer churn using trained ML model random forest classifier.
- Focus on minimizing False Negatives (important for churn detection)
- Provides actionable insights for customer retention

# Tech Stack
- Python
- Scikit-learn
- FastAPI
- Streamlit
- Pandas, NumPy
- Docker

# Model Details
Model Used: Random Forest Clasifier.
Evaluation Metrics:
Accuracy: 82 %
Precision: 55 %
Recall: 71 %
Optimization Goal: Improve recall to reduce missed churn cases

# How to Run?
on local server
 change
 dtabase_url->local_database_url
 backend_url->api_url

Clone the repository:
  git clone https://github.com/kalyani693/Customer_Churn_Predictor.git
  cd <repo-folder>
Install dependencies:
  pip install -r requirements.txt
Run FastAPI backend:
  cd backend
  python -m uvicorn FastAPI.main:app --reload
Run Streamlit frontend:
  cd frontend
  python -m streamlit run main.py

# What I Learned?
- Handling real-world datasets
- Data preprocessing and feature engineering
- Exploratory Data Analysis (EDA)
- Model evaluation using classification metrics
- Model serialization (saving/loading with pickle)
- Building APIs using FastAPI
- Integrating ML model with frontend
