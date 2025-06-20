# prediction.py

def predict_disease(symptoms_input):
    # Simple rule-based example
    symptoms = symptoms_input.lower().split(',')

    symptoms = [s.strip() for s in symptoms]

    # Example rules (you can expand this list)
    if "fever" in symptoms and "cough" in symptoms and "headache" in symptoms:
        return "Flu"
    elif "fever" in symptoms and "rash" in symptoms:
        return "Measles"
    elif "chest pain" in symptoms and "shortness of breath" in symptoms:
        return "Heart Disease"
    elif "cough" in symptoms and "sore throat" in symptoms:
        return "Common Cold"
    elif "fatigue" in symptoms and "weight loss" in symptoms:
        return "Diabetes"
    else:
        return "Unknown – Please consult a doctor"
