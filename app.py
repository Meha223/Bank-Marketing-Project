
# Streamlit app for Task 2

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import duckdb

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["EDA", "SQL Query"])

if page == "EDA":
    st.title("Bank Marketing - EDA")
    df = pd.read_parquet("fact_campaigns.parquet")
    st.write("Sample Data", df.head())

    age_group = st.sidebar.multiselect("Age Group", options=["Young", "Adult", "Senior"], default=["Adult"])
    if "age_group" in df.columns:
        df = df[df["age_group"].isin(age_group)]

    st.subheader("Campaign Response Count")
    fig, ax = plt.subplots()
    sns.countplot(data=df, x='y', ax=ax)
    st.pyplot(fig)

elif page == "SQL Query":
    st.title("SQL Query Interface")
    query = st.text_area("Enter SQL Query", value="SELECT * FROM fact_campaigns LIMIT 10")
    run = st.button("Run")

    if run:
        result = duckdb.query(query).to_df()
        st.dataframe(result)

        csv = result.to_csv(index=False).encode('utf-8')
        st.download_button("Download CSV", data=csv, file_name="query_result.csv", mime="text/csv")
