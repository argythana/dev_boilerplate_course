import pandas as pd
import streamlit as st
import plotly.express as px
from typing import Any


datafile = "./data/run4moreProd.activities.csv"
# TODO!: Show why this is wrong and why we should use the code above.
# Although it works from my PC and different folders within the project.
# datafile = "C:/Users/tharg/dev_boilerplate_course/src/data/run4moreProd.activities.csv"


activities_datafile = "./data/run4moreProd.activities.csv"

# TODO!: Show why the code below is wrong and why we should use the code as is above.
#  Although it works from my PC and different folders within the project.
# datafile = "C:/Users/tharg/dev_boilerplate_course/src/data/run4moreProd.activities.csv"


def get_averages(datafile: str) -> pd.DataFrame:
    df = pd.read_csv(datafile)
    df["date"] = pd.to_datetime(df["createdAt"]).dt.date
    df_avg = df.groupby("date")["distance"].mean().reset_index()
    return df_avg


def csv_from_mongo_to_dfs(datafile: str) -> tuple[Any, pd.DataFrame]:
    """
    Read a csv datafile, and return users and activities dataframes grouped by date.
    Args:
        datafile: A csv datafile that has all activities' data.
    Returns:
        A tuple of two dataframes, users and activities.
    """
    df = pd.read_csv(datafile)
    assert isinstance(pd.to_datetime(df["createdAt"]).dt.date, object)
    df["date"] = pd.to_datetime(df["createdAt"]).dt.date
    df = df.drop("_id", axis=1)
    # place date column as first column
    date = df.pop("date")
    df.insert(loc=0, column="date", value=date)
    df_acts = df.groupby("date").size().to_frame(name="activities").reset_index()
    df_users = df.groupby("date")["user_id"].nunique().reset_index()
    df_users.rename(columns={"user_id": "users"}, inplace=True)
    return df_acts, df_users


def csv_from_mongo_to_df(datafile):
    df = pd.read_csv(datafile)
    assert isinstance(pd.to_datetime(df["createdAt"]).dt.date, object)
    df["date"] = pd.to_datetime(df["createdAt"]).dt.date
    df = df.drop("_id", axis=1)

    # Calculate the total distance per day
    df_distances = df.groupby("date")["distance"].sum().reset_index()

    # Calculate the average distance per day
    df_avg_distances = df.groupby("date")["distance"].mean().reset_index()

    # Calculate the total points per day
    df_points = df.groupby("date")["points"].sum().reset_index()

    return df_distances, df_avg_distances, df_points



def date_slider(df: pd.DataFrame) -> tuple:
    slider_dates = st.sidebar.slider(
        "Pick a date range",
        df.date.min(),
        df.date.max(),
        (df.date.min(), df.date.max()),
    )
    return slider_dates

# def date_slider(df: pd.DataFrame, key: str) -> tuple:
#     slider_dates = st.sidebar.slider(
#         "# Pick a date range",
#         df.date.min(),
#         df.date.max(),
#         (df.date.min(), df.date.max()),
#         key=key,
#     )
#     return slider_dates

def update_df_dates(df: pd.DataFrame, slider_dates: tuple) -> pd.DataFrame:
    date_range = (df.date >= slider_dates[0]) & (df.date <= slider_dates[1])
    filter_df_dates = df.loc[date_range]
    return filter_df_dates


def plot_daily(df: pd.DataFrame) -> st.plotly_chart:
    # streamlit with plotly chart
    fig = px.line(df, x="date", y=df.columns[1])
    st.plotly_chart(fig)


def plot_points(df: pd.DataFrame):
    fig = px.bar(df, x="date", y="points")
    st.plotly_chart(fig)

def plot_daily_dashboard(datafile: str):
    df_acts, df_users = csv_from_mongo_to_dfs(datafile)
    slider_dates = date_slider(df_acts, key='slider_daily_totals')
    st.header(df_acts.columns[1].capitalize())
    df_acts = update_df_dates(df_acts, slider_dates)
    plot_daily(df_acts)
    st.header(df_users.columns[1].capitalize())
    df_users = update_df_dates(df_users, slider_dates)
    plot_daily(df_users)


def plot_daily_dashboard_choice(datafile: str, metric: str):
    df_distances, df_avg_distances, df_points = csv_from_mongo_to_df(datafile)
    slider_dates = date_slider(df_distances)

    st.header(f"Total {metric} per Day")

    if metric == "Distance":
        df = update_df_dates(df_distances, slider_dates)
        plot_daily(df, y_column="distance")
    elif metric == "Average Distance":
        df = update_df_dates(df_avg_distances, slider_dates)
        plot_daily(df, y_column="distance")
    elif metric == "Points":
        df = update_df_dates(df_points, slider_dates)
        plot_points(df)

def plot_daily_averages(datafile: str):
    df_avg = get_averages(datafile)
    slider_dates_averages = date_slider(df_avg, 'slider_daily_averages')
    st.header(df_avg.columns[1].capitalize())
    df_avg = update_df_dates(df_avg, slider_dates_averages)
    plot_daily(df_avg)



if __name__ == "__main__":
    st.title("Total Distance and Points per Day Visualization")

    metrics = ["Distance", "Average Distance", "Points"]
    selected_metric = st.sidebar.selectbox("Select Metric", metrics)

    plot_daily_dashboard_choice(datafile, selected_metric)