import pandas as pd
import streamlit as st
import plotly.express as px



datafile = "./../data/run4moreProd.activities.csv"

def csv_from_mongo_to_df(datafile):
    df = pd.read_csv(datafile)
    assert isinstance(pd.to_datetime(df["createdAt"]).dt.date, object)
    df["date"] = pd.to_datetime(df["createdAt"]).dt.date
    df = df.drop("_id", axis=1)

    # Calculate the total distance per day
    df_distances = df.groupby("date")["distance"].sum().reset_index()

    # Calculate the total points per day
    df_points = df.groupby("date")["points"].sum().reset_index()

    return df_distances, df_points

def date_slider(df: pd.DataFrame) -> tuple:
    slider_dates = st.sidebar.slider(
        "Pick a date range",
        df.date.min(),
        df.date.max(),
        (df.date.min(), df.date.max()),
    )
    return slider_dates

def update_df_dates(df: pd.DataFrame, slider_dates: tuple) -> pd.DataFrame:
    date_range = (df["date"] >= slider_dates[0]) & (df["date"] <= slider_dates[1])
    filter_df_dates = df[date_range]
    return filter_df_dates

def plot_daily(df: pd.DataFrame):
    fig = px.line(df, x="date", y="distance")
    st.plotly_chart(fig)

def plot_points(df: pd.DataFrame):
    fig = px.bar(df, x="date", y="points")
    st.plotly_chart(fig)

def plot_daily_dashboard(datafile: str):
    df_distances, df_points = csv_from_mongo_to_df(datafile)
    slider_dates = date_slider(df_distances)
    st.header("Total Distance per Day")
    df_distances = update_df_dates(df_distances, slider_dates)
    plot_daily(df_distances)
    st.header("Total Points per Day")
    df_points = update_df_dates(df_points, slider_dates)
    plot_points(df_points)

if __name__ == "__main__":
    st.title("Total Distance and Points per Day Visualization")
    plot_daily_dashboard(datafile)