import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

st.set_page_config(page_title="Solar Metrics Comparison", layout="wide")

@st.cache_data
def load_data(country):
    path = f"data/{country.lower()}_clean.csv"
    if os.path.exists(path):
        return pd.read_csv(path)
    st.error(f"Data file for {country} not found!")
    return pd.DataFrame()

def plot_boxplot(df, metric):
    plt.figure(figsize=(8, 4))
    sns.boxplot(x="country", y=metric, data=df)
    plt.title(f"{metric} Distribution by Country")
    st.pyplot(plt.gcf())
    plt.clf()

def get_summary(df):
    summary = df.groupby("country")[["GHI", "DNI", "DHI"]].agg(["mean", "median", "std"])
    return summary.round(2)

def main():
    st.title("Comparative Analysis of Solar Metrics")
    st.markdown("Compare **GHI**, **DNI**, and **DHI** across Benin, SierraLeone, and Togo.")

    countries = ["Benin", "SierraLeone", "Togo"]
    selected_countries = st.multiselect("Select Countries", countries, default=countries)

    if not selected_countries:
        st.warning("Please select at least one country.")
        return

    # Load and combine selected country data
    dfs = []
    for country in selected_countries:
        df = load_data(country)
        if not df.empty:
            df["country"] = country
            dfs.append(df)

    if not dfs:
        st.error("No data available to display.")
        return

    data = pd.concat(dfs, ignore_index=True)

    # Boxplots for GHI, DNI, DHI
    st.subheader(" Boxplots of Solar Metrics")
    for metric in ["GHI", "DNI", "DHI"]:
        plot_boxplot(data, metric)

    # Summary table
    st.subheader(" Summary Table")
    summary_table = get_summary(data)
    st.dataframe(summary_table)

    # Bar chart for average GHI
    st.subheader(" Average GHI by Country")
    avg_ghi = data.groupby("country")["GHI"].mean().sort_values(ascending=False)
    st.bar_chart(avg_ghi)

if __name__ == "__main__":
    main()
