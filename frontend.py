import streamlit as st
import requests 
import json

API_URL = "http://127.0.0.1:5000"

st.title("Monkeypox Detection App")
st.write("Check the boxes for any symptoms you are experiencing.")

rectal_pain = st.checkbox("Rectal Pain")
sore_throat = st.checkbox("Sore Throat")
penile_oedema = st.checkbox("Penile Oedema")
oral_lesions = st.checkbox("Oral Lesions")
solitary_lesion = st.checkbox("Solitary Lesion")
swollen_tonsils = st.checkbox("Swollen Tonsils")
hiv_infection = st.checkbox("HIV Infection")
sti = st.checkbox("Sexually Transmitted Infection")

if st.button("Predict"):
    data = {
        "Rectal Pain": 1 if rectal_pain else 0,
        "Sore Throat": 1 if sore_throat else 0,
        "Penile Oedema": 1 if penile_oedema else 0,
        "Oral Lesions": 1 if oral_lesions else 0,
        "Solitary Lesion": 1 if solitary_lesion else 0,
        "Swollen Tonsils": 1 if swollen_tonsils else 0,
        "HIV Infection": 1 if hiv_infection else 0,
        "Sexually Transmitted Infection": 1 if sti else 0
    }

    headers = {"Content-Type": "application/json"}
    response = requests.post(f"{API_URL}/predict", data=json.dumps(data), headers=headers)

    if response.status_code == 200:
        result = response.json()
        prediction = result["prediction"]

        if prediction == 1:
            st.error("Prediction: Positive for Monkeypox")
        else:
            st.success("Prediction: Negative for Monkeypox")
        
        st.write(f"Probability Positive: {result['probability_positive']:.2f}")
        st.write(f"Probability Negative: {result['probability_negative']:.2f}")
    else:
        st.error(f"Error: Could not get a response from the API. Status code: {response.status_code}")

    









