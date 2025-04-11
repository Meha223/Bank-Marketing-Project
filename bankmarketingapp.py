# Bank Marketing dashboard

import streamlit as st
# Load parquet files

DATA_PATH = Path(r"C:\Users\khe000626\Downloads\bank_marketing_project")
client_df = pd.read_parquet(DATA_PATH / "client.parquet")
contact_df = pd.read_parquet(DATA_PATH / "contact.parquet")
campaign_df = pd.read_parquet(DATA_PATH / "campaign.parquet")
fact_df = pd.read_parquet(DATA_PATH / "fact_campaign_results.parquet")

# Merge data for EDA
merged_df = fact_df \
    .merge(client_df, on="client_id") \
    .merge(contact_df, on="contact_id") \
    .merge(campaign_df, on="campaign_id")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Exploratory Data Analysis", "SQL Query Interface"])

if page == "Exploratory Data Analysis":
    st.title("Exploratory Data Analysis")
    st.markdown("### Distribution of Subscriptions by Age Group")
    fig_age = px.histogram(merged_df, x="age_group", color="subscribed", barmode="group")
    st.plotly_chart(fig_age)

    st.markdown("### Subscription Rate by Job")
    job_sub_rate = merged_df.groupby(["job", "subscribed"]).size().reset_index(name="count")
    fig_job = px.bar(job_sub_rate, x="job", y="count", color="subscribed", barmode="group")
    st.plotly_chart(fig_job)

    st.markdown("### Duration Length vs. Subscription")
    fig_duration = px.histogram(merged_df, x="duration_length", color="subscribed", barmode="group")
    st.plotly_chart(fig_duration)

    st.markdown("---")
    st.markdown("#### Assumptions & Insights")
    st.markdown("- Longer contact duration is associated with higher subscription rates.")
    st.markdown("- Certain jobs (e.g. admin, technician) tend to subscribe more often.")
    st.markdown("- Older age groups tend to show a higher interest in deposits.")

elif page == "SQL Query Interface":
    st.title("SQL Query Interface")

    st.markdown("### Run SQL on Parquet Data")
    sql = st.text_area("Write your SQL query below:",
                      """
                      SELECT job, COUNT(*) AS total
                      FROM merged_df
                      GROUP BY job
                      ORDER BY total DESC
                      """)

    try:
        con = duckdb.connect()
        con.register("merged_df", merged_df)
        result_df = con.execute(sql).fetchdf()
        st.dataframe(result_df)

        csv = result_df.to_csv(index=False).encode('utf-8')
        st.download_button("Download Result as CSV", csv, "query_result.csv", "text/csv")
    except Exception as e:
=======
# Bank Marketing dashboard

import streamlit as st
# Load parquet files

DATA_PATH = Path(r"C:\Users\khe000626\Downloads\bank_marketing_project")
client_df = pd.read_parquet(DATA_PATH / "client.parquet")
contact_df = pd.read_parquet(DATA_PATH / "contact.parquet")
campaign_df = pd.read_parquet(DATA_PATH / "campaign.parquet")
fact_df = pd.read_parquet(DATA_PATH / "fact_campaign_results.parquet")

# Merge data for EDA
merged_df = fact_df \
    .merge(client_df, on="client_id") \
    .merge(contact_df, on="contact_id") \
    .merge(campaign_df, on="campaign_id")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Exploratory Data Analysis", "SQL Query Interface"])

if page == "Exploratory Data Analysis":
    st.title("Exploratory Data Analysis")
    st.markdown("### Distribution of Subscriptions by Age Group")
    fig_age = px.histogram(merged_df, x="age_group", color="subscribed", barmode="group")
    st.plotly_chart(fig_age)

    st.markdown("### Subscription Rate by Job")
    job_sub_rate = merged_df.groupby(["job", "subscribed"]).size().reset_index(name="count")
    fig_job = px.bar(job_sub_rate, x="job", y="count", color="subscribed", barmode="group")
    st.plotly_chart(fig_job)

    st.markdown("### Duration Length vs. Subscription")
    fig_duration = px.histogram(merged_df, x="duration_length", color="subscribed", barmode="group")
    st.plotly_chart(fig_duration)

    st.markdown("---")
    st.markdown("#### Assumptions & Insights")
    st.markdown("- Longer contact duration is associated with higher subscription rates.")
    st.markdown("- Certain jobs (e.g. admin, technician) tend to subscribe more often.")
    st.markdown("- Older age groups tend to show a higher interest in deposits.")

elif page == "SQL Query Interface":
    st.title("SQL Query Interface")

    st.markdown("### Run SQL on Parquet Data")
    sql = st.text_area("Write your SQL query below:",
                      """
                      SELECT job, COUNT(*) AS total
                      FROM merged_df
                      GROUP BY job
                      ORDER BY total DESC
                      """)

    try:
        con = duckdb.connect()
        con.register("merged_df", merged_df)
        result_df = con.execute(sql).fetchdf()
        st.dataframe(result_df)

        csv = result_df.to_csv(index=False).encode('utf-8')
        st.download_button("Download Result as CSV", csv, "query_result.csv", "text/csv")
    except Exception as e:
        st.error(f"Error in query: {e}")
