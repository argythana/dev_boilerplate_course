import pandas as pd
import streamlit as st
import plotly.express as px


datafile = "./data/run4moreProd.activities.csv"
# TODO!: Show why this is wrong and why we should use the code above.
# Although it works from my PC and different folders within the project.
# datafile = "C:/Users/tharg/dev_boilerplate_course/src/data/run4moreProd.activities.csv"


def csv_from_mongo_to_df(datafile: str) -> pd.DataFrame:
    """ """
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


def date_slider(df: pd.DataFrame) -> tuple:
    slider_dates = st.sidebar.slider(
        "# Pick a date range",
        df.date.min(),
        df.date.max(),
        (df.date.min(), df.date.max()),
    )
    return slider_dates


def update_df_dates(df: pd.DataFrame, slider_dates: tuple) -> pd.DataFrame:
    date_range = (df.date >= slider_dates[0]) & (df.date <= slider_dates[1])
    filter_df_dates = df.loc[date_range]
    return filter_df_dates


def plot_daily(df: pd.DataFrame) -> st.plotly_chart:
    # streamlit with plotly chart
    fig = px.line(df, x="date", y=df.columns[1])
    st.plotly_chart(fig)


def plot_daily_dashboard(datafile: str):
    df_acts, df_users = csv_from_mongo_to_df(datafile)
    slider_dates = date_slider(df_acts)
    st.header(df_acts.columns[1].capitalize())
    df_acts = update_df_dates(df_acts, slider_dates)
    plot_daily(df_acts)
    st.header(df_users.columns[1].capitalize())
    df_users = update_df_dates(df_users, slider_dates)
    plot_daily(df_users)
