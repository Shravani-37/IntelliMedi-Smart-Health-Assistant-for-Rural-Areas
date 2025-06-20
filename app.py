import streamlit as st
from database import insert_patient, get_connection
from prediction import predict_disease 

def show_all_patients():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patients")
    rows = cursor.fetchall()
    conn.close()
    return rows

def insert_patient_data(name, age, gender, symptoms):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO patients (name, age, gender, symptoms) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (name, age, gender, symptoms))
    conn.commit()
    conn.close()

def main():
    st.set_page_config(page_title="IntelliMedi", layout="centered")
    st.title("💊 IntelliMedi – Smart Health Assistant for Rural Areas")
    st.sidebar.title("🩺 IntelliMedi Menu")
    
    menu = ["Patient Registration", "View All Records","Symptom Checker"]
    choice = st.sidebar.selectbox("Navigation", menu)

    if choice == "Patient Registration":
        st.subheader("📋 Register a New Patient")
        with st.form("patient_form"):
            name = st.text_input("Patient Name")
            age = st.number_input("Age", min_value=0, max_value=120, step=1)
            gender = st.selectbox("Gender", ["Male", "Female", "Other"])
            symptoms = st.text_area("Symptoms")

            submit_button = st.form_submit_button("Submit")

            if submit_button:
                if name and symptoms:
                    insert_patient_data(name, age, gender, symptoms)
                    st.success("✅ Patient data saved successfully!")
                else:
                    st.error("❌ Name and symptoms are required fields.")

    elif choice == "View All Records":
        st.subheader("📄 All Patient Records")
        records = show_all_patients()
        if records:
            st.table(records)

        else:
            st.info("No patient records found.")
    elif choice == "Symptom Checker":
        st.subheader("🔍 Symptom-based Disease Prediction")
        symptoms_input = st.text_area("Enter your symptoms (comma-separated)", placeholder="e.g., fever, cough, headache")
        if st.button("Predict Disease"):
            if symptoms_input.strip():
                result = predict_disease(symptoms_input)
                st.success(f"🧠 Possible Diagnosis: **{result}**")
            else:
                st.warning("Please enter symptoms to get a prediction.")       

if __name__ == "__main__":
    main()
