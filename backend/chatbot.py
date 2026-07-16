import os
import pandas as pd
from dotenv import load_dotenv
from google import genai

# ===============================
# LOAD GEMINI API
# ===============================

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# ===============================
# LOAD DATASET
# ===============================

df = pd.read_csv("data/crime.csv")
# Clean column names
df.columns = df.columns.str.strip()

# ===============================
# SEARCH DATASET
# ===============================

def search_dataset(question):

    q = question.lower()

    results = df.copy()

    # -----------------------
    # District
    # -----------------------
    for district in df["District"].dropna().unique():

        district_str = str(district).lower()

        if district_str in q:
            results = results[
                results["District"] == district
            ]

    # -----------------------
    # Crime Type
    # -----------------------
    for crime in df["Crime_Type"].dropna().unique():

        crime_str = str(crime).lower()

        if crime_str in q:
            results = results[
                results["Crime_Type"] == crime
            ]

    # -----------------------
    # Police Station
    # -----------------------
    for station in df["Police_Station"].dropna().unique():

        station_str = str(station).lower()

        if station_str in q:
            results = results[
                results["Police_Station"] == station
            ]

    # -----------------------
    # Severity
    # -----------------------
    for severity in df["Severity"].dropna().unique():

        severity_str = str(severity).lower()

        if severity_str in q:
            results = results[
                results["Severity"] == severity
            ]

    return results      
# ===============================
# AI CHATBOT
# ===============================

def ask_crime_ai(question):

    # Search relevant records
    records = search_dataset(question)

    # If no records match, use the full dataset
    if records.empty:
        records = df.head(50)

    # Limit records sent to Gemini
    if len(records) > 50:
        records = records.head(50)

    # ===============================
    # CREATE GEMINI PROMPT
    # ===============================

    prompt = f"""
You are an AI Crime Investigation Assistant for Karnataka State Police.

Your job is to analyze the crime dataset and answer the officer professionally.

Dataset Columns:

{list(df.columns)}

Relevant Crime Records:

{records.to_string(index=False)}

Officer Question:

{question}

Instructions:

• Use ONLY the supplied records.
• If statistics are requested, calculate from the records.
• If trends are requested, explain them.
• If recommendations are requested, provide practical policing suggestions.

Format your answer as:

📌 Summary

📊 Analysis

🚨 Key Findings

👮 Police Recommendations
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:

        return f"⚠ Gemini Error:\n\n{e}"
    
# ===============================
# FIR ANALYZER
# ===============================

def analyze_fir(text):

    prompt = f"""
You are an AI Crime Investigation Assistant for Karnataka State Police.

Analyze the following FIR report:

{text}

Provide:

1. Crime Summary
2. Crime Type
3. Victim Details
4. Suspect Details
5. Risk Level
6. Recommended Police Action
7. Investigation Suggestions
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        # Compatible with different SDK response formats
        if hasattr(response, "text"):
            return response.text
        return str(response)

    except Exception as e:
        return f"⚠ Gemini Error:\n\n{e}"