import streamlit as st
import pandas as pd
from company_generator import get_companies
from ai_engine import generate_insight

st.title("AI Lead Generation & Outreach Assistant")

industry = st.text_input("Industry")
location = st.text_input("Location")
num_leads = st.slider("Number of leads", 1, 10, 5)

if st.button("Generate Leads"):

    companies = get_companies(industry, location, num_leads)

    results = []

    for company in companies:

        insight = generate_insight(company, industry)

        with st.expander(company):
            st.write(insight)

        results.append({
            "Company": company,
            "Insight": insight
        })

    df = pd.DataFrame(results)

    st.subheader("Lead Summary")

    st.dataframe(df)

    csv = df.to_csv(index=False)

    st.download_button(
        label="Download Leads CSV",
        data=csv,
        file_name="ai_leads.csv",
        mime="text/csv"
    )