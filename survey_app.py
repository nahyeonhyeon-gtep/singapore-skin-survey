#!/usr/bin/env python
# coding: utf-8

# In[9]:


import streamlit as st

st.set_page_config(page_title="Singapore Skin Type Survey", page_icon="🧴")

st.title("🧴 Singapore Skin Type Survey")
st.write("Analyze your skin type and get personalized skincare insights!")

st.markdown(
    "This survey is for women aged 18–29 in Singapore. "
    "Your answers are anonymous and will be used in aggregated form "
    "to understand common skin concerns and recommend suitable skincare solutions."
)

st.header("1. About You")

age = st.selectbox(
    "Age group",
    ["18–29", "30-44", "45+"]
)

gender = st.radio(
    "Gender",
    ["Female", "Male", "Prefer not to say"]
)

ethnicity = st.selectbox(
    "Ethnicity / Race (optional)",
    ["Chinese", "Malay", "Indian", "Other / Prefer not to say"]
)

st.header("2. Skin Condition (1 = Strongly disagree / 5 = Strongly agree)")

OIL = st.slider("My T-zone (forehead / nose) becomes oily or shiny easily.", 1, 5, 3)
HYD = st.slider("My skin feels tight or dry after washing, even with a gentle cleanser.", 1, 5, 3)
SEN = st.slider("My skin often stings, burns, or turns red when I try new products.", 1, 5, 3)
ACN = st.slider("I get breakouts / pimples frequently.", 1, 5, 3)
POR = st.slider("I notice visible pores or blackheads.", 1, 5, 3)
RED = st.slider("My skin gets red or flushed easily (sun, heat, stress).", 1, 5, 3)
PIG = st.slider("I am concerned about dark spots, acne marks, or uneven tone.", 1, 5, 3)
ELST = st.slider("My skin feels less firm or shows fine lines.", 1, 5, 3)
BAR = st.slider("My skin barrier feels weak (easily irritated, damaged, flaky).", 1, 5, 3)
DRYRESIST = st.slider("My skin dries out again quickly even after moisturizer.", 1, 5, 3)

st.header("3. Priority Concern")

PRIO = st.radio(
    "If you could fix only ONE first, which concern would you choose?",
    [
        "Oily T-zone / Sebum control",
        "Acne / Breakouts / Red bumps",
        "Large pores / Blackheads",
        "Dryness / Tightness / Lack of moisture",
        "Sensitive / Easily irritated skin",
        "Dark spots / Uneven tone",
        "Loss of firmness / Fine lines",
        "Other"
    ]
)

st.header("4. Skincare Routine Habits (Select all that apply)")
ROUTINE_USE = st.multiselect(
    "Which of these do you use most days?",
    [
        "Cleanser / Face wash",
        "Toner / Pad",
        "Serum / Ampoule",
        "Moisturizer / Cream",
        "Spot treatment (pimple patch, etc.)",
        "Sunscreen",
        "I usually don’t apply skincare regularly"
    ]
)

st.header("5. What do you avoid in skincare?")
AVOID = st.multiselect(
    "When you buy skincare, which of the following do you try to avoid?",
    [
        "Strong fragrance / strong perfume",
        "Alcohol / stinging feel",
        "Heavy / greasy texture",
        "Ingredients that make my face red or hot",
        "Animal testing / not cruelty-free",
        "Nothing in particular"
    ]
)

st.header("6. Contact (Optional)")
CONSENT_RECO = st.radio(
    "Would you like to receive a personalized Ledande product suggestion based on your answers?",
    ["Yes, please send me a suggestion", "Not sure yet", "No, thanks"]
)

contact_method = None
email = None

if CONSENT_RECO == "Yes, please send me a suggestion":
    contact_method = st.radio(
        "How would you like to receive it?",
        ["Email", "Shopee chat / message", "Other / later"]
    )
    if contact_method == "Email":
        email = st.text_input("Your email (optional):")

submitted = st.button("Submit")

if submitted:
    st.success("✅ Thank you! Your skin profile has been recorded.")
    st.write("Preview of your data:")
    st.json({
        "age": age,
        "gender": gender,
        "ethnicity": ethnicity,
        "OIL": OIL,
        "HYD": HYD,
        "SEN": SEN,
        "ACN": ACN,
        "POR": POR,
        "RED": RED,
        "PIG": PIG,
        "ELST": ELST,
        "BAR": BAR,
        "DRYRESIST": DRYRESIST,
        "priority": PRIO,
        "routine_use": ROUTINE_USE,
        "avoid": AVOID,
        "consent": CONSENT_RECO,
        "contact_method": contact_method,
        "email": email
    })

    st.caption(
        "In production, this data would be stored for clustering analysis "
        "of Singaporean skin types (18–29)."
    )


# In[ ]:




