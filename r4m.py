{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "95b10c83-039d-43f4-ac8f-aac5642d7ad4",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import streamlit as st\n",
    "from typing import Any\n",
    "import plotly as plo"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "14b6cb5f-70ff-4c5c-b41b-450a581245cb",
   "metadata": {},
   "outputs": [],
   "source": [
    "datafile = pd.read_csv('C:\\\\Users\\\\savma\\\\dev_boilerplate_course\\\\dev_boilerplate_course\\\\src\\\\data\\\\run4moreProd.activities.csv')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "f4c9f338-1151-417e-90e9-16a7dbea5e07",
   "metadata": {},
   "outputs": [],
   "source": [
    "activities_datafile = 'C:\\\\Users\\\\savma\\\\dev_boilerplate_course\\\\dev_boilerplate_course\\\\src\\\\data\\\\run4moreProd.activities.csv'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "5ccc81be-8060-4f4c-814c-387bb163a414",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>_id</th>\n",
       "      <th>distance</th>\n",
       "      <th>pace.hours</th>\n",
       "      <th>pace.minutes</th>\n",
       "      <th>pace.seconds</th>\n",
       "      <th>points</th>\n",
       "      <th>time.hours</th>\n",
       "      <th>time.minutes</th>\n",
       "      <th>time.seconds</th>\n",
       "      <th>user_id</th>\n",
       "      <th>createdAt</th>\n",
       "      <th>type</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>62873d1f181a6d5adf0f62b2</td>\n",
       "      <td>0.17</td>\n",
       "      <td>0</td>\n",
       "      <td>14</td>\n",
       "      <td>39</td>\n",
       "      <td>17</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>33</td>\n",
       "      <td>6206e062fb2d16fd06802520</td>\n",
       "      <td>2022-05-20T07:02:55.295Z</td>\n",
       "      <td>walk-run</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>62873d8e181a6d5adf0f62c2</td>\n",
       "      <td>4.10</td>\n",
       "      <td>0</td>\n",
       "      <td>13</td>\n",
       "      <td>19</td>\n",
       "      <td>410</td>\n",
       "      <td>0</td>\n",
       "      <td>54</td>\n",
       "      <td>41</td>\n",
       "      <td>6251c082520daa3cd653d214</td>\n",
       "      <td>2022-05-20T07:04:46.043Z</td>\n",
       "      <td>walk-run</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>62874060181a6d5adf0f62f0</td>\n",
       "      <td>0.15</td>\n",
       "      <td>0</td>\n",
       "      <td>17</td>\n",
       "      <td>32</td>\n",
       "      <td>15</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>40</td>\n",
       "      <td>6206e062fb2d16fd06802520</td>\n",
       "      <td>2022-05-20T07:16:48.452Z</td>\n",
       "      <td>walk-run</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>628740a3181a6d5adf0f62fd</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>59</td>\n",
       "      <td>6206e062fb2d16fd06802520</td>\n",
       "      <td>2022-05-20T07:17:55.980Z</td>\n",
       "      <td>walk-run</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>62874460181a6d5adf0f6318</td>\n",
       "      <td>0.54</td>\n",
       "      <td>0</td>\n",
       "      <td>10</td>\n",
       "      <td>2</td>\n",
       "      <td>54</td>\n",
       "      <td>0</td>\n",
       "      <td>5</td>\n",
       "      <td>29</td>\n",
       "      <td>6206e062fb2d16fd06802520</td>\n",
       "      <td>2022-05-20T07:33:52.419Z</td>\n",
       "      <td>walk-run</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                        _id  distance  pace.hours  pace.minutes  pace.seconds  \\\n",
       "0  62873d1f181a6d5adf0f62b2      0.17           0            14            39   \n",
       "1  62873d8e181a6d5adf0f62c2      4.10           0            13            19   \n",
       "2  62874060181a6d5adf0f62f0      0.15           0            17            32   \n",
       "3  628740a3181a6d5adf0f62fd      0.00           0             0             0   \n",
       "4  62874460181a6d5adf0f6318      0.54           0            10             2   \n",
       "\n",
       "   points  time.hours  time.minutes  time.seconds                   user_id  \\\n",
       "0      17           0             2            33  6206e062fb2d16fd06802520   \n",
       "1     410           0            54            41  6251c082520daa3cd653d214   \n",
       "2      15           0             2            40  6206e062fb2d16fd06802520   \n",
       "3       0           0             0            59  6206e062fb2d16fd06802520   \n",
       "4      54           0             5            29  6206e062fb2d16fd06802520   \n",
       "\n",
       "                  createdAt      type  \n",
       "0  2022-05-20T07:02:55.295Z  walk-run  \n",
       "1  2022-05-20T07:04:46.043Z  walk-run  \n",
       "2  2022-05-20T07:16:48.452Z  walk-run  \n",
       "3  2022-05-20T07:17:55.980Z  walk-run  \n",
       "4  2022-05-20T07:33:52.419Z  walk-run  "
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "datafile.head(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "37cb72ea-6fa1-487c-96ce-d5a9feebb4d9",
   "metadata": {},
   "outputs": [],
   "source": [
    "def csv_from_mongo_to_dfs(datafile: str) -> tuple[Any, pd.DataFrame]:\n",
    "    df = pd.read_csv(datafile)\n",
    "    assert isinstance(pd.to_datetime(df[\"createdAt\"]).dt.date, object)\n",
    "    df[\"date\"] = pd.to_datetime(df[\"createdAt\"]).dt.date\n",
    "    df = df.drop(\"_id\", axis=1)\n",
    "    # place date column as first column\n",
    "    date = df.pop(\"date\")\n",
    "    df.insert(loc=0, column=\"date\", value=date)\n",
    "    df_acts = df.groupby(\"date\").size().to_frame(name=\"activities\").reset_index()\n",
    "    df_users = df.groupby(\"date\")[\"user_id\"].nunique().reset_index()\n",
    "    df_users.rename(columns={\"user_id\": \"users\"}, inplace=True)\n",
    "    return df_acts, df_users\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "eec59905-6ebb-4c77-ae12-5f4994c8b978",
   "metadata": {},
   "outputs": [],
   "source": [
    "def date_slider(df: pd.DataFrame) -> tuple:\n",
    "    slider_dates = st.sidebar.slider(\n",
    "        \"# Pick a date range\",\n",
    "        df.date.min(),\n",
    "        df.date.max(),\n",
    "        (df.date.min(), df.date.max()),\n",
    "    )\n",
    "    return slider_dates"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "856e76ef-dc22-40ec-8245-d8291955abac",
   "metadata": {},
   "outputs": [],
   "source": [
    "def update_df_dates(df: pd.DataFrame, slider_dates: tuple) -> pd.DataFrame:\n",
    "    date_range = (df.date >= slider_dates[0]) & (df.date <= slider_dates[1])\n",
    "    filter_df_dates = df.loc[date_range]\n",
    "    return filter_df_dates"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "6ef196cb-ffbd-4042-9904-c386f0eeb657",
   "metadata": {},
   "outputs": [],
   "source": [
    "def plot_daily(df: pd.DataFrame) -> st.plotly_chart:\n",
    "    # streamlit with plotly chart\n",
    "    fig = px.line(df, x=\"date\", y=df.columns[1])\n",
    "    st.plotly_chart(fig)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "3db7f4cb-0c3b-475f-b382-7f8e156bb0bd",
   "metadata": {},
   "outputs": [],
   "source": [
    "def plot_daily_dashboard(datafile: str):\n",
    "    df_acts, df_users = csv_from_mongo_to_dfs(datafile)\n",
    "    slider_dates = date_slider(df_acts)\n",
    "    st.header(df_acts.columns[1].capitalize())\n",
    "    df_acts = update_df_dates(df_acts, slider_dates)\n",
    "    plot_daily(df_acts)\n",
    "    st.header(df_users.columns[1].capitalize())\n",
    "    df_users = update_df_dates(df_users, slider_dates)\n",
    "    plot_daily(df_users)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6f4c24bb-59ec-475b-a5bf-055d66c5b3c2",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d3329666-44f5-4e53-9458-3acd5e180d49",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
