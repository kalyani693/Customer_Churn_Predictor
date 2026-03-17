import streamlit as st
from sqlalchemy import text  # For raw SQL if needed, but we'll use ORM-style
from database_relational.db_main import sessionlocal
import requests

# Page configuration (unchanged)
st.set_page_config(
    page_title="Customer Churn Predictor",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS (unchanged - all your styling remains exactly the same)
st.markdown("""
<style>
    /* [All your existing CSS unchanged] */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    /* ... rest of your CSS exactly as is ... */
</style>
""", unsafe_allow_html=True)

# Main title (unchanged)
st.markdown('<h1 class="main-title">CUSTOMER CHURN PREDICTOR</h1>', unsafe_allow_html=True)

# Sidebar (unchanged - all inputs exactly the same)
with st.sidebar:
    st.markdown("## 📋 Customer Information")
    st.markdown("---")
    
    # Demographics
    st.markdown("### 👤 Demographics")
    SeniorCitizen = st.selectbox("Senior Citizen", ["Yes","No"])
    Family=st.selectbox("Family",["Yes", "No"])
    
    st.markdown("---")
    
    # Account Details
    st.markdown("### 📊 Account Details")
    tenure = st.number_input("Tenure (months)", min_value=0, max_value=1000, help="How long the customer has been with the company")
    MonthlyCharges = st.number_input("Monthly Charges ($)", min_value=0.0, max_value=2000.0, step=0.1)
    TotalCharges = st.number_input("Total Charges ($)", min_value=0.0, max_value=50000.0, step=0.1)
    
    st.markdown("---")
    
    # Services
    st.markdown("### 📞 Services")
    InternetService = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    OnlineSecurity = st.selectbox("Online Security", ["Yes", "No", "No internet"])
    OnlineBackup = st.selectbox("Online Backup", ["Yes", "No", "No internet"])
    DeviceProtection = st.selectbox("Device Protection", ["Yes", "No", "No internet"])
    TechSupport = st.selectbox("Tech Support", ["Yes", "No", "No internet"])
    Streaming = st.selectbox("Streaming", ["Yes", "No"])
  
    
    st.markdown("---")
    
    # Billing
    st.markdown("### 💳 Billing")
    Contract = st.selectbox("Contract", ["month to month", "one year", "two year"])
    PaperlessBilling = st.selectbox("Paperless Billing", ["Yes", "No"])
    PaymentMethod = st.selectbox("Payment Method", 
                                 ["Electronic check", "Mailed check", 
                                  "Bank transfer (automatic)", "Credit card (automatic)"])

# Main content area (unchanged)
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown('<div class="info-card">', unsafe_allow_html=True)
    st.markdown("### 🎯 Prediction Center")
    st.markdown("Click the button below to predict customer churn probability based on the provided information.")
    st.markdown('</div>', unsafe_allow_html=True)

# Predict button (unchanged)

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    predict_btn = st.button("Predict Churn", use_container_width=True)

# ONLY CHANGE: Replace raw SQL with SQLAlchemy (inside if predict_btn)
if predict_btn:
   
    payload={
    "SeniorCitizen":SeniorCitizen,
    "family":Family,
    "tenure":tenure,
    "InternetService":InternetService, 
    "OnlineSecurity": OnlineSecurity,
    "OnlineBackup": OnlineBackup,
    "DeviceProtection":DeviceProtection,
    "TechSupport":TechSupport,
    "Contract":Contract,
    "PaperlessBilling":PaperlessBilling,
    "PaymentMethod":PaymentMethod,
    "Streaming":Streaming,
    "MonthlyCharges":MonthlyCharges,
    "TotalCharges":TotalCharges
    }
    #connecting with api(backend)
    API_URL="http://127.0.0.1:8000/post_name"   
# add this into frontend code
#payload=user input which is get validate from backend api
    try:
        with st.spinner("calling API..."):
            res= requests.post(API_URL,
                               json=payload,
                                 timeout=15)

        if res.status_code != 200:
            st.error(f"API Error{res.status_code}: {res.text}")
        else:           
            data=res.json()  
        
            #-----replace predicted price with name which is returned as ans from api-----
        y_pred=data.get("Wii churn")  
        y_prob=data.get("Probability of Churn")  
                

        if y_pred:
            st.success(f"Predicted result : {y_pred}")
            st.success(f"Probability of churn: {y_prob}") 
        else:
            st.warning(f"Responses received but key not found.full response:{data}")
          

    except requests.exceptions.ConnectionError:
        st.error("could not connect to fastapi. is it running on port 8000?")
    except Exception as e:
        st.error(f"something went wrong:{e}")  
    

# [Rest of your code unchanged - Feature Importance, Model Performance, Footer all exactly the same]
# Feature Importance button
if "prediction" in st.session_state:
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        feature_btn = st.button(" View Feature Importance", use_container_width=True)
    
    if feature_btn:
        y_pred = st.session_state["prediction"]
        userinput = st.session_state["user_input"]
        
        st.markdown("---")
        st.markdown('<div class="info-card">', unsafe_allow_html=True)
        st.markdown("###  Feature Importance Analysis")
        

        st.markdown('</div>', unsafe_allow_html=True)

        if(y_pred == 1):
            st.markdown("---")
            st.markdown('<div class="info-card">', unsafe_allow_html=True)
            st.markdown("###  Retention Recommendations")
            
            suggestion = []
            if(userinput["tenure"].iloc[0] < 12):
                suggestion.append("Offer long-term discount to increase tenure and build loyalty.")    
            if(userinput["MonthlyCharges"].iloc[0] > 80):
                suggestion.append("Provide flexible billing or cheaper plan options to reduce cost burden.")
            if("TechSupport_yes" in userinput.columns):
                tech_support_value = userinput["TechSupport_yes"].iloc[0]
            else:
                tech_support_value = 0            
            if(tech_support_value == 0):
                suggestion.append("Encourage using Tech Support for better service experience and satisfaction.") 
            if("OnlineSecurity_yes" in userinput.columns):
                OnlineSecurity_value = userinput["OnlineSecurity_yes"].iloc[0]
            else:
                OnlineSecurity_value = 0             
            if(OnlineSecurity_value == 0):
                suggestion.append("Offer security add-ons as part of loyalty program to increase value.")

            for i, s in enumerate(suggestion, 1):
                st.markdown(f"""
                <div style='background: #f8f9fa; padding: 15px; border-radius: 10px; 
                            margin: 10px 0; border-left: 4px solid #667eea;'>
                    <strong style='color: #667eea; font-size: 1.1rem;'>{i}.</strong> {s}
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)



