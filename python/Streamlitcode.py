import streamlit as st
# import pickle

# Load your trained fraud detection model
model_path = "C://Users//nagoo//Downloads//fraud_detection_model.pkl"
model = pickle.load(open(model_path, "rb"))

# App Title
st.title("Credit Card Fraud Detection")

# Input fields for transaction data
st.header("Enter Transaction Details")

# User inputs
amount = st.number_input("Transaction Amount", min_value=0.0, step=0.01)
transaction_type = st.selectbox(
    "Transaction Type",
    ["Online", "In-store", "Withdrawal", "Other"]
)
location = st.text_input("Transaction Location", "")

# Map transaction type to numerical values (if necessary for the model)
transaction_type_mapping = {
    "Online": 1,
    "In-store": 2,
    "Withdrawal": 3,
    "Other": 4
}
transaction_type_value = transaction_type_mapping[transaction_type]

# Button to trigger prediction
if st.button("Check for Fraud"):
    if location.strip() == "":
        st.warning("Please enter a valid transaction location.")
    else:
        # Prepare input data as a list (adjust based on your model's expected input format)
        input_data = [[amount, transaction_type_value]]

        # Predict using the model
        prediction = model.predict(input_data)[0]  # 1 = Fraud, 0 = Not Fraud
        confidence = model.predict_proba(input_data).max() * 100

        # Display result
        if prediction == 1:
            st.error(f"🚨 This transaction is FRAUDULENT with {confidence:.2f}% confidence!")
        else:
            st.success(f"✅ This transaction is NOT FRAUDULENT with {confidence:.2f}% confidence!")
